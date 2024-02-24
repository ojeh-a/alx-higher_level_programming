-- Creates the database 'hbtn' and the user 'user_0d_2'
CREAATE DATABASE IF NOT EXISTS 	hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0b_2.* TO 'user_0d_2'@'localhost';
