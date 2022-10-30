#!/bin/bash
# Daily 45
# Author: Mhinkyu Kim
# function that takes external file name as argument and turns it into an executable file
external_arguments=($@)

main () {
    chmod u+x $external_arguments
}
main