#!/bin/bash

export CAMERA_IP_FILE=camera_ip

for CAMERA_IP in $(cat camera_ip)
do
ping -n 1 $CAMERA_IP >> output.txt
done
 
