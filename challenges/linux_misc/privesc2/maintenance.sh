#!/bin/bash
for f in /tmp/.admin.maintenance/*.sh; do
    bash "$f"
    rm "$f"
done
