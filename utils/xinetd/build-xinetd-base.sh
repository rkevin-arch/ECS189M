#!/bin/bash -xe

UTILS="cat bash base64 whoami uname echo more hostname touch pwd true false ls sha1sum id md5sum sha256sum sha512sum"
CONTAINER=`docker run --rm -d --entrypoint /bin/sleep xinetd:latest 10000`

# copy a binary and its library files
copybin() {
    u=$1
    docker cp -L $CONTAINER:$(docker exec $CONTAINER which $u) $TARGET/bin/
    for l in `docker exec $CONTAINER sh -c 'ldd $(which '$u')'`; do
        if echo $l | grep '^/lib' >/dev/null; then
            mkdir -p $TARGET$(dirname $l)
            docker cp -L $CONTAINER:$l $TARGET$l
        fi
    done
}

# binary environment
TARGET=../../xinetd_base/binary
rm -rf $TARGET
mkdir $TARGET

mkdir $TARGET/bin
for u in cat bash base64 whoami uname echo more hostname touch pwd true false ls sha1sum id md5sum sha256sum sha512sum; do
    copybin $u
done
cp ../noaslr/noaslr $TARGET/bin/
ln -s bash $TARGET/bin/sh

docker cp $CONTAINER:/lib/terminfo $TARGET/lib/terminfo
docker cp -L $CONTAINER:/lib/ld-linux.so.2 $TARGET/lib/
mkdir $TARGET/lib32
docker cp -L $CONTAINER:/lib32/libc.so.6 $TARGET/lib32/
mkdir $TARGET/etc

cat <<EOF >$TARGET/etc/group
root:x:0:
user:x:1337:
admin:x:1338:
EOF

cat <<EOF >$TARGET/etc/passwd
root:x:0:0:root:/:/bin/bash
user:x:1337:1337::/:/bin/bash
admin:x:1338:1338::/:/bin/bash
EOF

# python environment
TARGET=../../xinetd_base/python
rm -rf $TARGET
cp -Plr ../../xinetd_base/binary $TARGET

copybin python3
mkdir -p $TARGET/usr/lib/
docker cp $CONTAINER:/usr/lib/python3.7 $TARGET/usr/lib/
mkdir $TARGET/usr/lib/python3.7/dist-packages/
docker cp $CONTAINER:/usr/lib/python3/dist-packages/cryptography $TARGET/usr/lib/python3.7/dist-packages/
docker cp $CONTAINER:/usr/local/lib/python3.7/dist-packages/timeout_decorator $TARGET/usr/lib/python3.7/dist-packages/

docker stop $CONTAINER
