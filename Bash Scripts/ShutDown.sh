#!/bin/bash
# Bash Menu Script Example
function shutdown() {

PS3='Please enter your choice: '
select opt in shutdown restart Quit;
do
    case $opt in
            shutdown)
            echo "System shutdown now"
            sleep 3
            shutdown -h now
            ;;
            restart)
            echo "System restart now"
            sleep 3
            reboot
            ;;
            Quit)
            echo "Bye"
            sleep 1
            exit 0
            ;;
    esac
done
}
shutdown