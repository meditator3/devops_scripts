echo "this will allow certain ports on ufw"
echo "disable ufw so it wont crash ssh"
sudo ufw status
sudo ufw disable
echo "open port 22"
sudo ufw allow 22
echo "open port 8000"
sudo ufw allow 8000
echo "now can be opened"
sudo ufw enable
echo "now 22 and 8000 are opened"
sudo ufw status numbered
curl localhost:8000
echo "to close just 8000, to block my app"
sudo ufw deny 8000
echo "check curl after blocked 8000"
curl localhost:8000
echo "if closed, open"
sudo ufw allow 8000
