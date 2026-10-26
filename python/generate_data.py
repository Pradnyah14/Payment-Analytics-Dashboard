import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Set seed for reproducibility
np.random.seed(42)

def generate_data(num_records=5000):
    merchants = ['Amazon', 'Flipkart', 'Zomato', 'Swiggy', 'Uber', 'Ola', 'Reliance Digital', 'Myntra', 'BigBasket', 'Nykaa']
    payment_methods = ['UPI', 'Credit Card', 'Debit Card', 'Wallet', 'Net Banking']
    statuses = ['Success', 'Failed', 'Pending', 'Refunded']
    cities = ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Ahmedabad', 'Chennai', 'Kolkata', 'Pune', 'Jaipur', 'Lucknow']
    states = ['Maharashtra', 'Delhi', 'Karnataka', 'Telangana', 'Gujarat', 'Tamil Nadu', 'West Bengal', 'Maharashtra', 'Rajasthan', 'Uttar Pradesh']
    gateways = ['Razorpay', 'Paytm', 'Cashfree', 'BillDesk', 'Stripe']
    devices = ['Android', 'iOS', 'Web', 'Desktop']
    
    city_state_map = dict(zip(cities, states))
    
    data = []
    start_date = datetime(2023, 1, 1)
    
    for i in range(num_records):
        transaction_id = f'TXN{100000 + i}'
        date = start_date + timedelta(days=random.randint(0, 365), hours=random.randint(0, 23), minutes=random.randint(0, 59))
        merchant = random.choice(merchants)
        customer_id = f'CUST{random.randint(1000, 9999)}'
        payment_method = random.choice(payment_methods)
        
        # Amount logic: UPI usually smaller, Credit Card larger
        if payment_method == 'UPI':
            amount = round(random.uniform(10, 2000), 2)
        elif payment_method == 'Credit Card':
            amount = round(random.uniform(500, 50000), 2)
        else:
            amount = round(random.uniform(100, 10000), 2)
            
        status = np.random.choice(statuses, p=[0.85, 0.08, 0.04, 0.03])
        city = random.choice(cities)
        state = city_state_map[city]
        gateway = random.choice(gateways)
        device = random.choice(devices)
        
        # Processing fee logic: 1-3% of amount
        fee_pct = random.uniform(0.01, 0.03)
        processing_fee = round(amount * fee_pct, 2)
        
        data.append([
            transaction_id, date, merchant, customer_id, payment_method, 
            amount, status, city, state, gateway, device, processing_fee
        ])
        
    df = pd.DataFrame(data, columns=[
        'transaction_id', 'date', 'merchant_name', 'customer_id', 'payment_method', 
        'amount', 'transaction_status', 'city', 'state', 'gateway', 'device_type', 'processing_fee'
    ])
    
    # Sort by date
    df = df.sort_values('date')
    
    # Save to CSV
    df.to_csv('data/transactions.csv', index=False)
    print(f"Generated {num_records} records in data/transactions.csv")

if __name__ == "__main__":
    generate_data()
