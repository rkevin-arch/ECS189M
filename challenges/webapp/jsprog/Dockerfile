FROM debian:latest
RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y install --no-install-recommends \
    python3-bottle curl bzip2 fontconfig ca-certificates python3-paste

RUN curl -Ls https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 | \
tar -jx phantomjs-2.1.1-linux-x86_64/bin/phantomjs -O > /usr/bin/phantomjs && chmod +x /usr/bin/phantomjs

RUN useradd -s /bin/bash -m -u 1340 web

COPY app.py /home/web/
COPY templates /home/web/templates/
COPY load_page.js /home/web/

RUN ln -snf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime && dpkg-reconfigure -f noninteractive tzdata

ENV OPENSSL_CONF=/etc/openssl.cnf
USER web
ENTRYPOINT ["/usr/bin/python3.7", "/home/web/app.py"]

WORKDIR /home/web
