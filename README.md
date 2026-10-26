# Payment Analytics & Business Finance Dashboard 🚀

## 📊 Project Overview
This project is an end-to-end fintech analytics solution built to analyze digital payment transactions and provide actionable business insights through SQL, Power BI, Python, and AI-powered reporting.

The dashboard simulates a fintech environment similar to a payment gateway platform (like **Razorpay**) where thousands of transactions are processed daily through UPI, Cards, Wallets, and Net Banking.

---

## 💼 Business Problem
Finance teams often rely on manual reports that delay decision-making and increase the risk of data inconsistencies. This project addresses these challenges by:
- **Automating KPI reporting**: Real-time tracking of revenue and volume.
- **Monitoring transaction health**: Identifying success/failure bottlenecks.
- **Analyzing merchant performance**: Benchmarking top-performing businesses.
- **AI-Powered Insights**: Automating executive summaries for rapid decision-making.

---

## 🛠️ Tech Stack
- **SQL**: MySQL / PostgreSQL (Advanced Queries, Window Functions, CTEs)
- **Python**: Pandas, NumPy, Matplotlib, Seaborn (Data Cleaning, EDA, AI Insights)
- **BI Tool**: Power BI (Executive Dashboard, DAX Measures)
- **AI**: LLM-based Insight Generation (Prompt Engineering)

---

## 📂 Project Structure
```text
├── data/                   # Raw and cleaned datasets (CSV)
├── sql/                    # SQL Schema and Analytical Queries
├── python/                 # Data cleaning, EDA, and AI insights scripts
├── powerbi/                # Dashboard specifications and DAX measures
├── docs/                   # Data dictionary and business insights
├── README.md               # Project documentation
└── .gitignore              # Files to ignore in Git
```

---

## 📈 Key Performance Indicators (KPIs)
- **Total Revenue**: Sum of successful transaction amounts.
- **Total Transactions**: Total count of transaction attempts.
- **Success Rate**: Percentage of successful transactions vs total attempts.
- **Failure Rate**: Percentage of failed transactions.
- **Average Transaction Value (ATV)**: Average amount per successful transaction.

---

## 🚀 Key Deliverables

### 1. SQL Data Analysis
- **Schema Design**: Normalized database structure for fintech transactions.
- **Advanced Queries**: Used CTEs, Window Functions, and Joins to extract business-critical metrics like monthly growth and success rates.
- [View SQL Scripts](sql/)

### 2. Python Data Cleaning & EDA
- **Preprocessing**: Handled missing values, duplicates, and date normalization.
- **Exploratory Analysis**: Automated calculation of business KPIs.
- [View Python Scripts](python/)

### 3. Power BI Dashboard
- **Executive Overview**: High-level KPIs and revenue trends.
- **Transaction Analytics**: Deep dive into success vs failure across states and devices.
- **Merchant Performance**: Revenue contribution and success rate benchmarking.
- [View Dashboard Spec](powerbi/dashboard_spec.md)

### 4. AI-Powered Insight Generator
- Developed a Python workflow that generates automated business insights and LLM-ready prompts for executive summaries.
- [View AI Insights](docs/business_insights.txt)

---


---

## 📜 How to Run
1. Clone the repository.
2. Run `python python/generate_data.py` to create the dataset.
3. Run `python python/data_cleaning.py` to clean and analyze the data.
4. Execute SQL scripts in `sql/` on your local database.
5. Use `powerbi/dashboard_spec.md` to recreate the visuals in Power BI.

---

**Developed by [Pradnya Hiremath]**  
