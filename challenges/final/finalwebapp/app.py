import re
import os
import binascii
import subprocess
import secrets
import bottle
import mysql.connector
import time

from collections import namedtuple
from bottle import get, post, request, response, abort
from bottle import run, static_file, redirect, template

flag="ECS{placeholder}"
pt1_msg="Note: You're 1/3 of the way from solving this challenge. Detail how you got here in your writeup and you will have at least 175 points from this challenge."
pt2_msg="Note: You're 2/3 of the way from solving this challenge! Detail how you got here in your writeup and you will have at least 350 points from this challenge."

OPERATOR_SESSID = secrets.token_hex()
COOKIE_SESS = "webchal_final_sessid"
PHANTOMJS = "/usr/bin/phantomjs"
JS_FILE = "/home/web/load_page.js"
ENABLE_PHANTOMJS = False # should always be true unless testing webapp

# Cookies for active users. schema { sess_id : username }
# By default admin is logged in.
#  we need this so admin can "click" links
ACTIVE_SESSIONS = {}

#  _   _  _    _  _
# | | | || |_ (_)| | ___
# | | | || __|| || |/ __|
# | |_| || |_ | || |\__ \
#  \___/  \__||_||_||___/
#

def getdb():
    global conn
    return conn.cursor(buffered=True)

#  ____                _
# |  _ \  ___   _   _ | |_  ___  ___
# | |_) |/ _ \ | | | || __|/ _ \/ __|
# |  _ <| (_) || |_| || |_|  __/\__ \
# |_| \_\\___/  \__,_| \__|\___||___/
#
@get(r"/static/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="static/css")

@get(r"/static/js/<filepath:re:.*\.js>")
def css(filepath):
    return static_file(filepath, root="static/js")

@get(r"/static/css/<filepath:re:.*\.woff>")
def css(filepath):
    return static_file(filepath, root="static/css")




#  __  __        _    _                 _
# |  \/  |  ___ | |_ | |__    ___    __| | ___
# | |\/| | / _ \| __|| '_ \  / _ \  / _` |/ __|
# | |  | ||  __/| |_ | | | || (_) || (_| |\__ \
# |_|  |_| \___| \__||_| |_| \___/  \__,_||___/

@get('/')
def index():
    sess_id = request.get_cookie(COOKIE_SESS)
    msg = ''

    if sess_id not in ACTIVE_SESSIONS:
        return template('templates/notloggedin.tpl', {'msg': msg})
    if ACTIVE_SESSIONS[sess_id] != "operator":
        return template('templates/submit_plans.tpl', {'msg': msg})

    db=getdb()
    db.execute("SELECT * FROM plans_awaiting_approval;")
    plans=db.fetchall()
    db.close()
    plans=[{'title': title, 'description': description, 'id': id} for title, description, id in plans]
    return template('templates/approve_plans.tpl', {'msg': msg, 'plans': plans})

@post('/submitplan')
def submit_plan():
    """ Submit plan for secret plan """

    sess_id = request.get_cookie(COOKIE_SESS)

    if sess_id not in ACTIVE_SESSIONS:
        return template('templates/notloggedin.tpl', {'msg':""})
    if ACTIVE_SESSIONS[sess_id] == "operator":
        return template('templates/approve_plans.tpl', {'msg': "The operator may not submit plans."})
    title = request.forms.get('title')
    description = request.forms.get('description')
    db=getdb()
    try:
        db.execute("SELECT * FROM plans_awaiting_approval, approved_plans WHERE title = %s", (title))
        if db.rowcount != 0:
            return template('templates/submit_plans.tpl', {'msg':
                            'A plan with that name already exists in the database.'})
        db.execute("INSERT INTO plans_awaiting_approval (title, description) VALUES (%s,%s)", (title, description))
        return template('templates/submit_plans.tpl', {'msg':
                        'Plan submitted, awaiting operator approval.'})
    except mysql.connector.errors.ProgrammingError as e:
        return template('templates/submit_plans.tpl', {'msg': str(e)})
    finally:
        db.close()

@post('/approveplan')
def approve_plan():
    """ Approve plan """
    pass

@post('/login')
def login():
    """ handle post data from login form """

    # delete cookie if it exists
    #response.set_cookie(COOKIE_SESS, "", httponly=True)

    username = request.forms.get('username')
    password = request.forms.get('password')

    msg = ''

    db = getdb()
    try:
        db.execute("SELECT * FROM users WHERE username = '%s' AND password = '%s'"%(username,password))

        if db.rowcount == 0:
            msg = 'No username/password combo matched in the database.'
        if db.rowcount >= 2:
            msg = 'Database returned more than one row. Login failed.'

        user = db.fetchone()[0]
        if user == 'operator':
            msg = 'The operator is already logged in, you may only login as a non-operator.'

    except mysql.connector.errors.ProgrammingError as e:
        msg = str(e)
    finally:
        db.close()
    if msg:
        return template('templates/notloggedin.tpl', {'msg': msg})

    sess = secrets.token_hex()
    response.set_cookie(COOKIE_SESS, sess)
    ACTIVE_SESSIONS.update({sess: user})
    redirect('/')

if __name__ == "__main__":
    global conn
    conn=mysql.connector.connect(user="db_user", password="1b93b39ccc87a8495ded6410752acc6c", unix_socket="/var/run/mysqld/mysqld.sock", database='redshift_plan_tracker')

    bottle.debug(True)
    ACTIVE_SESSIONS.update({OPERATOR_SESSID: "operator"})

    run(host='0.0.0.0', port=8080, reloader=False)

