FROM debian:latest
RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y install --no-install-recommends \
      tcpd \
      xinetd \
      python3 \
      python3-setuptools \
      python3-pip && \
  pip3 install timeout-decorator
ENTRYPOINT [ "xinetd", "-dontfork" ]
RUN useradd -s /bin/bash -d / -u 1337 user && \
useradd -s /bin/bash -d / -u 1338 admin

RUN ln -snf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime && dpkg-reconfigure -f noninteractive tzdata
