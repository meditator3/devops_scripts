#!/bin/bash

	# display odd numbers only from 0 to 99 
	# HORIZONTAL print 

echo""

for NUM in {1..99} 
do
	# check if the number divided by 2 has a remainder(opposite of even number)
	if [ $((NUM % 2 )) -ne 0 ] 
	then 
		echo -n "${NUM}  "
	fi
done	

echo ""

