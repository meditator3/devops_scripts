#!/bin/bash

	# prompt user for directory, and lock permission for it
	# for the user.

read -p "Lock which directory? >>" DIR

chmod -R 700 $DIR 
echo "Only The User $(whoami) has access to $DIR Directory"



	
