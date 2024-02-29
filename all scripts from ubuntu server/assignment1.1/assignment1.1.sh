#!/bin/bash

		           # display 1 to 50 natural numbers via loop

				# NOTICE: IN A **HORIZONTAL WAY**

echo ""
echo ""
echo " 	         OUTPUT FOR #1 display 1-50 natural numbers" 
echo ""

for NUM in {1..50}
do
	#this condition is to avoid "," at the end of the loop	
  if [ $NUM -eq 50 ] 
  then 
	echo $NUM
  else		
	  # this displays the numbers horizontally (with -n switch)
  	echo -n "${NUM}, " 
  fi
done

