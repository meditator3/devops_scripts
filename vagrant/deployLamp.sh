#!/bin/bash




sudo apt-get update
sudo apt-get install -y apache2 php php-mbstring php-zip phpunit unzip libapache2-mod-php debconf-utils php-curl

sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password admin'

sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password admin'

 sudo apt-get install mysql-server -y
 sudo systemctl start mysql 
 mysql -u root -padmin < createUser.sql

 curl -Ss https://getcomposer.org/installer | php
 sudo mv composer.phar /usr/bin/composer
 sudo chown -R vagrant:vagrant /var/www
 composer global require laravel/installer
 cd /var/www
 composer create-project --prefer-dist laravel/laravel myProject
 chmod -R 777 /var/www/myProject/storage
 cd /var/www/myProject
 sudo sed -i 's/DocumentRoot.*/DocumentRoot \/var\/www\/myProject\/public/' /etc/apache2/sites-available/000-default.conf

 sudo apachectl restart

 sudo sed -i '/mysql/{n;n;n;n;s/'\''DB_DATABASE'\'', '\''.*'\''/'\''DB_DATABASE'\'', '\''myproject'\''/g}' /var/www/myProject/config/database.php
 sudo sed -i '/mysql/{n;n;n;n;n;s/'\''DB_USERNAME'\'', '\''.*'\''/'\''DB_USERNAME'\'', '\''myproject'\''/g}' /var/www/myProject/config/database.php
sudo sed -i '/mysql/{n;n;n;n;n;n;s/'\''DB_PASSWORD'\'', '\''.*'\''/'\''DB_PASSWORD'\'', '\''myproject'\''/g}' /var/www/myProject/config/database.php


