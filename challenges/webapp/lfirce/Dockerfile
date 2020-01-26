FROM php:7.3.0RC4-apache-stretch

COPY index.php /var/www/html/
RUN usermod -c ECS{P33K4800_B2618A84076474EA954D45580305D15D} www-data

COPY sonnets/ /var/www/sonnets/
RUN rm /var/log/apache2/access.log && touch /var/log/apache2/access.log

RUN sed -i 's/Listen 80/Listen 8080/' /etc/apache2/ports.conf && \
sed -i 's/VirtualHost \*:80/VirtualHost *:8080/' /etc/apache2/sites-available/000-default.conf
RUN ln -snf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime && dpkg-reconfigure -f noninteractive tzdata
