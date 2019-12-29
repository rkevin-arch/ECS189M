#!/usr/bin/env python3
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
	nice = 10
	rlimit_as = 64M
	rlimit_cpu = 20
}}
"""

SSH_SUID_CLIENT_BASE="""#include <stdio.h>
#include <unistd.h>
int main(){{
    alarm(21600); //6 hours
    puts("Setting up challenge environment for {0}, please wait...");
    fflush(stdout);
    char *argv[]={{"docker", "run", "--memory=64m", "--memory-swap=128m", "--cpus=.25", "--rm", "-it", "{0}", NULL}};
    execve("/usr/bin/docker", argv, NULL);
    puts("Something has gone wrong, please contact rk!");
    fflush(stdout);
    return 1;
}}

"""

def version_check():
    """ Validate Python version supports modules """

    # datetime.date.isoformat() is not present below Python 3.7
    if sys.version_info < (3, 7):
        print("Please install Python 3.7 or above.")
        sys.exit(1)

def main():

    version_check()
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
    os.mkdir("build/sshable")

    with open("challenges/categories.yml") as f:
        y=yaml.safe_load(f)
        categories=y['categories']
    mellivora_sql,category_mapping=categories_to_sql(categories)
    mellivora_sql="DELETE FROM categories; DELETE FROM challenges;\n"+mellivora_sql

    challenges={}

    for category in categories:

        # Report and Fail gracefully if category doesn't exist on disk
        try:
            listdir = os.listdir("challenges/%s" % category)
        except FileNotFoundError as e:
            print("Skipping (%s). Not found" % category, e)
            continue

        for challenge in listdir:
            print("Processing %s/%s..."%(category,challenge))
            if challenge in challenges:
                raise Exception("Challenge is a duplicate!")
            with open("challenges/%s/%s/info.yml"%(category,challenge)) as f:
                y=yaml.safe_load(f)

                #process prebuild script
                if 'prebuild' in y:
                    os.chdir("challenges/%s/%s"%(category,challenge))
                    if os.system(y['prebuild']):
                        raise Exception("Prebuild script failed!")
                    os.chdir("../../..")

                if y['type']=="misc":
                    pass
                elif y['type']=="xinetd":
                    with open("build/xinetd/xinetd.d/%s"%challenge,"w") as wf:
                        wf.write(XINETD_CONF_BASE.format(challenge,y['xinetd_config']['executable'],y['xinetd_config']['port']))
                    shutil.copytree("xinetd_base/%s"%y['xinetd_config']['base'],"build/xinetd/src/%s"%challenge,symlinks=True)
                    shutil.copytree("challenges/%s/%s/dist"%(category,challenge),"build/xinetd/src/%s"%challenge,dirs_exist_ok=True)
                    with open("build/xinetd/src/%s/flag"%challenge,"w") as wf:
                        wf.write(y['flag']+"\n")
                elif y['type']=="sshable":
                    os.chdir("challenges/%s/%s"%(category,challenge))
                    if os.system("docker build -t %s ."%challenge):
                        raise Exception("Building docker container failed!")
                    os.chdir("../../..")
                    with open("build/sshable/%s_client.c"%challenge,"w") as wf:
                        wf.write(SSH_SUID_CLIENT_BASE.format(challenge))
                    if os.system("gcc build/sshable/%s_client.c -o build/sshable/%s_client"%(challenge,challenge)):
                        raise Exception("Compiling the SUID client went horribly wrong!")
                    #TODO: make a script that creates all the right users and copies the %s_clients to the right place and makes it suid?
                else:
                    raise Exception("Unrecognized challenge type %s!"%y['type'])

                y['category']=category
                challenges[challenge]=y


    mellivora_sql+=challenges_to_sql(challenges,categories,category_mapping)
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
                curtimestamp(), #creation time
                1, #creator (uid=1, the admin)
                config[c]['name'], #category name
                "", #category description, left blank for now
                iso2timestamp(config[c]['start']), #start time
                iso2timestamp(config[c]['end'])) #end time
        if c in category_mapping:
            raise Exception("duplicate category %s"%c)
        category_mapping[c]=id
        id+=1
    return sql+';\n\n',category_mapping

def challenges_to_sql(challenges, categories, category_mapping):
    sql="INSERT INTO `challenges` VALUES \n"
    id=1
    for challenge in challenges:
        c=challenges[challenge]
        sql+="(%d,%d,%d,'%s',%d,'%s',%d,%d,%d,'%s',%d,%d,%d,%d,%d,%d)"%(
                id, #id
                int(datetime.datetime.now().timestamp()), #creation time
                1, #added by (uid=1)
                c['title'], #title
                category_mapping[c['category']], #category (id)
                c['description'], #description
                1, #exposed
                iso2timestamp(categories[c['category']]['start']), #start time
                iso2timestamp(categories[c['category']]['end']), #end time
                c['flag'], #flag
                0, #case insensitive? no
                1, #automark
                c['points'], #points
                0, #num attempts allowed? unlimited
                0, #min seconds between submissions? 0
                0) #doesnt rely on another challenge
        id+=1
    return sql+';\n'

def iso2timestamp(s):
    return int(datetime.datetime.fromisoformat(s).timestamp())

def curtimestamp():
    return int(datetime.datetime.now().timestamp())

if __name__=="__main__":
     main()
