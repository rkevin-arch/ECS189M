FROM debian:latest
RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y install --no-install-recommends \
    tmux screen nano vim procps less netcat-openbsd xinetd

RUN useradd -s /bin/bash -m -u 1337 user && \
useradd -s /bin/bash -m -u 1338 admin

COPY flag /home/admin/
COPY xinetd.conf /etc/
COPY dist/* /usr/local/bin/

RUN chown admin:admin /home/admin/flag && \
chmod 440 /home/admin/flag && \
chmod 711 /usr/local/bin/nchandler && \
chmod 700 /usr/local/bin/init

USER root:1337
ENTRYPOINT ["/usr/local/bin/init"]
WORKDIR "/home/user/"
