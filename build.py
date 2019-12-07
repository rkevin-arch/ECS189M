#!/usr/bin/python3
'''
Script to parse challenges in the `challenges` directory and outputs configuration files.

Note: This script is meant to be run internally, by me (rk). Therefore, I didn't bother with any input sanitizing.
Don't run this on challenge sources people give you unless you want your system borked!

The script makes a `build` directory, where it puts:
  mellivora.sql:    A list of SQL commands for the mellivora database, to populate the challenges on the scoreboard
  xinetd/xinetd.d:  List of xinetd configurations
  xinetd/src:       The directory to be mounted in the xinetd container as /challenges
  And more! I won't worry too much about it from the start. I'll make something that works first.
'''

import os
import sys
import yaml
import shutil
import datetime

XINETD_CONF_BASE="""service {0}
{{
	id = {0}
	type = UNLISTED
	disable = no
	socket_type = stream
	protocol = tcp
	wait = no
	user = root
	server = /usr/sbin/chroot
	server_args = --userspec=user:user /challenges/{0} {1}
	port = {2}
	bind = 0.0.0.0
}}
"""

def main():
    mellivora_sql=""

    os.chdir(os.path.dirname(__file__))
    if os.path.exists("build"):
        if("--destroy-old-build" not in sys.argv):
            print("WARNING! THE BUILD FOLDER EXISTS.")
            i=input("Are you sure you want to remove the previous build and start over? ")
            if(i.lower() not in ['y','yes']):
                exit(0)
        shutil.rmtree("build")
    os.mkdir("build")
    os.mkdir("build/xinetd")
    os.mkdir("build/xinetd/src")
    os.mkdir("build/xinetd/xinetd.d")

    with open("challenges/categories.yml") as f:
        y=yaml.safe_load(f)
        categories=y['categories']
    mellivora_sql,category_mapping=categories_to_sql(categories)


    for category in categories:
        for challenge in os.listdir("challenges/%s"%category):
            print("Processing %s/%s..."%(category,challenge))
            with open("challenges/%s/%s/info.yml"%(category,challenge)) as f:
                y=yaml.safe_load(f)
                mellivora_sql+=challenge_to_sql(y,category_mapping[category])

                if y['type']=="misc":
                    pass
                elif y['type']=="xinetd":
                    with open("build/xinetd/xinetd.d/%s"%challenge,"w") as wf:
                        wf.write(XINETD_CONF_BASE.format(challenge,y['xinetd_config']['executable'],y['xinetd_config']['port']))
                    shutil.copytree("xinetd_base/%s"%y['xinetd_config']['base'],"build/xinetd/src/%s"%challenge,symlinks=True)
                    shutil.copytree("challenges/%s/%s/dist"%(category,challenge),"build/xinetd/src/%s"%challenge,dirs_exist_ok=True)
                    with open("build/xinetd/src/%s/flag"%challenge,"w") as wf:
                        wf.write(y['flag']+"\n")
                #TODO: add more types, like webapps, ssh-able challenges, and downloadable ones


    with open("build/mellivora.sql","w") as f:
        f.write(mellivora_sql)
    print("Done!")

def categories_to_sql(config):
    sql="INSERT INTO `categories` VALUES \n"
    category_mapping={}
    id=1
    for c in config:
        sql+="(%d,%d,%d,'%s','%s',1,%d,%d)\n"%(
                 id, #id
                 int(datetime.datetime.now().timestamp()), #creation time
                 1, #creator (uid=1, the admin)
                 config[c]['name'], #category name
                 "", #category description, left blank for now
                 int(datetime.datetime.fromisoformat(config[c]['start']).timestamp()), #start time
                 int(datetime.datetime.fromisoformat(config[c]['end']).timestamp())) #end time
        if c in category_mapping:
            raise Exception("duplicate category %s"%c)
        category_mapping[c]=id
        id+=1
    return sql+';',category_mapping

def challenge_to_sql(config,category_id):
    #TODO: bleh
    #might need to change function signature as well cuz available_from to available_to, and autoincrement id
    return ""

if __name__=="__main__":
     main()
