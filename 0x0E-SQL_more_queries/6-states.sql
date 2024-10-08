-- Create the database hbtn_0d_usa if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the newly created or existing database
USE hbtn_0d_usa;

-- Create the table states if it does not already exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
