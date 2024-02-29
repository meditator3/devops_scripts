#!/bin/bash

# takes any number of directories from user and lists them all

read -p "what directories do you want to list? >>" DIRECTORIES

for DIRS in $DIRECTORIES 
do
	echo ""
	echo "this displays $DIRS Directory:"
	echo ""
	echo $(ls $DIRS)
	echo ""
done

