import sqlite3 
import pandas as pd

df = pd.read_csv('data/sales_data.csv')

conn = sqlite3.connect('data/sales_data.db')
cursor = conn.cursor()

df.to_sql('sales', conn, if_exists='replace', index=False)

conn.commit()
conn.close()