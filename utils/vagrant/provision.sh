#!/usr/bin/env bash

# Phase 1: install docker
sudo apt-get update
sudo apt-get -y install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

# add docker key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# add repo 
sudo add-apt-repository -y\
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

# update again
sudo apt-get update

# install
sudo apt-get -y install docker-ce docker-ce-cli containerd.io

# Phase 2: docker-compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose


# install python-3.8
sudo apt install -y software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt install -y python3.8
sudo apt-get install -y python3.8-dev

# set python3.8 as preferred
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8  1 
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8  1


#get pip
sudo apt-get -y install python3-distutils
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python get-pip.py


# get 32-bit headers - invtracker
sudo apt install -y gcc-multilib

#Phase 3: pip installs
sudo pip  install nuitka

#Phase 4: misc
sudo usermod -aG docker $USER

