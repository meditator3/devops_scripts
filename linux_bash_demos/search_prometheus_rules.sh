#!/bin/bash
# change grep reciever to whatever you want to search in rules
PROMPT=$(kubectl get prometheusrules -n monitoring | awk '{print $1}'| head -n -1 | tail -n+2)
echo "prompt is: $PROMPT"

D=0

for prompt in  $PROMPT 
do
	echo "doing search on $prompt"
	echo $(kubectl get prometheusrules -n monitoring $prompt -o yaml |grep receiver)
	D=$(($D + 1 ))
	echo "done another $D"
done

