FROM debian:latest
RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y install --no-install-recommends \
    tmux screen nano vim procps sudo less curl wget cron && \
  apt clean

RUN useradd -s /bin/bash -m -u 1337 user && \
groupmod -g 1338 operator && \
useradd -s /bin/bash -m -u 1338 -g 1338 operator && \
useradd -s /bin/bash -m -u 1339 admin && \
useradd -s /bin/bash -m -u 1340 system

# User to operator
COPY --chown=1338:1338 todolist .viminfo part_1_message /home/operator/
RUN echo operator:cathedralremovedsubsidizeshorteryin | chpasswd && \
    chmod 400 /home/operator/part_1_message

# Operator to admin
RUN echo "operator ALL=(admin) NOPASSWD: /bin/nano" >> /etc/sudoers && \
    echo "operator ALL=(admin) NOPASSWD: /usr/bin/vim" >> /etc/sudoers
COPY --chown=1339:1339 part_2_message /home/admin
RUN chmod 400 /home/admin/part_2_message


# Admin to system
COPY --chown=1340:1340 top_secret_information_and_flag networkstatus /home/system/
COPY --chown=1339:1339 network_connectivity_test.sh /home/admin/
RUN chmod 400 /home/system/top_secret_information_and_flag && \
    mkdir /backup && chown system:system /backup && \
    echo "* * * * * system /home/admin/network_connectivity_test.sh" >> /etc/crontab

RUN rm /etc/cron.daily/*
COPY dist/init /usr/local/bin/
RUN ln -snf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime && dpkg-reconfigure -f noninteractive tzdata
ENV HOME /home/user
USER root:1337
ENTRYPOINT ["/usr/local/bin/init"]
WORKDIR "/home/user/"
