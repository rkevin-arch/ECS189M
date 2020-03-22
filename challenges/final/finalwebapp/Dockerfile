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
    description TEXT NOT NULL,\
    id TEXT NOT NULL\
);\
CREATE TABLE top_secret_plans (\
    title TEXT NOT NULL,\
    description TEXT NOT NULL,\
    id TEXT NOT NULL\
);\
INSERT INTO users (username, password) VALUES\
('operator','9b1ae9f537049de6b73655d5b2da36cd'),\
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
INSERT INTO plans_awaiting_approval(title, description, id) VALUES\
('Buy every property in the world above its 39th floor',\
'We can melt the polar ice caps using the Hubble Space Telescope, and the survivors will be forced to live in our property from now on till the end of time!',\
'dfba87e7e2db8ecf564ac6b54625b53c7390dcfcacf956881ec5f9dd036cd94c'),\
('Create a Frindolian Misoleevian Theta-Combobulator that uses sigma-infused ᾳ-cartridges',\
'As title. I can explain more if you have concerns about the higher homomorphism of Moussorgski particles affecting the Turgenev-Preobrazhensky zero-point adjustment module, but it should work.',\
'9b0db7b91d20a086fcf862a5bbd4b818a0186404249da6f9b819a501804f66ab'),\
('Recruit someone to become become famous children\\'s TV performers',\
'Afterwards, we can cryogenically freeze them for 40 years. When they’re thawed out, their fans will have grown up into the new world leaders, and they will be worshiped. This plan is airtight!',\
'2ad0a59ee8573d109d8d2c47b559ac95777ac0ee489aac9cb049bb2d8756498c'),\
('Realign Cartesian Mandrels',\
'This should boost our syllogism twine strength by 300% and nearly double the throughput of our Dejigamaflipper.',\
'789e7931b65a17f956e9dd5910a247dc19c1a31c70ff798fe9bc4fb7e62c3b0d');\
INSERT INTO top_secret_plans(title, description, id) VALUES\
('Waste everyone''s time',\
'We can pose as John, claim his homework is due, and ask everyone to do his homework for him! This will gain everyone''s pity and waste everyone''s time, especially those who remember the horrors of homework. Everyone will be so busy no one will see us coming!',\
'16d45adc67af743cbf4ddcb1df7cc558d78105840271f63f4db5c5fa368ef17d'),\
('Threaten to bomb major cities',\
'Through my contacts, I have sourced an intercontinental ballistic missile. We can hold a US city for ransom, and if they don''t give us money... Poof! The missile should be ready to launch at 10:00PM on Mar 20th. The missile interface can be viewed by connecting to photon.rkevin.dev port 30016, and the launch codes for the missile is ECS{L4T3_T0_TH3_P4RTY_4C50E5F2291EF75D31BFE234253BE43E}.',\
'ef5bcc8e62ccfae1eb06bba3b50eaad369ee3283aba911792169e21d555551cc');\
UPDATE mysql.user SET Password=PASSWORD('5473c338cab16ab860c51a83d9e34c43') WHERE User='root';\
DELETE FROM mysql.user WHERE User='';\
DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');\
DROP DATABASE IF EXISTS test;\
DELETE FROM mysql.db WHERE Db='test' OR Db='test\\\\_%';\
CREATE USER db_user@'%' IDENTIFIED BY '1b93b39ccc87a8495ded6410752acc6c';\
GRANT ALL PRIVILEGES ON redshift_plan_tracker.* TO db_user@'%';\
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
