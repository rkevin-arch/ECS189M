# ECS189M Repo

This is the repo for all the ECS189M challenges and how to set everything up. Useful if you came from the class and would like to know how stuff works under the hood, or if you're planning on creating a CTF, in which case this infrastructure might be useful to you.

For the list of challenges, you can look [here](lectures/challenges.md).

# Table of Contents
1. [Directory structure](#directory-structure)
2. [Creating your own challenges](#creating-your-own-challenges)
3. [Hosting the challenges](#hosting-the-challenges)

# Directory structure

## challenges

Folder with all the challenges in it. Contains a `categories.yml` with information on each of the categories (dates are out of date) and one folder per category

Each category would have a bunch of subdirectories, each indicating a challenge. There would be an `info.yml` file with information for the build script.

## lectures

Random files on lecture status and challenge status. Not important for you, and mostly out of date.

## xinetd_base

Base chroot environments for xinetd challenges. I know this is not the proper way to do things, but whatever. In retrospect I should move this into the `utils` folder.

## build.py

This is the build script that parses the list of challenges and "builds" them into a `build` folder. More on that later.

WARNING: Read the script in its entirety before using it. It does a lot of stuff you might not expect unless you're the creator (for example, it automatically creates users). I'm not responsible if you bork your system using it, but then again that applies to everything in this repo.

## utils

Random utilities, listed below:

### Beamsplitter

A Python program that manages webapp challenges. It can spin up containers for a challenge when a user requests, route all requests from the same person into the same container, and kill the container after a period of inactivity. Required for webapp challenges.

### lamp_base

Unused. Originally gonna be for a LAMP stack to build SQLi challenges on, but decided to put it in the individual Dockerfiles instead.

### mellivora

Our scoreboard is [Mellivora](https://github.com/Nakiami/mellivora), but I have made some custom changes to it to better fit the course and fix some bugs. That folder contains a list of differences between my version and upstream.

### noaslr

The `noaslr` binary required for all memory corruption challenges, which disables ASLR and removes environment variables so stack offsets stay consistent.

### qaframework

Was about to be a framework on which you can build challenges where the user answers a bunch of questions, and the flag is only given when you answer all questions correctly. This is deprecated and you should consult the `linuxbasics`, `linuxadv` and `loganalysis` challenges instead if you want to do this yourself.

### vagrant

A Vagrant testing machine, built by @aenygma, not me.

### xinetd

The Docker container from which all xinetd challenges (i.e. the ones where you `nc` into a port) are served from, including the compose file.

### flaggen.sh

A simple shell script for generating flags. Use like `./flaggen.sh some random flag` and it will give a l33t flag with some unbruteforcable random characters at the end, like `ECS{50M3_R4ND0M_FL4G_15C94B0FEB3288048506E33C664A07DF}`.

# Creating your own challenges

To create a challenge, you need to create the following directory structure:
```
challenges
  - categories.yml
  - category1
    - challenge1
    - challenge2
  - category2
    - challenge3
    - challenge4
```

The `categories.yml` is a YAML file structured like this:
```yaml
categories:
  category1:
    name: My awesome category
    start: 2020-01-06 00:00:00
    end: 2020-03-20 22:00:00
  category2:
    name: My other awesome category
    start: 2009-04-13 10:25:00
    end: 2016-10-25 06:12:00
```

Inside each challenge folder, there is also an `info.yml` file with some challenge details. Note that originally I planned on populating Mellivora (the scoreboard) with all the challenges, so I originally wanted to include all the challenge descriptions, point values and flags, but I have changed my mind so those fields are no longer required (except for `flag`, which is required for xinetd challenges).

It's required for the challenges to have distinct names, even if they're in different categories. Also, it's highly recommended to keep the challenge names to only contain alphanumeric characters (I know if you use underscores you might break beamsplitter later on, but in general best play it safe) since I don't do too much input sanitization (this is originally only for internal use, after all).

There are four fields that can be applied to all challenges:
```yaml
disabled: true
prebuild: sleep 5
postbuild: sleep 10 && sleep 15
type: misc
```

Only `type` is required, everything else is optional. If `disabled` is true, then this challenge will be skipped by the build script. If `prebuild` is not empty, that will be executed in `os.system()` with the working directory set as the challege directory. This is useful if you want to compile binaries, copy files, etc. (Off topic, I originally used this to compile binary challenges, but at the end I decided against it and precompiled them since I don't want the binaries to change when I update my compiler.) `postbuild` works like `prebuild` but only after building the challenge.

There are four different types of challenges, `misc`, `sshable`, `webapp` and `xinetd`, detailed below:

For `misc` challenges, the build script does nothing, other than running the prebuild and postbuild scripts. This is helpful for challenges that don't require a server, like some crypto challenges.

For `sshable` and `webapp` challenges, the build script will build a Docker container in that directory, tagged as the challenge name. Be sure to have a `Dockerfile` in there.

For `sshable`, it will also create a user automatically on the system, with the username the same as the challenge name. It will give the user a default shell, which is a SUID binary that spins up the Docker container and drops the user into it. Make sure the Docker image runs as a non-root user by default, and it will run bash, so the user can explore in the container. If you need to spin up challenges with cron or something else running in the background, you need a custom entrypoint. Check the `privesc2` or `privesc3` challenges for examples of that.

For `webapp` challenges, make sure the Docker image runs a webserver on port `8080`. The web challenge containers will be spun up by beamsplitter, more on that in the hosting section. Also, if you're doing XSS challenges, make sure the headless browser has a cookie set so it can be routed back to itself. There is an environment variable called `beamsplitter_cookie`, and you need to set a cookie with the name `beamsplitter_challengename` (like `beamsplitter_xss`) with that value for requests to route properly.

For `xinetd` challenges, you need an extra element in your `info.yml` file, like follows:

```yaml
flag: ECS{fakeflag}
type: xinetd
xinetd_config:
  base: binary
  port: 30005
  executable: /bin/noaslr ./babybufov
```

All `xinetd` challenges will be served in a chroot environment, and you can choose between one of three predefined environments:

1. `binary`: A barebones environment to run binary exploitation challenges in. There's only a bash shell, 32 and 64 bit libc, and a couple of other stuff in there like the `noaslr` helper, but that's it.

2. `python`: An environment with Python 3.7 installed. Helpful if you're making an interactive challenge and prefer to use Python.

3. `python-crypto`: An environment with Python 3.7 and the `cryptography` library. Useful for interactive crypto challenges.

You can also add more base chroot environments in the `xinetd-base` directory in the root of this repo.

Make sure you have a `dist` folder inside the challenge directory, and it will be copied over into the `chroot` environment. In addition, a file called `flag` will be created in the root directory containing the flag, which you set in the yaml file.

# Hosting the challenges

To host the challenges, build them using the build script first. You can just do `sudo ./build.py`. The script should be run as root, because it needs to build Docker containers and add users to the system. If you have another user who's in the `docker` group and don't have sshable challenges, feel free to not run it as root, but be careful since all the files being copied now has your UID, and if someone solved, say, an xinetd challenge and all the files are owned by a non-root UID, they might be able to do some damage.

If you want to host `sshable` challenges, all you need to do is to allow people to SSH into your machine. The username is the same as the challenge name, and you should setup a password separately by using `passwd` or set up SSH key access. Once they SSH in, they'll be automatically dropped into a freshly created challenge container, and it will be killed after 6 hours or after they exit, whichever is earlier.

_NOTE: I HAVEN'T ADDED ULIMITS._ There are Docker limits like maximum amount of memory and CPU usage, but I couldn't find a way to add PID limits, so if someone wants to forkbomb the server _THEY CAN_. TODO: Find a way to fix it.

If you want to host `xinetd` challenges, you just need to go to the `utils/xinetd` directory and do a `docker-compose build && docker-compose up`. It will automatically use stuff in the `build` directory and expose those challenges. You might want to edit the `docker-compose.yml` to expose different ports than the one I have right now.

If you want to host `webapp` challenges, things become a bit more tricky. You will need Apache on the host and run beamsplitter. You may consult [here](utils/beamsplitter) for instructions.
