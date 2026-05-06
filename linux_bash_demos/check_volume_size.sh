echo "this checks if disk is full more than 1% and sends warning"
echo "then it will become also a script via cronjob/crontab"

STRING=$(sudo df -T /mnt/prac_storg | awk '{ print $6 }' | tail -n 1)
DISK_USAGE=${STRING%\%}
echo "disk usage now is on $DISK_USAGE"
sudo touch /mnt/prac_storg/added_storage.txt
echo "now adding more storage"
for i in {1..450}; do
        echo "this is just aline to add storage number $i" | sudo tee -a /mnt/prac_storg/added_storage.txt
done
STRING=$(sudo df -T /mnt/prac_storg | awk '{ print $6 }' | tail -n 1)
DISK_USAGE=${STRING%\%}

echo "and now storage in new volume is:$STRING "

if [ $DISK_USAGE -gt 1 ]
then
        echo "TOO MUCH STORAGE!!"
fi

