#!/bin/bash 
# Script that checks if a process is running by PID and if it is not running, it will create a new file with Warning and number of PID
function PID() {
while [[ 1 -eq 1 ]];
do
    pross=`ps aux | awk '{print$2}' | grep ^$1$`
    if [[ $pross != $1 ]];then
        if [ -d "/Users/mhinkyu/Warning" ]; then 
            echo "Warning pid [$1] is Down" > /Users/mhinkyu/Warning/Warning:$1.txt
        else
            mkdir  ~/Warning
        fi
    fi
    sleep 5
done
}
PID