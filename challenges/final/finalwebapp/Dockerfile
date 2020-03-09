FROM debian:latest
RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y install --no-install-recommends \
    python3-bottle curl bzip2 fontconfig ca-certificates \
    mariadb-server python3-pip && \
  pip3 install mysql-connector-python

RUN curl -Ls https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 | \
tar -jx phantomjs-2.1.1-linux-x86_64/bin/phantomjs -O > /usr/bin/phantomjs && chmod +x /usr/bin/phantomjs

RUN useradd -s /bin/bash -m -u 1340 web

# unfortunately have to use mysql, since i only taught the students how to use information_schema
RUN service mysql start && echo "\
CREATE DATABASE IF NOT EXISTS redshift_plan_tracker;\
USE redshift_plan_tracker;\
CREATE TABLE users (\
    username TEXT NOT NULL,\
    password TEXT NOT NULL\
);\
CREATE TABLE plans_awaiting_approval (\
    title TEXT NOT NULL,\
    description TEXT NOT NULL\
);\
CREATE TABLE top_secret_plans (\
    title TEXT NOT NULL,\
    description TEXT NOT NULL\
);\
INSERT INTO users (username, password) VALUES\
('operator','9b1ae9f537049de6b73655d5b2da36cd'),\
('asriel_dreemurr','be7ef042f4e811e370c48b7c447ae479'),\
('carlton_houpt','d00d7a5a043f23b6e77d6be2f8bb5a25'),\
('dave_strider','c1d85b1162c660b1c38bd539d010ebbd'),\
('donte_dona','633fde0bf732ea689aa4c278bbcd2ffc'),\
('finn_mertens','97a2c322760ab4da18c9507f83817437'),\
('florentina_marcil','a6b071637ae11479c82ed8bdc2e0c329'),\
('georgene_whiteford','fecc8cb9ab231acca8289fe6aa2682af'),\
('gwenn_tamura','cbede9fffd0f31c968d658844261ec21'),\
('heidi_leff','18e0526af09a136abdd180ea6b7d006f'),\
('ione_ballard','fb38ae50c92509f2e378cb226ecba8cf'),\
('jade_harley','173065ce03d5291607240498abcb6f90'),\
('janella_muller','03b954f0e243eca25458406ea9c4fdb6'),\
('jennifer_lariviere','776b08e9c6d1c9771789e29cdf72285c'),\
('john_doe','da6dd0ee0e3a217cde4f8923cc0c4cda'),\
('john_egbert','686914c0b8f901eb64283afc5441cfe2'),\
('karena_cornelison','3c44d680d0b0bfc2a579b1e4850ef055'),\
('karima_cupp','bfab1c1f43587f28efa6a161aecc97b7'),\
('karkat_vantas','a73c829adaf54787b033a882819cfef7'),\
('kathie_rodney','060a5037b624ece3d348314169bdde29'),\
('kelly_quon','95c4d1caf340fc2d0023c5b176561f18'),\
('kevin_mitnick','3e7774cbeea06e8887ddeeca74d6cb6a'),\
('lucretia_basel','5b0516a3e6331b8dc548c998e70ac0cc'),\
('micki_regis','ab26f992a203aca39773fbae096d60fe'),\
('monty_jantzen','8987ecdcf7ec32154cefb7da96766fe4'),\
('regenia_evenson','0cb0c12cd596e1ea3fa5d7dd172d9046'),\
('rose_lalonde','10667ea9387fd71bb6190a796d6fe3bb'),\
('sebastian_laviolette','a6148e80c441ef26dd876eb92fab0928'),\
('tamera_winchester','0f5c3d10d6d91d929b5ca36211ec2705'),\
('velma_farquharson','a6828830e020da9db3a5eee568dcc5cd');\
INSERT INTO plans_awaiting_approval(title, description) VALUES\
('testtitle', 'testdesc'),\
('testtitle2', 'testdesc2');\
INSERT INTO top_secret_plans(title, description) VALUES\
('bleh', 'ECS{fakeflag}');\
UPDATE mysql.user SET Password=PASSWORD('1b93b39ccc87a8495ded6410752acc6c') WHERE User='root';\
DELETE FROM mysql.user WHERE User='';\
DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');\
DROP DATABASE IF EXISTS test;\
DELETE FROM mysql.db WHERE Db='test' OR Db='test\\\\_%';\
FLUSH PRIVILEGES;" |mysql && \
sleep 1 && service mysql stop

RUN ln -snf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime && dpkg-reconfigure -f noninteractive tzdata

ENV OPENSSL_CONF=/etc/openssl.cnf
USER root:1340
COPY entrypoint.py /home/web/
ENTRYPOINT ["/home/web/entrypoint.py"]

WORKDIR /home/web

COPY app.py /home/web/
COPY static /home/web/static/
COPY templates /home/web/templates/
COPY load_page.js /home/web/
