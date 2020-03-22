FROM php:7-apache

COPY index.php /var/www/html/
RUN usermod -c '<span class="flag">ECS{P33K4800_B2618A84076474EA954D45580305D15D}</span>' www-data

COPY sonnets/ /var/www/sonnets/

RUN sed -i 's/Listen 80/Listen 8080/' /etc/apache2/ports.conf && \
sed -i 's/VirtualHost \*:80/VirtualHost *:8080/' /etc/apache2/sites-available/000-default.conf
RUN ln -snf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime && dpkg-reconfigure -f noninteractive tzdata
