import sqlite3 
import pandas as pd 
import os 

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/financials.db')

def run_query(query):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df 

def total_revenue_by_department():
    query = """
    SELECT department, SUM(revenue) AS total_revenue,
    SUM(expenses) AS total_expenses,
    SUM(profit) AS total_profit
    FROM financials
    GROUP BY department
    ORDER BY total_revenue DESC;"""
    
    return run_query(query)

def monthly_profit_trend():
    query = """
    SELECT strftime('%Y-%m', date) AS month,
    SUM(profit) AS total_profit
    FROM financials
    GROUP BY month
    ORDER BY month;
    """
    
    return run_query(query)

def avg_profit_margin_by_department():
    query = """
    SELECT department, 
    ROUND(AVG(profit / revenue * 100),  2) AS avg_profit_margin
    FROM financials
    GROUP BY department
    ORDER BY avg_profit_margin DESC;
    """
    
    return run_query(query)

def yearly_financial_summary():
    query = """
    SELECT strftime('%Y', date) AS year, 
    SUM(revenue) AS total_revenue,
    SUM(expenses) AS total_expenses,
    SUM(profit) AS total_profit
    FROM financials
    GROUP BY year 
    ORDER BY year DESC;
    """
    
    return run_query(query)

def top_months_by_profit(limit=5):
    query = f"""
    SELECT strftime('%Y-%m', date) as month,
    SUM(profit) AS total_profit
    FROM financials
    GROUP BY month
    ORDER BY total_profit DESC
    LIMIT {limit};
    """
    
    return run_query(query)