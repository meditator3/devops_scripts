#!/bin/bash
# this script will update linux and upgrade it fully
# we can run this any day

echo ""
echo ""
echo "#############################"
echo "# Updating Operating System #"
echo "#############################"
echo ""
echo ""
# -y is always unattended, automatically does yes to all updates

apt update && apt upgrade -y
echo ""
echo ""
echo "#############################"
echo "#   Done Updating System    #"
echo "#############################"
echo ""
echo ""


echo "#############################"
echo "#   running full upgrade    #"
echo "#############################"
apt full-upgrade -y

