FROM debian:latest
RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y install --no-install-recommends \
    tmux screen nano vim procps cron less curl wget && \
  apt clean

RUN useradd -s /bin/bash -m -u 1337 user && \
useradd -s /bin/bash -m -u 1338 admin

COPY flag maintenance.sh /home/admin/
RUN chown admin:admin /home/admin/flag /home/admin/maintenance.sh && \
chmod 440 /home/admin/flag && chmod 755 /home/admin/maintenance.sh

RUN echo "* * * * * admin /home/admin/maintenance.sh" >> /etc/crontab
RUN mkdir /tmp/.admin.maintenance && chmod 777 /tmp/.admin.maintenance

COPY dist/init /usr/local/bin/
RUN chmod 755 /usr/local/bin/init

#RUN chown root:admin /var/run && chmod 775 /var/run
RUN rm /etc/cron.daily/*


RUN ln -snf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime && dpkg-reconfigure -f noninteractive tzdata

ENV HOME /home/user
USER root:1337
ENTRYPOINT ["/usr/local/bin/init"]
WORKDIR "/home/user"
