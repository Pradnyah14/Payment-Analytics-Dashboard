import pandas as pd

def generate_business_insights(file_path):
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date'])
    success_df = df[df['transaction_status'] == 'Success']
    
    insights = []
    
    # 1. Monthly Revenue Growth
    df['month'] = df['date'].dt.to_period('M')
    monthly_rev = success_df.groupby(df['date'].dt.to_period('M'))['amount'].sum()
    if len(monthly_rev) >= 2:
        last_month = monthly_rev.iloc[-1]
        prev_month = monthly_rev.iloc[-2]
        growth = ((last_month - prev_month) / prev_month) * 100
        direction = "increased" if growth > 0 else "decreased"
        insights.append(f"Revenue {direction} by {abs(growth):.1f}% compared to the previous month.")
    
    # 2. UPI Contribution
    upi_success = len(success_df[success_df['payment_method'] == 'UPI'])
    total_success = len(success_df)
    upi_pct = (upi_success / total_success) * 100
    insights.append(f"UPI contributed {upi_pct:.1f}% of all successful transactions.")
    
    # 3. Top Merchant
    top_merchant = success_df.groupby('merchant_name')['amount'].sum().idxmax()
    top_merchant_rev = success_df.groupby('merchant_name')['amount'].sum().max()
    insights.append(f"Merchant '{top_merchant}' generated the highest revenue (INR {top_merchant_rev:,.2f}).")
    
    # 4. Success Rate
    success_rate = (len(success_df) / len(df)) * 100
    insights.append(f"The overall transaction success rate is {success_rate:.1f}%.")
    
    return insights

def llm_prompt_structure(insights):
    prompt = f"""
    Act as a Senior Data Analyst at Razorpay. 
    Analyze the following business insights and provide a 3-sentence executive summary for the CFO.
    
    Insights:
    {chr(10).join(['- ' + i for i in insights])}
    
    Format:
    1. Financial Health Overview
    2. Key Driver Identification
    3. Actionable Recommendation
    """
    return prompt

if __name__ == "__main__":
    business_insights = generate_business_insights('data/transactions_cleaned.csv')
    
    print("--- Automated Business Insights ---")
    for insight in business_insights:
        print(f"DEBUG: {insight}")
        
    print("\n--- LLM-Ready Prompt ---")
    print(llm_prompt_structure(business_insights))
    
    # Save insights to a file
    with open('docs/business_insights.txt', 'w') as f:
        f.write("Automated Business Insights:\n")
        for i in business_insights:
            f.write(f"- {i}\n")
        f.write("\nLLM Prompt Structure:\n")
        f.write(llm_prompt_structure(business_insights))
