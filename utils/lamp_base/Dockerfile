FROM debian:latest

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install --no-install-recommends \
    apache2 mariadb-server php libapache2-mod-php php-mysql

COPY src/* /var/www/html
COPY start.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh && rm /var/www/html/index.html
CMD /docker-entrypoint.sh

