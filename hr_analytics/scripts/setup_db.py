import sqlite3 
import pandas as pd 
import os 

data_path = os.path.join(os.path.dirname(__file__), '../data/hr_analytics_data.csv')
db_path = os.path.join(os.path.dirname(__file__), '../data/hr_analyticsdata.db')

df = pd.read_csv(data_path)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

df.to_sql('employees', conn, if_exists='replace', index =False)

conn.commit()
conn.close()