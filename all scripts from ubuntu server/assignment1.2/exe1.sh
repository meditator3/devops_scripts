#!/bin/bash

        # checks the error exit staus for running cat /etc/shadow 


cat /etc/shadow

# this following command reads the exit status of last command ^

RESULT=$?
echo ""
echo ""

# now the exit status value is saved
if [ $RESULT -eq 0 ] 
then
	echo "Command Succeeded!"
elif [ $RESULT -gt 0 ]
then 
	echo "Command Failed!"
fi

echo ""




