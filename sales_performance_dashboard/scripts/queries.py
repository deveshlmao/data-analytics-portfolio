import pandas as pd
import sqlite3
import os 

def run_query(query):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, '../data/sales_data.db')
    
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Queries

def total_sales_by_region():
    query = """
    SELECT region, ROUND(SUM(sales_amount), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
    from sales 
    GROUP BY region
    ORDER BY total_sales DESC;"""
    
    return run_query(query)

def top_product_categories(limit=5):
    query = f"""
    SELECT product_category, ROUND(SUM(sales_amount), 2) AS total_sales,
    ROUND(SUM(profit),2) AS total_profit
    FROM sales
    GROUP BY product_category
    ORDER BY total_sales DESC
    LIMIT {limit};
    """
    
    return run_query(query)

def monthly_sales_trend():
    query = """
    SELECT strftime('%Y-%m', date) AS month,
    ROUND(SUM(sales_amount), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
    FROM sales
    GROUP BY month
    ORDER BY month;"""
    
    return run_query(query)

def top_sales_reps(limit=5):
    query = f"""
    SELECT sales_rep, ROUND(SUM(sales_amount), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
    FROM sales
    GROUP BY sales_rep
    ORDER BY total_sales DESC
    LIMIT {limit};"""
    
    return run_query(query)

def avg_profit_margin_by_category():
    query = """
    SELECT product_category,
    ROUND(AVG((profit / sales_amount) * 100), 2) AS avg_profit_margin
    FROM sales
    WHERE sales_amount != 0
    GROUP BY product_category
    ORDER BY avg_profit_margin DESC;"""
    
    return run_query(query)

## testing

if __name__ == '__main__':
    print(avg_profit_margin_by_category(), '\n')
    print(top_sales_reps(), '\n')
    print(monthly_sales_trend(), '\n')
    print(top_product_categories(), '\n')
    print(total_sales_by_region(), '\n')