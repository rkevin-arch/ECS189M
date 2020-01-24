FROM php:7.3.0RC4-apache-stretch

COPY index.php /var/www/html/
COPY dist/execute_me_to_get_the_flag /
RUN chmod 111 /execute_me_to_get_the_flag

RUN sed -i 's/Listen 80/Listen 8080/' /etc/apache2/ports.conf && \
sed -i 's/VirtualHost \*:80/VirtualHost *:8080/' /etc/apache2/sites-available/000-default.conf
RUN ln -snf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime && dpkg-reconfigure -f noninteractive tzdata
