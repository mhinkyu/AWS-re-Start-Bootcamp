#!/bin/bash
#REmote SSH Connect
function SSH() {

        read -p "Enter IP Address: " ip
        read -p "Enter User: " user
        read -p "Enter Private Key: " pkey

        ssh -i $pkey $user@$ip

}
SSH