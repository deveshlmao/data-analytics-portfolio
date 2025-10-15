import pandas as pd 
import os 
import sqlite3 
from queries import (total_revenue_by_department, monthly_profit_trend,
                     avg_profit_margin_by_department, yearly_financial_summary,
                     top_months_by_profit)
import matplotlib.pyplot as plt
import seaborn as sns

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/financials.db')


def plot_total_revenue_by_department():
    df = total_revenue_by_department()
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='department', y='total_revenue', palette='rocket')
    plt.title('Total Revenue By Department')
    plt.xlabel('Department')
    plt.ylabel('Total Revenue')
    plt.savefig('total_revenue_by_department.png')
    plt.tight_layout()
    plt.show()
    

def plot_monthly_profit_trend():
    df = monthly_profit_trend()
    plt.figure(figsize=(16, 8))
    sns.lineplot(data=df, x='month', y='total_profit', marker='o', linestyle='-', color='b')
    plt.title('Monthly Profit Trend (2022-2024)')
    plt.xlabel('Month')
    plt.ylabel("Total Profit")
    plt.savefig('monthly_profit_trend.png')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(rotation=45, ha='right')
    steps = max(len(df) // 12, 1)
    plt.xticks(df['month'][::steps])
    plt.show()
    
def plot_avg_profit_margin_by_department():
    df = avg_profit_margin_by_department()
    plt.figure(figsize=(10,6))
    sns.barplot(data=df, x='department', y='avg_profit_margin', palette='viridis')
    plt.title('Average Profit Margin By Department')
    plt.xlabel('Department')
    plt.ylabel('Average Profit Margin (%)')
    plt.tight_layout()
    plt.savefig('avg_profit_margin_by_department.png')
    plt.show()
    
def plot_yearly_financial_summary():
    df = yearly_financial_summary()
    df_melted = df.melt(id_vars='year', value_vars=['total_revenue', 'total_expenses', 'total_profit'])
    sns.set_palette('Set2')
    plt.figure(figsize=(12,6))
    sns.barplot(data=df_melted, x='year', y='value', hue='variable')
    plt.title('Yearly Financial Summary')
    plt.xlabel('Year')
    plt.ylabel('Amount')
    plt.legend(title='Metric')
    plt.tight_layout()
    plt.savefig('yearly_financial_summary.png')
    plt.show()
    
    
def plot_top_months_by_profit(limit=5):
    df = top_months_by_profit(limit)
    plt.figure(figsize=(10,6))
    sns.barplot(data=df, x='month', y='total_profit', palette='mako')
    plt.title(f'Top {limit} Months By Profit')
    plt.xlabel('Month')
    plt.ylabel('Total Profit')
    plt.tight_layout()
    plt.savefig('top_months_by_profit.png')
    plt.show()
    