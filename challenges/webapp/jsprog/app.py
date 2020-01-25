import re
import os
import binascii
import subprocess
import secrets

from collections import namedtuple
from bottle import get, post, request, response
from bottle import run, static_file, redirect, template

PHANTOMJS = "/usr/bin/phantomjs"
JS_FILE = "/home/web/load_page.js"
ENABLE_PHANTOMJS = True # should always be true unless testing webapp

@get('/')
def index():
    return template('templates/index.tpl', {"code": "", "msg": []})

@post('/')
def answer():
    js=request.forms.get('code')

    if js is None:
        p="You didn't submit any code!"

    if ENABLE_PHANTOMJS:
        p=subprocess.run([PHANTOMJS, JS_FILE, js], stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        p=p.stdout.decode()
    else:
        p="You should never see this. Contact Kevin because he forgot to remove testing code."

    return template('templates/index.tpl', {"code": js, "msg": p.split('\n')})

@get('/reflect')
def reflectdummypage():
    if request.environ.get('REMOTE_ADDR')=='127.0.0.1': #this works behind beamsplitter cuz docker doesn't use localhost when forwarding requests
        return template('templates/reflect.tpl')
    else:
        return template('templates/cheat.tpl')

@get('/flag')
def reflectdummypage():
    if request.environ.get('REMOTE_ADDR')=='127.0.0.1':
        return template('templates/flag.tpl')
    else:
        return template('templates/cheat.tpl')

if __name__ == "__main__":
    run(host='0.0.0.0', port=8080, server='paste')
