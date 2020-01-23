import re
import os
import asyncio
import binascii

import subprocess

from collections import namedtuple
from bottle import get, post, request, response
from bottle import run, static_file, redirect, template

flag="123"

#   ____                __  _
#  / ___| ___   _ __   / _|(_)  __ _  ___
# | |    / _ \ | '_ \ | |_ | | / _` |/ __|
# | |___| (_) || | | ||  _|| || (_| |\__ \
#  \____|\___/ |_| |_||_|  |_| \__, ||___/
#                              |___/

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = None
ADMIN_SESSID = None
COOKIE_SESS = "tp_sessid"
DEFAULT_PASSWORD = "slartibartfast"
REGEX_LINKS = re.compile(r'<a href.*(?P<link>http.[^\">]*)', re.DOTALL|re.M|re.I)
POSTS_LIMIT = 10
PHANTOMJS = "/usr/bin/phantomjs"
JS_FILE = "/home/web/load_page.js"

# Cookies for active users. schema { sess_id : username }
# By default admin is logged in.
#  we need this so admin can "click" links
ACTIVE_SESSIONS = {}
AUTHDB = {
    ADMIN_USERNAME: ADMIN_PASSWORD,
    'user': 'slartibartfast',
    'oolon colluphid': 'bob'
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


def generate_cookie(num_bytes=16):
    """ generate a random string of @num_bytes chars """
    return binascii.hexlify(os.urandom(num_bytes)).decode('utf-8')


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
        errormsg = "Password reset"

    return template('templates/login.tpl',
                    {"errormsg": errormsg})


def logout():
    """ Logout. clear cookie and active sessions """

    # get cookie and clear it
    sess = request.get_cookie(COOKIE_SESS)
    response.set_cookie(COOKIE_SESS, "")

    # ignore if it doesn't exist.
    try:
        ACTIVE_SESSIONS.pop(sess)
    except KeyError as e:
        print(e, "Sessions %s doesn't exist" % sess)
    return template('templates/login.tpl',
                    {"errormsg": "Logged out."})


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
        return template('templates/login.tpl', {"errormsg": ""})

    # Check if we're logging out
    logout_param = request.query.get('logout', None)
    if logout_param:
        return logout()

    # Check if we're resetting password
    reset_param = request.query.get('reset', None)
    if reset_param:
        return reset()

    # Show posts
    redirect('/posts')


@post('/')
def login():
    """ handle post data from login form """

    # delete cookie if it exists
    response.set_cookie(COOKIE_SESS, "")

    username = request.forms.get('username')
    password = request.forms.get('password')

    if check_user_pass(username, password):
        # set cookie
        sess = generate_cookie()
        response.set_cookie(COOKIE_SESS, sess)
        ACTIVE_SESSIONS.update({sess: username})

        # Welcome and show posts
        redirect('/posts')
    else:
        # failed auth.
        return template('templates/login.tpl',
                        {"errormsg": "Incorrect Login credentials."})

    raise Exception("Shouldn't get here. So let's freakout.")


@get('/posts')
def show_posts():
    """ lists posts """

    # Check if the user session is active, if not send to login page
    sess_id = request.get_cookie(COOKIE_SESS)
    if not is_authed(sess_id):
        return template('templates/login.tpl',
                        {"errormsg": "Please login first."})

    errormsg = ""
    username = ACTIVE_SESSIONS[sess_id]
    print(sess_id, username)
    print(ACTIVE_SESSIONS)

    if username == ADMIN_USERNAME:
        errormsg = "You found the: flag %s" % flag

    print(errormsg)
    return template('templates/posts.tpl',
                    {"username": username,
                        "posts": POSTS,
                        "errormsg": errormsg})


@post('/posts')
def create_posts():
    """ create new post """

    # Check if the user session is active, if not send to login page
    sess_id = request.get_cookie(COOKIE_SESS)
    if not is_authed(sess_id):
        return template('templates/login.tpl',
                        {"errormsg": "Please login first."})

    # get form data
    errormsg = ""
    username = ACTIVE_SESSIONS[sess_id]
    posttext = request.forms.get('posttext')
    newpost = Post(username, posttext)

    # check we're at limit of posts
    if len(POSTS) < POSTS_LIMIT:
        POSTS.append(newpost)
        subprocess.Popen([PHANTOMJS, JS_FILE, ADMIN_SESSID], stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
            )
    else:
        errormsg = "Too many posts. Max 10."

    return template('templates/posts.tpl',
                    {"username": username,
                        "posts": POSTS,
                        "errormsg": errormsg})


if __name__ == "__main__":

    # init admin password and cookie
    ADMIN_PASSWORD = generate_cookie()
    ADMIN_SESSID = generate_cookie()

    # update sessions and db with creds
    ACTIVE_SESSIONS.update({
        ADMIN_SESSID: ADMIN_USERNAME})
    AUTHDB.update({
        ADMIN_USERNAME: ADMIN_PASSWORD,
    })

    print("ADMIN_COOKIE: ", ADMIN_SESSID)
    # prime some posts
    for i in range(3):
        newpost = Post("ljsdf", "slkdjflaksjdflajdsf")
        POSTS.append(newpost)

    run(host='0.0.0.0', port=8080)
