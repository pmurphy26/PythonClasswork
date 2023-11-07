#!/bin/bash

# NOTE: This can take a long time to run (possibly a few minutes)

echo "      PID    PPID    PGID     WINPID   TTY         UID    STIME COMMAND"
for OUTPUT in $(netstat -ao | grep https | awk '{print $NF}' | sort | uniq)
do
    ps -W | awk -v var="$OUTPUT" '$4==var'
done