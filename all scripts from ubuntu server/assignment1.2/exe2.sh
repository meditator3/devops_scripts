#!/bin/bash

	# reads prompt directory from user- 
	# counts number of files in the directory
	# or, if no input - return number of the files in current directory

read -p "Type in your Directory name: " NAME

       # wc -l displays the count of lines for the ls prompt

NUM_OF_LINES=$(ls $NAME |wc -l)

	# even if the user doesn't prompt anything it will read it as just-
	# ls |wc -l 
	# which gives the desired output

echo $NUM_OF_LINES

