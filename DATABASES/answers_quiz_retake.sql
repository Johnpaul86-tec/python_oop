-- answers_quiz_retake.sql
-- Author: johnpaul
-- Purpose: SQL Quiz Retake – Week 2
-- Date: 15 August 2025
-- Database: salesdb


USE salesdb;
-- Query 1: Retrieve payment details
SELECT checkNumber, paymentDate, amount
FROM payments;

-- Query 2: Get 'In Process' orders, sorted by most recent order date
SELECT orderDate, requiredDate, status
FROM orders
WHERE status = 'In Process'
ORDER BY orderDate DESC;

-- Query 3: List Sales Reps with contact info, ordered by employee number
SELECT firstName, lastName, email
FROM employees
WHERE jobTitle = 'Sales Rep'
ORDER BY employeeNumber DESC;

-- Query 4: Show all office records and details
SELECT *
FROM offices;

-- Query 5: Get 5 cheapest products with their stock quantity
SELECT productName, quantityInStock
FROM products
ORDER BY buyPrice ASC
LIMIT 5;
