-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS my_database;

-- Select the database to use
USE my_database;


DROP TABLE IF EXISTS employees;


CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    liast_name VARCHAR(255) NOT NULL,
    age INT,
    gender CHAR(1),
    department VARCHAR(255)
);


INSERT INTO employees (id, name, surname, age, gender, department) VALUES
(1, 'Alice', 'Smith', 20, 'm', 'Finance'),
(2, 'Bob', 'Johnson', 20, 'm', 'IT'),
(3, 'Charlie', 'Williams', 30, 'm', 'Marketing'),
(4, 'David', 'Jones', 40, 'm', 'IT'),
(5, 'Eve', 'Brown', 50, 'f', 'Sales'),
(6, 'Fiona', 'Davis', 40, 'f', 'Finance'),
(7, 'George', 'Miller', 50, 'f', 'Marketing'),
(8, 'Hannah', 'Wilson', NULL, NULL, 'Finance'),
(9, 'Ian', 'Moore', NULL, NULL, 'Marketing'),
(10, 'Jane', 'Taylor', NULL, NULL, 'IT'),
(11, 'Kevin', 'Anderson', 25, 'm', 'Sales'),
(12, 'Laura', 'Thomas', 26, 'f', 'IT'),
(13, 'Mike', 'Jackson', 27, 'm', 'Sales'),
(14, 'Nancy', 'White', 28, 'f', 'Marketing'),
(15, 'Oscar', 'Harris', 29, 'm', 'Finance'),
(16, 'Pam', 'Martin', 30, 'f', 'Marketing'),
(17, 'Quincy', 'Thompson', 31, 'm', 'IT'),
(18, 'Rachel', 'Garcia', 32, 'f', 'Sales'),
(19, 'Sam', 'Martinez', 33, 'm', 'IT'),
(20, 'Tina', 'Robinson', 34, 'f', 'Sales');


SELECT * FROM employees;

TRUNCATE TABLE employees;
