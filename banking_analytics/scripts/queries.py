import sqlite3 
import pandas as pd

DB_PATH = "db/banking_data.db"

def run_query(query):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def top_customers(limit=10):
    query = f"""
    SELECT customer_id, ROUND(SUM(amount), 2) AS total_spent
    FROM transactions
    GROUP BY customer_id
    ORDER BY total_spent DESC
    LIMIT {limit};
    """
    
    return run_query(query)

def monthly_spending():
    query = """
    SELECT strftime('%Y-%m', date) AS Month,
    ROUND(SUM(amount), 2) AS total_spent
    FROM transactions
    GROUP BY Month
    ORDER BY Month;
    """
    
    return run_query(query)

def spending_by_category():
    query = """
    SELECT category, COUNT(*) AS num_transactions, ROUND(SUM(amount),2) AS total_spent
    FROM transactions
    GROUP BY category
    ORDER BY total_spent DESC;
    """
    return run_query(query)

def spending_by_city(): 
    query = """
    SELECT city, ROUND(SUM(amount), 2) as total_spent, COUNT(*) AS num_transactions
    FROM transactions
    GROUP BY city
    ORDER BY total_spent DESC;"""
    
    return run_query(query)

def payment_method_usage():
    query = """
    SELECT payment_method, COUNT(*) AS num_transactions, ROUND(SUM(amount), 2) AS total_spent
    FROM transactions
    GROUP BY payment_method
    ORDER BY total_spent DESC;
    """
    
    return run_query(query)

