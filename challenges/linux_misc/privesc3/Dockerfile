FROM debian:latest
RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y install --no-install-recommends \
    tmux screen nano vim procps less

RUN useradd -s /bin/bash -m -u 1337 user && \
useradd -s /bin/bash -m -u 1338 admin && \
useradd -s /bin/false -m -u 1339 wendi && \
echo admin:anchored53Leach94Isolated | chpasswd

COPY flag /home/admin/
COPY dist/sync_wrapper /home/wendi
COPY dist/init /usr/local/bin/init

RUN chown admin:admin /home/admin/flag && \
chmod 440 /home/admin/flag && \
chown wendi:wendi /home/wendi/sync_wrapper && \
chmod 700 /home/wendi/sync_wrapper && \
chmod 700 /usr/local/bin/init

USER root:1337
ENTRYPOINT ["/usr/local/bin/init"]
WORKDIR "/home/user/"
