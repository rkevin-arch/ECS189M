#!/bin/bash
# Verify we have a network connection
if ping -c1 -W1 73.66.52.69; then
    echo "Network online." > /home/system/networkstatus
else
    # Internet down! Notify the sysadmin
    echo "Network offline!" > /home/system/networkstatus
fi
