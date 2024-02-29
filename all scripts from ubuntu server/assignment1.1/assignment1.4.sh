#!/bin/bash

		# prompt user for name of file or directory
		# report if file is regular or directory or another type
		# do a long listing of ls of the file/directory
echo ""

read -p "Type in your File or Directory: " NAME 


if [ -e $NAME ]     # check if exists at all
	then

	if [ -d $NAME ]                     # checks if its a directory
	then
        	echo "$NAME is a Directory"
	elif [ -f $NAME ]
	then 		     		#  checks if its a regular file
		echo "$NAME is a regular File"
	else 		  		# if it's not a regular file(false) report it:
	echo "$NAME is different File type"
	fi
else					# if it does not exist at all - report it also
     echo "$NAME does not exist! (here at least)"

fi

echo""

ls -l $NAME    #display long listing of the object


