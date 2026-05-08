echo "this lists all rules of iptables, which is filtering before application layer"
sudo iptable -L
echo "added rule to drop all connections when connecting to port 8000"
sudo iptables -A INPUT -p tcp --dport 8000 -j DROP
echo " can be added to that line 10.0.0.0/24 to allow this cidr block access and then"
echo " iptables -A INPUT -j DROP"

echo " now it will show that it is blocked:"
sudo iptables -L --line-numbers
echo " we use line numbers to determine which rule to delete so i can open the port again"
echo "this is bad usage of iptables, can be easily done with ufw"
echo "but is meant as demo"
echo "and now to delete the rule:"
sudo iptables -D INPUT 1
echo "rule deleted:"
sudo iptables -L
