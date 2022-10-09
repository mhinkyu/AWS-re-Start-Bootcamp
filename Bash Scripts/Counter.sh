#!/bin/bash 
COUNTER=0

function get_number () {
  while [ $COUNTER -lt 2 ]; do
        echo The counter is $COUNTER
        read a b c
    if [ $a -eq $b -a $a -eq $c ]; then
        echo "All the three numbers are equal"
    elif [[ $a -eq $b || $b -eq $c || $c -eq $a ]]; then
        echo "I cannot figure out which number is largest"
    else
        if [ $a -gt $b -a $a -gt $c ]; then
            echo "$a is biggest number"
        elif [ $b -gt $a -a $b -gt $c ]; then
            echo "$b is biggest number"
        elif [ $c -gt $a -a $c -gt $b ]; then
            echo "$c is biggest number"
            let COUNTER=COUNTER+1
        fi
    fi
  done
}
get_number