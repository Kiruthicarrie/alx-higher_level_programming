-- Create a MySQL server user named 'user_0d_1' whose password is 'user_0d_1_pwd'
CREATE USER IF NOT EXISTS user_0d_1@localhost;

/* SET password for newly_created user */
SET PASSWORD FOR user_0d_1@localhost = 'user_0d_1_pwd';

/* Grant the user all privileges on the MySQL server */
GRANT ALL PRIVILEGES
   ON *.*
   TO user_0d_1@localhost;
