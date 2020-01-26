import re
import os
import sys
import binascii
import subprocess
import secrets

from collections import namedtuple
from bottle import get, post, request, response
from bottle import run, static_file, redirect, template

#   ____                __  _
#  / ___| ___   _ __   / _|(_)  __ _  ___
# | |    / _ \ | '_ \ | |_ | | / _` |/ __|
# | |___| (_) || | | ||  _|| || (_| |\__ \
#  \____|\___/ |_| |_||_|  |_| \__, ||___/
#                              |___/

PHANTOMJS = "/usr/bin/phantomjs"
JS_FILE = "/home/web/load_page.js"
ENABLE_PHANTOMJS = True # should always be true unless testing webapp

POSTS = []

# Object type for Posts
Post = namedtuple("post", ["name", "text"])

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
def show_posts():
    return template('templates/posts.tpl',{"posts": POSTS})

@post('/')
def create_post():
    username = request.forms.get('name')
    posttext = request.forms.get('posttext')
    newpost = Post(username, posttext)

    POSTS.append(newpost)
    if ENABLE_PHANTOMJS:
        subprocess.Popen([PHANTOMJS, JS_FILE], stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
            )

    return template('templates/posts.tpl',{"posts": POSTS})

if __name__ == "__main__":

    POSTS.append(Post("Oreo","Oh-Oh-Oh - Ice cold milk and an Oreo cookie."))
    POSTS.append(Post("Chips Ahoy","A 1000 chips delicious!"))
    POSTS.append(Post("The Cookie Monster","COoooOKIes? nOO One sTEAling me COokiES. mE cOOkies ARe VerRy veRRY SafE!"))

    run(host='0.0.0.0', port=8080)
