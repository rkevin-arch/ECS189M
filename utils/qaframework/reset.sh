#!/bin/bash
# Run as root to reset /tmp/qaframework, purely for rk's testing purposes
rm -rf /tmp/qaframework
mkdir /tmp/qaframework
chown root:rkevin /tmp/qaframework
chmod 630 /tmp/qaframework
