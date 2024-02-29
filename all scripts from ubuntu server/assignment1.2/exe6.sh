#!/bin/bash

# create a command/bash script without a prompt that takes integers only
# and sorts them. ex: ./sort.sh 44 5 11 0 -1 3.2 >>output should be:
# 				1 0 3.2 is not an integer! 5 11 44
#				  

 		# loop over input numbers
for NUM in $@ 
do
		# finds if number has a '.' in it
	CHECK=$(echo $NUM |grep -F '.')
		# if it finds then the status=0. if not print into file
	STATUS=$?
	if [ $STATUS -gt 0 ]
	then	
		echo "$NUM" >> to_sort.txt 
	else	
		# in case the status is 0(finds a '.') print this error:
	   echo "$NUM not in integer!!" >> to_sort.txt
	fi
done 
echo ""
echo "sorted numbers:"
	# sort the file that the numbers were sent to (to_sort.txt)
	# sort also output the ordered numbers, no need for another loop
	
sort -n to_sort.txt 
		# delete temp file
rm to_sort.txt 




