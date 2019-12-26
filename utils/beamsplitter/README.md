# Beamsplitter

This is a Python server that allows unprivileged processes to control the creation of Docker containers. It's solely intended for ECS189 purposes, especially for the LFI and challenges.

## Usage

I'm too lazy, so the server.py will just be run in tmux rather than as an actual systemd daemon. The clients will communicate using /var/run/beamsplitter.sock and send requests for the server to fulfill.

## Protocol

The server listens on the socket /var/run/beamsplitter.sock. When someone visits the webserver's /webchal/start/challenge, the PHP script sends a request through the socket as "Cchallenge", C stands for create. The server will attempt to create a docker container for that challenge, and return the string "Scookie", S meaning success and the cookie should be set for the client as beamsplitter_challenge=cookie. If the server returns "F", that means the requested service is not in the whitelist.

After that, whenever the webserver gets a request for /webchal/challenge/*, the webserver invokes the client and asks it for the real port to reverse proxy to. The client sends a request in the following form: "Rchallenge_cookies", R stands for request, challenge is the challenge name, and a list of all cookies. The server checks the cookie named beamsplitter_challenge, where challenge is the name for that particular challenge, and tries to match it with the list of docker containers created. If one of them match, the server sends back the right address to reverse proxy to, like "http://localhost:40001" if that instance runs on port 40001. On error it returns a URL to an error page.

