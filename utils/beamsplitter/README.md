# Beamsplitter

This is a Python server that allows unprivileged processes to control the creation of Docker containers. It's solely intended for ECS189 purposes, especially for the LFI challenges.

## Usage

I'm too lazy, so the server.py will just be run in tmux rather than as an actual systemd daemon. The clients will communicate using `/var/run/beamsplitter.sock` and send requests for the server to fulfill.

For installation instructions, you can consult `apache_rules`, which is a list of Apache configuration files being run on twinpeaks. Feel free to take it and modify it to suit your purposes.

In addition, please copy the `start.php` somewhere on the scoreboard, so it can talk to beamsplitter and request spinning up of challenge containers. Also, copy `client.py` into somewhere Apache can read, so Apache can use it to query where to reverse proxy.

After all that, change the whitelist and production mode of `beamsplitter.py`, and run it as root or some other user with Docker privileges.

## Protocol

The server listens on the socket `/var/run/beamsplitter.sock`. When someone visits the webserver's `/webchal/start/challenge`, the PHP script sends a request through the socket as `Cchallenge`, C stands for create. The server will attempt to create a docker container for that challenge, and return the string `Scookie`, S meaning success and the cookie should be set for the client as `beamsplitter_challenge=cookie`. If the server returns `F`, that means the requested service is not in the whitelist, or something else has gone wrong.

After that, whenever the webserver gets a request for the right virtual host, the webserver invokes the client (client.py) and asks it for the real port to reverse proxy to. The client sends a request in the following form: `Rip_challenge_cookies`, R stands for request, `ip` is the remote IP, `challenge` is the challenge name, and then a list of all cookies. The server checks the cookie named `beamsplitter_challenge`, where challenge is the name for that particular challenge, and tries to match it with the list of docker containers created. If one of them match, the server sends back the right address to reverse proxy to, like "http://localhost:40001" if that instance runs on port 40001. On error it returns a URL to an error page.
