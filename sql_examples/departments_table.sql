-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS my_database;

-- Select the database to use
USE my_database;

DROP TABLE IF exists departments;

CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(255) UNIQUE NOT NULL
);


INSERT INTO departments (department_id, department_name) VALUES
(1, 'Finance'),
(2,  'IT'),
(3, 'Marketing'),
(4, 'Sales');


SELECT * FROM departments;


TRUNCATE TABLE departments;
