FROM debian:latest
RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y install --no-install-recommends \
    tmux screen nano vim gcc procps man-db libc6-dev less

RUN useradd -s /bin/bash -m -u 1337 user && \
chown -R root:root /home/user

COPY dist/* /usr/local/bin/
COPY spawner /usr/local/bin/
COPY README in.txt /home/user/

RUN chmod 111 /usr/local/bin/answer /usr/local/bin/correct /usr/local/bin/incorrect && \
chown -R root:root /home/user

RUN mkdir /tmp/qaframework && \
chown root:user /tmp/qaframework && \
chmod 730 /tmp/qaframework

RUN ln -snf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime && dpkg-reconfigure -f noninteractive tzdata

USER user
ENTRYPOINT ["/bin/bash"]
WORKDIR "/home/user/"
