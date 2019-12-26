#!/bin/bash
set -e
if [ $# -ne 3 ]; then
    echo "Usage: $0 python_file output_directory"
    echo "Uses nuitka to build python_file into a standalone binary,"
    echo "then copies everything over to output_directory."
    exit
fi
if [ ! -d $2 ]; then
    mkdir -p $2
fi
tmp=`mktemp`
python3 -m nuitka --python-flag=no_site --standalone $tmp $1
mv $tmp/*.dist/* $2
rm -rf $tmp
