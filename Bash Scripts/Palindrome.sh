#!/bin/bash

isPalindrome() {
    echo "Please enter a word to check if it is a palindrome"
    read word
    for i in $(seq 0 ${#word})
    do
        rvstr=${word:$i:1}${rvstr}
    done
    echo "Input String: $word"
    echo "Reversed String: $rvstr"

    if [ "$word" == "$rvstr" ]
    then
        echo "Ture"
    else
        echo "False"
    fi
}
isPalindrome