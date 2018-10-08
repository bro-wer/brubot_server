#!/bin/bash
while :
do
	echo "Updating git..."
        git stash
        git pull
        echo "Updated!"
	sleep 60
done
