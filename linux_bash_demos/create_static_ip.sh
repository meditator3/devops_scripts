echo "in centos typically netmanager is built in, so you can ntmui or nmcli to apply static ip"
echo "in ubuntu its in /etc/netplan/<some sort of yaml file>"

echo " also you need to remove cloud init auto generation because it'll override this new setting"
echo " sudo vi /etc/cloud/cloud.cfg.d/99-disable-network-config.cfg"
echo " in the vi --  network: {config: disabled}
echo "you can edit the yaml to this:"
echo "check also ip a for interface name"
networks:
  ethernets:
    enp0s3: 
      dhcp4: false
      addresses: 
        - 192.168.1.235/24
      gateway4: 192.168.1.1
      nameservers: 
        addresses:
          - 8.8.8.8
      
      
version: 2
echo "we define /24 bits to inform the system which network it resides. the boundry of the network 192.168.1.0-255 "
echo " then apply with sudo netplan apply"
echo " dhcp4 is method for creating temp ip4 addresses, so it must be set to false, in static sceanrio, like here"
