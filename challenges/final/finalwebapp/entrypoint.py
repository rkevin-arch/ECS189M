#!/usr/bin/python3
from subprocess import Popen
import os
Popen(["service", "mysql", "start"])
os.setresuid(1340, 1340, 1340)
os.execve("/usr/bin/python3", ["python3", "app.py"], os.environ)
