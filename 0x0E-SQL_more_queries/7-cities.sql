-- Create database 'hbtn_0d_usa' and table 'cities' on MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

/* Create table 'cities' in hbtn_0d_usa */
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
       PRIMARY KEY (id),
       id      	   INT		AUTO_INCREMENT,
       state_id	   INT		NOT NULL,
       name	   VARCHAR(256),

       FOREIGN KEY (state_id)
              REFERENCES hbtn_0d_usa.states(id));
