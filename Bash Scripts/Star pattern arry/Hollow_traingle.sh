#!/bin/bash
size=9
col=1
row=$size
echo
function Hollow_traingle () { 
    while [[ $col -le $size ]]
    do
        row=1
        let a=$((size-col))
        while [[ $row -le $size ]]
        do
            if [[ $row -eq $size || $a -eq $row-1 || $col -eq $size ]]
            then
                echo -n "* "
            else
                echo -n "  "
            fi
        let $((row++))
        done
        let $((col++))
        echo
    done
}
Hollow_traingle