CREATE DATABASE IF NOT EXISTS booksdb;
USE booksdb;

CREATE TABLE IF NOT EXISTS Books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL
);

ALTER TABLE Books
ADD COLUMN loan_status VARCHAR(20) DEFAULT 'Available',
ADD COLUMN borrower VARCHAR(100);

CREATE TABLE Users (
    id VARCHAR(15) PRIMARY KEY, -- Phone number as unique identifier
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100)
);
