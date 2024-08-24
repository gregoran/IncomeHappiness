-- Create the database
CREATE DATABASE IncomeHappiness;

-- Use the database
USE IncomeHappiness;

-- Create the table
CREATE TABLE IncomeHappinessTable (
    ID INT PRIMARY KEY,
    Income DECIMAL(18, 2),
    Happiness DECIMAL(18, 2)
);

-- Insert example data (if any)
INSERT INTO IncomeHappinessTable (ID, Income, Happiness)
VALUES (1, 50000.00, 7.5),
       (2, 60000.00, 8.0),
       (3, 45000.00, 6.5);

-- Example query
SELECT * FROM IncomeHappinessTable;
