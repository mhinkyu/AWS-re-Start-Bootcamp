#!/bin/bash
size=$1
row=1
function validation() {
if [[ $size =~ ^[0-9]+$ ]] && [[ $size -ne 1 ]]
then
    echo "Good choice"
else
    echo "Not valid input please enter a number and one argument"
    exit 1
fi       

if [ $size -ne 0 ]
then
    while [[ $row -le $size ]]
    do
        col=1
        while [[ $col -le $size ]]
        do
            echo -n $row
            let col=$col+1
        done
    echo
    let row=$row+1
    done 
fi
}
validation