we do piping with grep usually as stdout to command, but we can do stdin to command
 examples: find / -user root 2> /dev/null
 
 example2: this will give empty:sort -R numbers.txt >> numbers.txt
, because > first creates a blank file and then fills it, so it wont have the data to pick up and sort
 example2: this will give empty:sort -R numbers.txt > numbers.txt
, because > first creates a blank file and then fills it, so it wont have the data to pick up and sort
