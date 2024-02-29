#!/bin/bash

VAR="Y"
#VAR="y"
#VAR="N"
#VAR="n"

if [ $VAR = "y" ]
then 
	echo "YES"
elif [ $VAR = "Y" ]
then 
	echo "YES!"
elif [ $VAR = "n" ]
then
	echo "NO"
elif [ $VAR = "N" ] 
then
        echo "NO"
fi

		

echo " this is ${VAR} "
