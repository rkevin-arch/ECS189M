FROM debian:latest
RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y install --no-install-recommends \
    tmux screen nano vim procps sudo less

RUN useradd -s /bin/bash -m -u 1337 user && \
useradd -s /bin/bash -m -u 1338 admin

COPY flag /home/admin
RUN chown admin:admin /home/admin/flag && \
chmod 440 /home/admin/flag && \
echo "user ALL=(admin) NOPASSWD: ALL" >> /etc/sudoers

RUN ln -snf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime && dpkg-reconfigure -f noninteractive tzdata

USER user
ENTRYPOINT ["/bin/bash"]
WORKDIR "/home/user/"
