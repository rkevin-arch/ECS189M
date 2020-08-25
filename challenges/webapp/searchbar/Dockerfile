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
CREATE TABLE inventory (\
    item varchar(255) NOT NULL,\
    count INT NOT NULL\
);\
CREATE TABLE heyo_flag_here (\
    flag varchar(255) NOT NULL\
);\
INSERT INTO inventory (item,count) VALUES\
('AA Batteries',5),\
('100 Ohm resistors',70),\
('1 microfarad capacitors',30),\
('1 millihenry inductors',15),\
('Function generators',2),\
('Oscilloscopes',1),\
('Multimeters',4),\
('Lost hopes and dreams',1),\
('Some random homework assignments',1);\
INSERT INTO heyo_flag_here (flag) VALUES\
('ECS{50_TH4T5_WH3R3_MY_LUNCH_W3NT_D0E277745D6760E9B6FB2DEE6FAFA029}');" |mysql &&\
service mysql stop

RUN sed -i 's/Listen 80/Listen 8080/' /etc/apache2/ports.conf && \
sed -i 's/VirtualHost \*:80/VirtualHost *:8080/' /etc/apache2/sites-available/000-default.conf

RUN ln -snf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime && dpkg-reconfigure -f noninteractive tzdata
