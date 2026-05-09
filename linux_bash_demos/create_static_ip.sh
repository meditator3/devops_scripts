echo "in centos typically netmanager is built in, so you can ntmui or nmcli to apply static ip"
echo "in ubuntu its in /etc/netplan/<some sort of yaml file>
echo "you can edit the yaml to this:"
echo "check also ip a for interface name"
networks:
  ethernets:
    enp0s3: 
      dhcp4: no
      addresses: 
        - 192.168.1.235
      gateway4: 198.168.1.1
      nameservers: 
        addresses:
          - 8.8.8.8
      
      
version: 2
