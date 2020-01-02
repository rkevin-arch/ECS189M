#!/bin/bash
msg=`echo $*|tr a-z A-Z|tr A 4|tr B 8|tr E 3|tr I 1|tr O 0|tr S 5|tr ' ' '_'`
uuid=`uuidgen|md5sum|cut -d ' ' -f 1|tr a-z A-Z`
echo "ECS{${msg}_${uuid}}"
