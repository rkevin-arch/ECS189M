FROM debian:latest
RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y install --no-install-recommends \
    tmux screen nano vim less

RUN useradd -s /bin/bash -m -u 1337 user && \
useradd -s /bin/false -d / -u 1338 admin

COPY src/* /home/user/
COPY dist/race /home/user

RUN chown root:admin /home/user/race && \
chown root:admin /home/user/flag && \
chmod 2755 /home/user/race && \
chmod 440 /home/user/flag

RUN ln -snf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime && dpkg-reconfigure -f noninteractive tzdata

USER user
ENTRYPOINT ["/bin/bash"]
WORKDIR "/home/user/"
