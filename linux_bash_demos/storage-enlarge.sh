echo "creating new volume for usage- enlarging storage"
echo "in virtual box -make sure machine is completely shut down first"
echo "settings>storage>(SATA controller)new hard drive> create virtual hard drive>attach it"
lsblk
echo "should see sdb as disk according to your volume size"
pvcreate /dev/sdb 
echo " this creates physical volume from  /dev/sdb from your sdb(full size)"
echo "if we'd want to extend this size to our current volume group"
vgdisplay
echo "this shows our current volume groups names, lets say its ubuntu-vg is what we want to extend"
vgextend ubuntu-vg /dev/sdb
echo "should say successfully extended volume group ubuntu-vg"
echo "now we shall create logical volume out of a volume group and make it separate partition/group and volume"
