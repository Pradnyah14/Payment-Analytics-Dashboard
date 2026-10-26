-- Payment Analytics & Business Finance Dashboard - Analytical Queries

-- 1. Total Revenue (Successful transactions)
SELECT SUM(amount) AS total_revenue
FROM transactions
WHERE transaction_status = 'Success';

-- 2. Total Transactions
SELECT COUNT(transaction_id) AS total_transactions
FROM transactions;

-- 3. Monthly Revenue Trend
SELECT 
    DATE_FORMAT(transaction_date, '%Y-%m') AS month,
    SUM(amount) AS monthly_revenue
FROM transactions
WHERE transaction_status = 'Success'
GROUP BY month
ORDER BY month;

-- 4. Merchant Revenue Performance
SELECT 
    merchant_name,
    SUM(amount) AS total_revenue,
    COUNT(*) AS total_transactions
FROM transactions
WHERE transaction_status = 'Success'
GROUP BY merchant_name
ORDER BY total_revenue DESC;

-- 5. Average Transaction Value (ATV)
SELECT AVG(amount) AS average_transaction_value
FROM transactions
WHERE transaction_status = 'Success';

-- 6. Success Rate by Payment Method
WITH TransactionCounts AS (
    SELECT 
        payment_method,
        COUNT(*) AS total_txns,
        SUM(CASE WHEN transaction_status = 'Success' THEN 1 ELSE 0 END) AS success_txns
    FROM transactions
    GROUP BY payment_method
)
SELECT 
    payment_method,
    total_txns,
    success_txns,
    ROUND((success_txns / total_txns) * 100, 2) AS success_rate_pct
FROM TransactionCounts
ORDER BY success_rate_pct DESC;

-- 7. Failure Rate by Gateway
SELECT 
    gateway,
    COUNT(*) AS total_txns,
    SUM(CASE WHEN transaction_status = 'Failed' THEN 1 ELSE 0 END) AS failed_txns,
    ROUND((SUM(CASE WHEN transaction_status = 'Failed' THEN 1 ELSE 0 END) / COUNT(*)) * 100, 2) AS failure_rate_pct
FROM transactions
GROUP BY gateway
ORDER BY failure_rate_pct DESC;

-- 8. Revenue Contribution by Payment Type
SELECT 
    payment_method,
    SUM(amount) AS revenue,
    ROUND(SUM(amount) * 100 / (SELECT SUM(amount) FROM transactions WHERE transaction_status = 'Success'), 2) AS revenue_share_pct
FROM transactions
WHERE transaction_status = 'Success'
GROUP BY payment_method
ORDER BY revenue DESC;

-- 9. Top 10 Merchants by Success Rate (min 50 transactions)
SELECT 
    merchant_name,
    COUNT(*) AS txn_count,
    ROUND(SUM(CASE WHEN transaction_status = 'Success' THEN 1 ELSE 0 END) * 100 / COUNT(*), 2) AS success_rate
FROM transactions
GROUP BY merchant_name
HAVING txn_count >= 50
ORDER BY success_rate DESC
LIMIT 10;

-- 10. Monthly Transaction Growth Rate
WITH MonthlyTxns AS (
    SELECT 
        DATE_FORMAT(transaction_date, '%Y-%m') AS month,
        COUNT(*) AS txn_count
    FROM transactions
    GROUP BY month
)
SELECT 
    month,
    txn_count,
    LAG(txn_count) OVER (ORDER BY month) AS prev_month_txns,
    ROUND(((txn_count - LAG(txn_count) OVER (ORDER BY month)) / LAG(txn_count) OVER (ORDER BY month)) * 100, 2) AS growth_rate_pct
FROM MonthlyTxns;
