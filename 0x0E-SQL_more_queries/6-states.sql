-- Create the database 'hbtn_0d_usa' and table 'states' on MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

/* Create table 'states' in database 'hbtn_0d_usa' */
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
       PRIMARY KEY (id),
       id    INT    AUTO_INCREMENT,
       name  VARCHAR(256)	NOT NULL);
