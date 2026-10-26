-- Payment Analytics & Business Finance Dashboard - SQL Schema

CREATE DATABASE IF NOT EXISTS payment_analytics;
USE payment_analytics;

-- Drop table if exists
DROP TABLE IF EXISTS transactions;

-- Create transactions table
CREATE TABLE transactions (
    transaction_id VARCHAR(20) PRIMARY KEY,
    transaction_date DATETIME NOT NULL,
    merchant_name VARCHAR(100) NOT NULL,
    customer_id VARCHAR(20) NOT NULL,
    payment_method ENUM('UPI', 'Credit Card', 'Debit Card', 'Wallet', 'Net Banking') NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    transaction_status ENUM('Success', 'Failed', 'Pending', 'Refunded') NOT NULL,
    city VARCHAR(50),
    state VARCHAR(50),
    gateway VARCHAR(50),
    device_type VARCHAR(20),
    processing_fee DECIMAL(15, 2)
);

-- Indexing for performance
CREATE INDEX idx_merchant ON transactions(merchant_name);
CREATE INDEX idx_status ON transactions(transaction_status);
CREATE INDEX idx_date ON transactions(transaction_date);
