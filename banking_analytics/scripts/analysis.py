import sqlite3 
import pandas as pd
from queries import top_customers, payment_method_usage, spending_by_category, spending_by_city, monthly_spending
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

def plot_monthly_trend():
    df = monthly_spending()
    plt.figure(figsize=(10,5))
    sns.lineplot(data = df, x='Month', y="total_spent", marker='o')
    plt.title("Monthly Customer SPending")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("monthly_spending.png")
    plt.show()
    
def plot_category_spending():
    df = spending_by_category()
    plt.figure(figsize=(8,5))
    sns.barplot(data=df, x='total_spent', y='category')
    plt.title("Total spending by category")
    plt.tight_layout()
    plt.savefig('category_spending.png')
    plt.show()
    
def plot_payment_distribution():
    df = payment_method_usage()
    plt.figure(figsize=(6,6))
    plt.pie(df['num_transactions'], labels = df['payment_method'], autopct='%1.1f%%', startangle=140)
    plt.title("Payment Method Distribution")
    plt.tight_layout()
    plt.savefig('payment_method_distribution.png')
    plt.show()
    
    