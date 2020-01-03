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

RUN ln -snf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime && dpkg-reconfigure -f noninteractive tzdata

USER user
ENTRYPOINT ["/bin/bash"]
WORKDIR "/home/user/"
