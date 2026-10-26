# Data Dictionary - Payment Analytics Dashboard

| Column Name | Data Type | Description | Sample Values |
|-------------|-----------|-------------|---------------|
| `transaction_id` | VARCHAR | Unique identifier for each transaction | TXN100001 |
| `date` | DATETIME | Date and time of the transaction | 2023-05-12 14:30:00 |
| `merchant_name` | VARCHAR | Name of the business receiving payment | Amazon, Zomato |
| `customer_id` | VARCHAR | Unique identifier for the customer | CUST5521 |
| `payment_method` | ENUM | Method used for payment | UPI, Credit Card, Wallet |
| `amount` | DECIMAL | Transaction value in INR | 500.00, 12000.50 |
| `transaction_status`| ENUM | Current status of the transaction | Success, Failed, Refunded |
| `city` | VARCHAR | City where the transaction originated | Mumbai, Bangalore |
| `state` | VARCHAR | State where the transaction originated | Maharashtra, Karnataka |
| `gateway` | VARCHAR | Payment gateway provider | Razorpay, Paytm |
| `device_type` | VARCHAR | Device used for transaction | Android, iOS, Web |
| `processing_fee` | DECIMAL | Fee charged by the gateway | 5.00, 150.20 |

## Status Values:
- **Success**: Transaction completed successfully.
- **Failed**: Transaction failed due to technical or bank issues.
- **Pending**: Transaction is currently being processed.
- **Refunded**: Transaction amount returned to the customer.

## Payment Methods:
- **UPI**: Unified Payments Interface (Mobile apps).
- **Credit Card**: Credit card transactions.
- **Debit Card**: Debit card transactions.
- **Wallet**: Digital wallets (Paytm, PhonePe).
- **Net Banking**: Direct bank transfer via web.
