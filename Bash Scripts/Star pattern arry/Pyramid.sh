#!/bin/bash
line=1
colum=1
min=1
base=16
let middle=base/2+1
middle1=$middle
middle2=$middle

function pyramid () {
while [ $line -le $middle ]
do
    while [ $colum -le $middle2 ]
    do
        if [ $colum -ge $middle1 ]
        then
            echo -n "*"
        else
            echo -n " "
        fi
        let colum++
    done
    echo
    colum=1
    let middle2++
    let middle1--
    let line++
done
}
pyramid