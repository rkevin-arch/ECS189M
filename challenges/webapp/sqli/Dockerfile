FROM debian:latest
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install --no-install-recommends \
    apache2 mariadb-server php libapache2-mod-php php-mysql && \
  apt clean

COPY db.php index.php /var/www/html/
COPY start.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh && rm /var/www/html/index.html
CMD /docker-entrypoint.sh

RUN service mysql start && echo "\
CREATE DATABASE IF NOT EXISTS sqli;\
USE sqli;\
CREATE TABLE users (\
    username varchar(255) NOT NULL,\
    password varchar(255) NOT NULL\
);\
INSERT INTO users (username,password) VALUES\
('admin','im surprised you had the time to do this, do it on another challenge instead!');" |mysql &&\
service mysql stop

RUN sed -i 's/Listen 80/Listen 8080/' /etc/apache2/ports.conf && \
sed -i 's/VirtualHost \*:80/VirtualHost *:8080/' /etc/apache2/sites-available/000-default.conf

RUN ln -snf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime && dpkg-reconfigure -f noninteractive tzdata
