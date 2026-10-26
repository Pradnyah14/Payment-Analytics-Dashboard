import pandas as pd
import numpy as np

def clean_data(file_path):
    print(f"Loading data from {file_path}...")
    df = pd.read_csv(file_path)
    
    # 1. Date Conversion
    df['date'] = pd.to_datetime(df['date'])
    
    # 2. Handling Missing Values
    # In a real scenario, we might fill or drop. Here we ensure no NaNs in critical columns.
    df['amount'] = df['amount'].fillna(0)
    df['transaction_status'] = df['transaction_status'].fillna('Unknown')
    
    # 3. Duplicate Removal
    duplicate_count = df.duplicated().sum()
    if duplicate_count > 0:
        print(f"Removing {duplicate_count} duplicate records.")
        df = df.drop_duplicates()
    
    # 4. Currency Normalization (Ensuring amount is float and positive)
    df['amount'] = df['amount'].apply(lambda x: abs(float(x)))
    
    # 5. Validation Checks
    # Example: Processing fee shouldn't be more than the amount
    df = df[df['processing_fee'] <= df['amount']]
    
    # 6. Feature Engineering
    df['month_year'] = df['date'].dt.to_period('M')
    df['day_of_week'] = df['date'].dt.day_name()
    
    # Save cleaned data
    cleaned_path = file_path.replace('.csv', '_cleaned.csv')
    df.to_csv(cleaned_path, index=False)
    print(f"Cleaned data saved to {cleaned_path}")
    return df

def calculate_kpis(df):
    print("\n--- Business KPIs ---")
    
    # Filter for successful transactions for revenue metrics
    success_df = df[df['transaction_status'] == 'Success']
    
    total_revenue = success_df['amount'].sum()
    total_txns = len(df)
    success_rate = (len(success_df) / total_txns) * 100
    avg_txn_value = success_df['amount'].mean()
    
    print(f"Total Revenue: INR {total_revenue:,.2f}")
    print(f"Total Transactions: {total_txns:,}")
    print(f"Success Rate: {success_rate:.2f}%")
    print(f"Average Transaction Value: INR {avg_txn_value:.2f}")
    
    # Merchant Performance
    merchant_perf = success_df.groupby('merchant_name')['amount'].sum().sort_values(ascending=False).head(5)
    print("\nTop 5 Merchants by Revenue:")
    print(merchant_perf)

if __name__ == "__main__":
    df_cleaned = clean_data('data/transactions.csv')
    calculate_kpis(df_cleaned)
