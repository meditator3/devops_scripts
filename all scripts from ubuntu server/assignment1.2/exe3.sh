#!/bin/bash

# find user and see if he's locked or not

read -p "what user do you want to find?  >>" USER

USER_EXISTS=$(grep $USER /etc/passwd)
# this is to save error code in case user doesn't exist
NOT_EXIST=$?

# if the string "USER_EXISTS" is empty it means he didn't find any user.

if [ $NOT_EXIST -eq 0 ]
then
	echo ""
	echo "$USER is a user in this system!" 
	echo ""
       # save the output for Locked/Password enabled
	
	IS_LOCKED=$(passwd -S $USER | grep -e L)  

	# if the wordcount for ISLOCKED is higher than 1
	# since "grep -e L" gave full string if it has found locked user
	# if it didnt find something with L then the string length = 1
	
	if [ $(echo $IS_LOCKED|wc -w) -gt 1 ]
	then 
		echo "Sorry, User $USER is LOCKED!"
		echo ""
	else
		echo "$USER is not locked, phew :)"
		echo ""
	fi	

else 
	echo ""
	echo "USER $USER DOES NOT EXIST, HE IS PROBABLY IN ANOTHER DIMENSION!!!"
	echo ""
fi


