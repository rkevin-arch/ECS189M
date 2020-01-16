#!/bin/bash
pass=`dd if=/dev/urandom bs=16 count=1 status=none|sha1sum`
sed -i "s/password/$pass/" /var/www/html/db.php
service mysql start
mysql <<EOF
UPDATE mysql.user SET Password=PASSWORD("$pass"), plugin='' WHERE User='root';
DELETE FROM mysql.user WHERE User='';
DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');
DROP DATABASE IF EXISTS test;
DELETE FROM mysql.db WHERE Db='test' OR Db='test\\_%';
FLUSH PRIVILEGES;
EOF
. /etc/apache2/envvars
apache2 -DFOREGROUND #which hangs
