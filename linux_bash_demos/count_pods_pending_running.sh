#!/bin/bash
# use argument p or r for running or pending to count and display running/pending pods:
if [ $1 == "p" ]
then
        LIST=$(kubectl get pods -A --no-headers --field-selector status.phase=Pending)
        LIST_REVISED=$(echo -e "$LIST\n" | cat -n) # cat -n  adds count lines
        echo -e "$LIST_REVISED\n"
        TOTAL_PENDING=$(echo -e "$LIST\n" | wc -l)
        TOTAL=$((TOTAL_PENDING - 1))
        #echo "listed: $(echo $LIST_REVISED | awk '{print $3}')"
        if [[ $(echo $LIST_REVISED | awk '{print $3}') == "" ]] # if just one line and no column
        then
                echo "No Pending Pods"
        else

                echo "Total Pending pods = $TOTAL"
        fi
elif [ $1 == "r" ]
then
        LIST=$(kubectl get pods -A --no-headers --field-selector status.phase=Running)
        echo -e "$LIST\n" | cat -n
        TOTAL_RUNNING=$(echo -e "$LIST\n" | wc -l)
        TOTAL=$((TOTAL_RUNNING - 1))
        echo "Total Running pods = $TOTAL"
else
        echo "wrong Prompt, Type p for Pending, r for Running"
fi

