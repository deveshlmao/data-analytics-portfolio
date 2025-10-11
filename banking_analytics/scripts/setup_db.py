import sqlite3
import pandas as pd

def create_database(csv_path="data/transactions.csv", db_path="banking_data.db"):
    df = pd.read_csv(csv_path)
    conn = sqlite3.connect(db_path)
    df.to_sql("transactions", conn, if_exists="replace", index=False)
    conn.commit()
    conn.close()
    print(f"Database created at {db_path} with data from {csv_path}")
    

if __name__ == "__main__":
    create_database()
    
    