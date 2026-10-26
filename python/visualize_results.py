import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create directory for images if it doesn't exist
if not os.path.exists('docs/images'):
    os.makedirs('docs/images')

# Load cleaned data
df = pd.read_csv('data/transactions_cleaned.csv')
df['date'] = pd.to_datetime(df['date'])
success_df = df[df['transaction_status'] == 'Success']

# Set style
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# 1. Revenue Trend (Line Chart)
plt.figure()
monthly_rev = success_df.groupby(df['date'].dt.to_period('M'))['amount'].sum()
monthly_rev.index = monthly_rev.index.to_timestamp()
plt.plot(monthly_rev.index, monthly_rev.values, marker='o', color='#02042B', linewidth=2)
plt.title('Monthly Revenue Trend (Successful Transactions)', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Revenue (INR)', fontsize=12)
plt.savefig('docs/images/revenue_trend.png')
plt.close()

# 2. Payment Method Breakdown (Pie Chart)
plt.figure()
payment_counts = success_df['payment_method'].value_counts()
plt.pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%', colors=sns.color_palette('viridis'), startangle=140)
plt.title('Successful Transactions by Payment Method', fontsize=14)
plt.savefig('docs/images/payment_methods.png')
plt.close()

# 3. Top 10 Merchants by Revenue (Bar Chart)
plt.figure()
merchant_rev = success_df.groupby('merchant_name')['amount'].sum().sort_values(ascending=False).head(10)
sns.barplot(x=merchant_rev.values, y=merchant_rev.index, palette='magma')
plt.title('Top 10 Merchants by Revenue', fontsize=14)
plt.xlabel('Revenue (INR)', fontsize=12)
plt.ylabel('Merchant Name', fontsize=12)
plt.savefig('docs/images/top_merchants.png')
plt.close()

# 4. Success vs Failure Analysis (Count Plot)
plt.figure()
sns.countplot(data=df, x='payment_method', hue='transaction_status', palette='coolwarm')
plt.title('Transaction Status by Payment Method', fontsize=14)
plt.xlabel('Payment Method', fontsize=12)
plt.ylabel('Transaction Count', fontsize=12)
plt.legend(title='Status', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('docs/images/status_analysis.png')
plt.close()

print("Pictorial dashboard images generated successfully in docs/images/")
