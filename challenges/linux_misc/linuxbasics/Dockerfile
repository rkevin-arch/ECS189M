FROM debian:latest
RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y install --no-install-recommends \
    tmux screen nano vim gcc procps man-db libc6-dev less file && \
  apt clean

RUN useradd -s /bin/false -d / -u 1338 admin && \
useradd -s /bin/bash -m -u 1337 -G admin user && \
useradd -s /bin/false -d / -u 1001 -G admin      john && \
useradd -s /bin/false -d / -u 1002               dave && \
useradd -s /bin/false -d / -u 1003 -G user,admin rose && \
useradd -s /bin/false -d / -u 1004 -G user       jade && \
chown -R root:root /home/user

COPY dist/* /usr/local/bin/
COPY README /home/user/README
COPY myfile.txt /home/user

RUN chmod 111 /usr/local/bin/answer && \
chown root:admin /home/user/myfile.txt && \
chmod 754 /home/user/myfile.txt && \
touch -d $(date -d "2009-04-13 + `shuf -i0-3800 -n1` days" +'%Y-%m-%d') /home/user/myfile.txt && \
touch /home/user/chme && \
chown user:admin /home/user/chme

RUN mkdir /tmp/qaframework && \
chown root:user /tmp/qaframework && \
chmod 730 /tmp/qaframework

RUN ln -snf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime && dpkg-reconfigure -f noninteractive tzdata

USER user
ENTRYPOINT ["/bin/bash"]
WORKDIR "/home/user/"
