echo "script to un extend volume from vg unbuntu-vg and create one decoupled"
echo "showing all current volume groups, logical volumes, and physical vol"
sudo vgs
sudo lvs
suco pvs
echo "remove extension of sdb from ubuntu-vg"
sudo vgreduce ubuntu-vg /dev/sdb
sudo vgcreate practice_storage /dev/sdb
echo "see decoupled storage"
sudo vgs
echo "create logical volume from physical volume of volume group"
 sudo lvcreate -L 10k -n storg_prac practice_storage
echo "minimum is 4mb for volume"
echo "see list of block storage"
lsblk
echo "now format just this logical volume"
sudo mkfs.ext4 /dev/practice_storage/storg_prac
echo "mount according to naming"
sudo mkdir /mnt/prac_storg
sudo mount /dev/practice_storage/storg_prac /mnt/prac_storg
echo "showing new volume in new folder "
lsblk

