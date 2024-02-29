
CREATE DATABASE myProject;

CREATE USER 'myProject'@'localhost' IDENTIFIED BY 'mypassword';

GRANT ALL PRIVILIGES ON myProject.* TO 'myProject'@'localhost';

FLUSH PRIVILEGES



