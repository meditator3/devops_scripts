echo "you attach a volume via vm box - make sure to add to SATA and not the ide - or it'll think its boot and vm wont load!"
echo "create pv,vg, lv (physical volume > volume group > logical volume(size it and save some)"
sudo pvcreate /dev/sdc
sudo pvdisplay 
sudo vgcreate storg1 /dev/sdc
sudo vgdisplay
sudo lvcreate --size 40m storg2
sudo lvdisplay


echo "should see now some name on storg2 lv vol0 or something like that"
echo " now create the file system because otherwise it wont mount to your folder"
sudo mkfs.ext4 /dev/storg2/lvol0
echo "create folder for vol"
sudo mkdir /mnt/vol2-vol0
sudo mount /dev/storg2/lvol0 /mnt/vol2-vol0

echo " and now to make it permament in fstab"
echo " put this line in:"
sudo vi /etc/fstab
echo "careful its VERY sensitive and can brfeak boot forever!"
echo " /dev/storg2/lvol0 /mnt/vol2-vol0 ext4 defaults 0 0 "
