# xinetd container

This is the xinetd container that hosts all the netcat challenges.

## Usage

Just `docker-compose build && docker-compose up`. You might also want `docker-compose up -d` to background the running container.

Put the challenges in `./src`, and put the xinetd configurations in `./xinetd.d`. Both will be mounted inside the container. You can generate both using the build script.


