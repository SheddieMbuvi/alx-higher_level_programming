-- a sql script that creates the database hbtn_0d_usa
-- and the table states (in the database hbtn_0d_usa)
-- state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
	id INT UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT,
	state_id INT NOT NULL,
	FOREIGN KEY(state_id) REFERENCES states(id),
	name VARCHAR(256)
	);
