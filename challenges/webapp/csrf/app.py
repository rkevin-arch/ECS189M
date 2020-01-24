import re
import os
import binascii
import subprocess
import secrets

from collections import namedtuple
from bottle import get, post, request, response
from bottle import run, static_file, redirect, template

flag="ECS{1M4G1N3_TH15_8UT_D3L3T1NG_4LL_U53R5_B702F71E4C2139B5F1E9F3A32B8BACA3}"

#   ____                __  _
#  / ___| ___   _ __   / _|(_)  __ _  ___
# | |    / _ \ | '_ \ | |_ | | / _` |/ __|
# | |___| (_) || | | ||  _|| || (_| |\__ \
#  \____|\___/ |_| |_||_|  |_| \__, ||___/
#                              |___/

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = secrets.token_hex()
ADMIN_SESSID = secrets.token_hex()
COOKIE_SESS = "webchal_csrf_forum_sessid"
DEFAULT_PASSWORD = "password"
PHANTOMJS = "/usr/bin/phantomjs"
JS_FILE = "/home/web/load_page.js"
ENABLE_PHANTOMJS = True # should always be true unless testing webapp

# Cookies for active users. schema { sess_id : username }
# By default admin is logged in.
#  we need this so admin can "click" links
ACTIVE_SESSIONS = {}
AUTHDB = {
    ADMIN_USERNAME: ADMIN_PASSWORD,
}
POSTS = []

# Object type for Posts
Post = namedtuple("post", ["name", "text"])


#  _   _  _    _  _
# | | | || |_ (_)| | ___
# | | | || __|| || |/ __|
# | |_| || |_ | || |\__ \
#  \___/  \__||_||_||___/
#
def check_user_pass(usr, pwd):
    """ Return True if username and password are valid. """

    ret = AUTHDB.get(usr, None)
    if (ret is None) or (ret != pwd):
        return False
    return True


def is_authed(sess_id):
    """ check if the user is authenticated already """

    # check if cookie exists and is valid
    if sess_id in ACTIVE_SESSIONS:
        return True
    return False

@get('/reset')
def reset():
    """ reset the given user's password back to default """

    sess = request.get_cookie(COOKIE_SESS)
    username = request.query.get("username", None)
    errormsg = ""

    # validate active session, and username
    if ACTIVE_SESSIONS.get(sess, None) != username:
        errormsg = "You can only reset your own password"
    else:
        AUTHDB[username] = DEFAULT_PASSWORD
        errormsg = "Password reset! Your password has been changed to 'password'."

    return template('templates/message.tpl',
                    {"msg": errormsg})

@get('/logout')
def logout():
    """ Logout. clear cookie and active sessions """

    # get cookie and clear it
    sess = request.get_cookie(COOKIE_SESS)
    response.set_cookie(COOKIE_SESS, "", httponly=True)

    # ignore if it doesn't exist.
    try:
        ACTIVE_SESSIONS.pop(sess)
    except KeyError as e:
        print(e, "Sessions %s doesn't exist" % sess)
    return template('templates/message.tpl',
                    {"msg": "You have logged out."})


#  ____                _
# |  _ \  ___   _   _ | |_  ___  ___
# | |_) |/ _ \ | | | || __|/ _ \/ __|
# |  _ <| (_) || |_| || |_|  __/\__ \
# |_| \_\\___/  \__,_| \__|\___||___/
#
@get(r"/static/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="static/css")


#  __  __        _    _                 _
# |  \/  |  ___ | |_ | |__    ___    __| | ___
# | |\/| | / _ \| __|| '_ \  / _ \  / _` |/ __|
# | |  | ||  __/| |_ | | | || (_) || (_| |\__ \
# |_|  |_| \___| \__||_| |_| \___/  \__,_||___/

@get('/')
def index():

    # Check if the user session is active, if not send to login page
    sess_id = request.get_cookie(COOKIE_SESS)
    if not is_authed(sess_id):
        return template('templates/login.tpl', {})

    # Show posts
    redirect('/main')

@post('/register')
def register():

    # Check if the user session is active, if not send to login page
    sess_id = request.get_cookie(COOKIE_SESS)
    if is_authed(sess_id):
        redirect('/')

    username = request.forms.get('username')
    password = request.forms.get('password')

    if not username or not password:
        return template('templates/message.tpl', {'msg': 'Username or password cannot be blank!'})

    if AUTHDB.get(username, None) is not None:
        return template('templates/message.tpl', {'msg': 'That user already exists!'})

    AUTHDB.update({username:password})
    return template('templates/message.tpl', {'msg': 'You have successfully registered! Please log in.'})

@post('/login')
def login():
    """ handle post data from login form """

    # delete cookie if it exists
    response.set_cookie(COOKIE_SESS, "", httponly=True)

    username = request.forms.get('username')
    password = request.forms.get('password')

    if check_user_pass(username, password):
        # set cookie
        sess = secrets.token_hex()
        response.set_cookie(COOKIE_SESS, sess, httponly=True)
        ACTIVE_SESSIONS.update({sess: username})

        # Welcome and show posts
        redirect('/main')
    else:
        # failed auth.
        return template('templates/message.tpl',
                        {"msg": "Incorrect Login credentials."})

@get('/main')
def mainpage():
    # Check if the user session is active, if not send to login page
    sess_id = request.get_cookie(COOKIE_SESS)
    if not is_authed(sess_id):
        return template('templates/message.tpl',
                        {"msg": "Please login first."})

    errormsg = ""
    username = ACTIVE_SESSIONS[sess_id]
    print(sess_id, username)
    print(ACTIVE_SESSIONS)

    if username == ADMIN_USERNAME:
        errormsg = "You found the flag: %s" % flag

    return template('templates/main.tpl',
                    {"errormsg": errormsg, "username": username})


@get('/posts')
def show_posts():
    """ lists posts """

    # Check if the user session is active, if not send to login page
    sess_id = request.get_cookie(COOKIE_SESS)
    if not is_authed(sess_id):
        print(sess_id,"not authed")
        return template('templates/message.tpl',
                        {"msg": "Please login first."})

    errormsg = ""
    username = ACTIVE_SESSIONS[sess_id]
    print(sess_id, username)
    print(ACTIVE_SESSIONS)

    if username == ADMIN_USERNAME:
        errormsg = "You found the flag: %s" % flag

    #print(errormsg)
    return template('templates/posts.tpl',
                    {
                        "posts": POSTS,
                        "errormsg": errormsg})


@post('/post')
def create_post():
    """ create new post """

    # Check if the user session is active, if not send to login page
    sess_id = request.get_cookie(COOKIE_SESS)
    if not is_authed(sess_id):
        return template('templates/message.tpl',
                        {"msg": "Please login first."})

    # get form data
    errormsg = ""
    username = ACTIVE_SESSIONS[sess_id]
    posttext = request.forms.get('posttext')
    newpost = Post(username, posttext)

    POSTS.append(newpost)
    if ENABLE_PHANTOMJS:
        subprocess.Popen([PHANTOMJS, JS_FILE, ADMIN_SESSID], stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
            )

    return redirect('/posts')

if __name__ == "__main__":

    # update sessions and db with creds
    ACTIVE_SESSIONS.update({
        ADMIN_SESSID: ADMIN_USERNAME})
    AUTHDB.update({
        ADMIN_USERNAME: ADMIN_PASSWORD,
    })

    # print("ADMIN_COOKIE: ", ADMIN_SESSID)

    # prime some posts

    POSTS.append(Post("admin","Muahahahaha! I have a flag on this forum that only I can see!"))
    POSTS.append(Post("rkevin","Jerk."))
    POSTS.append(Post("ectoChemist","hey there! do you mind sharing the flag with me? pleeeease? :B"))
    POSTS.append(Post("admin","Nope! I'm just gonna watch all of your posts and how badly you want the flag but can't get it! Muahahahaha!"))
    POSTS.append(Post("Thab West","You meanieface! That's not nice."))

    run(host='0.0.0.0', port=8080)
