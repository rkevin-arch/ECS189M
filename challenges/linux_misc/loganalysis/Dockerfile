FROM debian:latest
RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y install --no-install-recommends \
    tmux screen nano vim procps man-db less

RUN useradd -s /bin/bash -m -u 1337 user && \
chown -R root:root /home/user

COPY dist/* /usr/local/bin/
COPY README access.log auth.log flags.txt /home/user/

RUN chmod 111 /usr/local/bin/answer

RUN mkdir /tmp/qaframework && \
chown root:user /tmp/qaframework && \
chmod 730 /tmp/qaframework
USER user
ENTRYPOINT ["/bin/bash"]
WORKDIR "/home/user/"
