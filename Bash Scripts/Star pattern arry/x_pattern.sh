#!/bin/bash
size=$1
upper=0
lower=$size-1
left=0
right=$size-1
row=0
col=0
# ##############################################################################################
function x_array () {
while [[ $row -lt $size ]]
do
    col=0
    while [[ $col -lt $size ]]
    do
    if [[ $col -eq $left || $col -eq $right || $row -eq $upper || $row -eq $right || $row -eq $col || $row+$col -eq $size-1 ]]
    then
    echo -n "* "
    else
    echo -n "  "
    fi
    ((col ++))
    done
    ((row ++))
echo
done
}
x_array
# ##############################################################################################