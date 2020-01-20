FROM debian:latest
RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y install --no-install-recommends \
    python3-bottle

RUN useradd -s /bin/bash -m -u 1340 web

COPY app.py /home/web/

RUN ln -snf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime && dpkg-reconfigure -f noninteractive tzdata

USER web
ENTRYPOINT ["/usr/bin/python3.7","/home/web/app.py"]
