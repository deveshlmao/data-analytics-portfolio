import sqlite3
import os 
import pandas as pd 

df = pd.read_csv('data/financials_data.csv')

conn = sqlite3.connect('data/financials.db')

df.to_sql('financials', conn, if_exists='replace', index=False)
conn.commit()
conn.close()


if __name__ == "__main__":
    print("Database setup complete and data inserted.")
    