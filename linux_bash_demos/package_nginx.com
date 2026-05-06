echo "this creates nginx - breaks the conf - shows logs of whats broken - repairs and restart"
sudo apt install -y nginx
echo "check if nginx is online"
curl localhost
echo "------"
echo "now break conf"
echo "========"
echo "save conf just in case"
sudo cp /etc/nginx/nginx.conf /etc/nginx/nginx-original.conf
echo "break the conf file"
echo "dsakjhkasjfh" >> /etc/nginx/nginx.conf
echo "check nginx status"
sudo systemctl status nginx
echo " see that it broke with logs"
sudo journalctl -u nginx

echo "repair"
head -n -1 /etc/nginx/nginx.conf
echo "see that its repaired in logs"
sudo journalctl -u nginx
echo "check site is running"
curl localhost
