if config; ;
ifconfig
ip addr
apt update
sudo apt update
sudo apt install nginx
systemctl status nginx
sudo find / system-enable
sudo find / |grep system-enable
sudo find / |grep system-en
sudo vi /etc/nginx/sites-enabled/
sudo vi /etc/nginx/sites-enabled/default 
systemctl restart nginx
sudo systemctl restart nginx
systemctl status nginx
ls
systemctl status nginx
sudo apt update
sudo apt install nginx
systemctl status nginx
sudo vi /etc/nginx/sites-enabled/default 
ip addr
ping 3.76.197.32
systemclt status nginx
systemctl status nginx
systemctl status nginx
sudo vi /etc/nginx/sites-enabled/default 
sudo systemctl restart nginx
systemctl status nginx
sudo vi /etc/nginx/sites-enabled/default 
ls
systemctl status nginx
sudo vi /etc/nginx/sites-enabled/default 
ip addr
ping 127.0.0.1
ping 10.0.42.61
ping ec2-18-184-18-55.eu-central-1.compute.amazonaws.com
ls
cd /etc/groups
ls /etc/usr
ls /etc/passwd
netstat
lscpu
free -h
ufw status
sudo ufw status
grep -i /etc/passwd
cat /etc/passwf
cat /etc/passwd
ls
echo 'i am creating rebel alliance and secret plans file only accesible by rebel-alliance group, darth vader will have trouble accessing it, while luke can.' >> README.txt
ls
cat README.txt 
ls
man addusr 
addusr --help
adduser --help
adduser lskywalker
sudo adduser lskywalker
cat /etc/passwd
su lskywalker
sudo passwd ubuntu
sudo addgroup rebel-alliance
sudo passwd root
su lskywalker
history
sudo usermod -a -G sudo lskywalker
su lskywalker
sudo cat /etc/groups
cat /etc/group
ls
whomai
whoami
sudo usermod -a -G rebel-alliance lskywalker
ll
su lskywalker
useradd dvader
sudo useradd dvader
sudo passwd dvader
su dvader
uname -a
ls
cat README.txt 
cat /etc/passwd
cd ../..
ls
cd /
ls
groups
whoami
su lskywalker
cd ~
ls
cat /etc/shadow
sudo cat /etc/shadow
ok
diff --help
cp README.txt README2.txt
echo "  \nbz" >>README2.txt 
cat README2.txt 
diff README.txt README2.txt 
sudo systemctl opensshd
sudo systemctl open-sshd
sudo systemctl status openssh
sudo systemctl status opensshd
sudo systemctl status open-sshd
top
netstat -tanup
ps -aux
systemctl status sshd
sudo apt install net-tools
netstat -tanup
ls
cat README2.txt 
cat README.txt
apt install tree
sudo apt install tree
tree -d -L 2
ls
cd ls
cd /
ls
tree -d -L 2
tree -d -L 3
בג .אצפ
cd /
ls
ll
ls
cd ~
ls
mkdir xargs
ls
ls x* |xargs cd
ls
ls x*
ls
ls xa*
ls
ls r*
cd xargs/
ls
mkdir xargs
ls
cd ..
ls
ls x*
ls x* |xargs cd
ls
ls x*
echo "1 2 3 4 5 6 " |xargs touch
ls
ll
echo "1 2 3 4 5 6 " |xargs rm
ls
ךד
ls
ll
touch 1
ls
ll
chmod 777 1
ll
sudo mv 1 /tmp
cd /tmp
ls
ll
tail history
history |xargs tail
history -n 10
ll
history
wc README.txt 
wc -l README.txt 
wc -m README.txt 
wc -c README.txt 
wc  README.txt 
man wc
wc -w README2.txt 
wc -w README.txt 
ls
wc -w how-to-use-xargs.txt.txt 
wc -w how-to-use-xargs.txt
ךד
ls -li
mv how-to-use-xargs.txt how-to-use-xargs2.txt 
ls -li
mv how-to-use-xargs2.txt /xargs/how-to-use-xargs.txt
mv how-to-use-xargs2.txt xargs/how-to-use-xargs.txt
ls
cp xargs/how-to-use-xargs.txt how-to-use-xargs-cpy.txt
ls
ls -li
ls -li xargs/
lsof
lsof 2>devnull
lsof 2>devnull |wc -l
lsof 2>devnull | tail
lsof 2>devnull | head
lsof 2>devnull | tail
df -h -i
df -h / -i
ls
del devnull 
delete devnull 
rm devnull 
ls
cd /etc/netplan
ls
cat 50-cloud-init.yaml 
ls
mkdir scp-transfer-demo
cd scp-transfer-demo/
ls
echo "use scp to transfer these files" >> README.txt
ls
cat README.txt 
touch test1 test2 test3
ls
cd scp-transfer-demo/
ls
vi README.txt 
cat README.txt 
vi README.txt 
cat README.txt 
ls
cd ..
ls
mv ariel-key.pem scp-transfer-demo/
ls
cd scp-transfer-demo/
ls
scp -i "ariel-key.pem" test3 ubuntu@ 3.71.0.71:home/ubuntu
ls
rm ariel-key.pem 
ls
cat README.txt 
vi README.txt 
cat README.txt 
shutdown now
sudo shutdown now
ls
grep error auth.log
sudo find / -name auth.log
cd /var/log
ls
grep error auth.log
cat auth.log
grep '^Oct 17' auth.log
grep 'root$' auth.log
clear
grep 'root$' auth.log
sl
ls
man egrep
cat std-in-out-err
cd stdin-stdout-demos/
ls
echo ' 6' >> numbers.txt 
cat numbers.txt 
vi numbers.txt 
4 < numbers.txt 
echo '4' < numbers.txt 
cat numbers.txt 
$? < numbers.txt
wc -l < numbers.txt 
find /var -user root 2>dev 
find /var -user ubuntu 2>dev 
find / -user lskywalker 2>dev 
find / -user lskywalker 2> /dev/null 
find / -user root 2> /dev/null 
su lskywalker
sort -R numbers.txt > numbers.txt
cat numbers.txt 
ls
cat dev 
rm dev
ls
vi numbers.txt 
sort -R numbers.txt
cat numbers.txt 
sort -R numbers.txt >> numbers.txt 
cat numbers.txt 
sort -R numbers.txt >> numbers.txt 
cat numbers.txt 
sort numbers.txt 
sort numbers.txt > numbers.txt
cat numbers.txt 
vi numbers.txt 
ls /var
ls /etc
ls /etc > lsetc.txt
sort <lsetc.txt 
cat lsetc.txt  | sort 
sort < lsetc.txt 
sort < lsetc > sorted-lsetc.txt
ls
ps -aux 
ps -aux | grep ubuntu
ps -aux | grep root
ps -fp 
vi sleepy.sh
./sleepy.sh
sh sleepy.sh 
vi sleepy.sh
sh sleepy.sh &
sh sleepy.sh &&
sh sleepy.sh &
ps -fp 850
vi sleepy.sh
ls
vi sleepy.sh 
ls
sh sleepy.sh &
vi sleepy.sh 
sh sleepy.sh &
echo $!
echo $?
vi sleepy.sh 
sh sleepy.sh &
vi sleepy.sh 
sh sleepy.sh &
vi sleepy.sh 
ls
vi sleepy.sh 
sh sleepy.sh 
sh sleepy.sh &
echo $!
cat sleepy.sh 
vi sleepy.sh 
ls
sh sleepy.sh 
vi sleepy.sh 
sh sleepy.sh 
vi sleepy.sh 
sh sleepy.sh 
cat sleepy.sh 
vi sleepy.sh 
sh sleepy.sh 
vi sleepy.sh 
sh sleepy.sh 
sh sleepy.sh &
ps -fp sleepy
ps -fp sleepy.sh
vi sleepy.sh 
sh sleepy.sh &
ps -aux |grep sleepy
sh sleepy.sh &
ps -aux |grep sleepy
vi sleepy.sh 
sh sleepy.sh &
sh sleepy.sh 
sleep 30 &
pidof sleep
vi sleepy.sh 
sh sleepy.sh &
vi sleepy.sh 
sh sleepy.sh &
vi sleepy.sh 
sh sleepy.sh &
vi sleepy.sh 
sh sleepy.sh &
vi sleepy.sh 
sh sleepy.sh &
vi sleepy.sh 
sh sleepy.sh &
pidof sleep
vi sleepy.sh 
sh sleepy.sh &
vi sleepy.sh 
sh sleepy.sh &
vi sleepy.sh 
sh sleepy.sh &
cat sleepy.sh 
ls
cd stdin-stdout-demos/
ls
cat README.txt 
cat numbers.txt 
history
echo "4" < numbers.txt
ls
cat numbers.txt 
echo < numbers.txt
echo --help
man echo
man print
print --help
echo " examples: find / -user root 2> /dev/null
 " >>README.txt 
cat RE
cat README.txt 
echo " example2: this will give empty : [200~sort -R numbers.txt >> numbers.txt
echo " example2: this will give empty:sort -R numbers.txt >> numbers.txt
, because > first creates a blank file and then fills it, so it wont have the data to pick up and sort" >> README.txt 
cat README.txt 
echo " example2: this will give empty:sort -R numbers.txt >> numbers.txt
, because > first creates a blank file and then fills it, so it wont have the data to pick up and sort" >> README.txt 
sort -R numbers.txt >> numbers.txt
cat numbers.txt 
vi README.txt 
cd ..
ls
cat README
cat README2.txt 
cat README.txt 
cat lsetc.txt 
ls
cat sleepy.sh 
sudo ./sleepy.sh &
sh sleepy.sh &
echo $!
ps -f 936
sh sleepy.sh &
ps -f 941
echo " do : sh sleepy.sh & , and then ps -f <number of PID>, if you do it before 15 seconds you'll see result in the processes table" >> sleep_demo.txt
sh sleepy.sh &
ps -ef |grep 945 | grep -v grep
cat sleepy.sh 
vi python.sh
;s
ls
mv python.sh python.py
ls
sudo chmod 755 python.py
./python.py 
apt install python
sudo apt install python
sudo apt install python-is-python3
where python
where sh
which python
cat python.py 
python python.py
vi python.py 
python python.py
echo "python python.py to run the python script, also i installed apt install python-is-python3" >> python_demo.txt
ls
./sleepy.sh
sudo ./sleepy.sh
ll 
ls *.sh | xargs chmod u+x
ls
echo" ls *.sh | xargs chmod u+x ...which creates executable permission for all scripts, instead of running it with sh!">>xargs_demo.txt
ls
cat xargs_demo.txt 
vi xargs_demo.txt 
cat xargs_demo.txt 
./sleepy.sh 
ps -ef 1266
ps -e 1266
ps | grep sleepy
ls
./python.py 
cat python_demo.txt 
echo " its actully can run with ./python.py if you changed the permission to executable :)" >> python_demo.txt 
cat python_demo.txt 
