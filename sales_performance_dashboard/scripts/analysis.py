import pandas as pd
import sqlite3
import os 
import matplotlib.pyplot as plt
import seaborn as sns
from queries import (total_sales_by_region, top_product_categories, 
                     monthly_sales_trend, top_sales_reps, avg_profit_margin_by_category)

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/sales_data.db')

sns.set_theme(style="whitegrid")

def plot_total_sales_by_region():
    df = total_sales_by_region()
    plt.figure(figsize=(8, 5))
    sns.barplot(x="region", y="total_sales", data=df)
    plt.title("Total Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Total Sales ($)")
    plt.tight_layout()
    plt.savefig( 'sales_by_region.png')
    plt.show()

    
def plot_top_product_categories():
    df = top_product_categories()
    plt.figure(figsize=(8,5))
    sns.barplot(data=df, x='product_category', y='total_sales', palette='mako')
    plt.title('Top Product Categories By Sales')
    plt.xlabel('Product Category')
    plt.ylabel('Total Sales ($)')
    plt.tight_layout()
    plt.savefig('top_product_categories.png')
    plt.show()
    
def plot_monthly_sales_trend():
    df = monthly_sales_trend()
    plt.figure(figsize=(10,5))
    plt.plot(df['month'], df['total_sales'], marker='o', label='Sales')
    plt.plot(df['month'], df['total_profit'], marker='o', label="Profit")
    plt.title('Monthly Sales and Profit trend')
    plt.xlabel('Month')
    plt.ylabel('Amount ($)')
    plt.grid(True, linestyle='--', alpha=0.6)    
    plt.legend()
    plt.tight_layout()
    plt.savefig('monthly_sales_trend.png')
    plt.show()
    
def plot_top_sales_reps():
    df = top_sales_reps()
    plt.figure(figsize=(8,5))
    sns.barplot(data=df, x='sales_rep', y='total_sales', palette='mako')
    plt.title('Top Sales Representatives')
    plt.xlabel('Sales Representative')
    plt.ylabel('Total Sales ($)')
    plt.tight_layout()
    plt.savefig('top_sales_reps.png')
    plt.show()
    
def plot_avg_profit_margin_by_category():
    df = avg_profit_margin_by_category()
    plt.figure(figsize=(8,5))
    sns.barplot(data=df, x='product_category', y='avg_profit_margin', palette='rocket')
    plt.title('Average Profit Margin by Product Category')
    plt.xlabel('Product category')
    plt.ylabel('Average Profit Margin (%)')
    plt.tight_layout()
    plt.savefig('avg_profit_margin_by_category.png')
    plt.show()
    
def print_summary_insights():
    print("Summary Insights: ")
    region_df = total_sales_by_region()
    top_region = region_df.iloc[0]
    print(f"The region with the highest sales is {top_region['region']} with total sales of ${top_region['total_sales']} and total profit of ${top_region['total_profit']}")
    
    category_df = top_product_categories(limit=1)
    top_category = category_df.iloc[0]
    print(f"The top product category is {top_category['product_category']} with total sales of ${top_category['total_sales']} and total profit of ${top_category['total_profit']}")
    
    rep_df = top_sales_reps(limit=1)
    top_rep = rep_df.iloc[0]
    print(f"The top sales representative is {top_rep['sales_rep']} with total sales of ${top_rep['total_sales']} and total profit of ${top_rep['total_profit']}")
    
    margin_df = avg_profit_margin_by_category()
    top_margin_category = margin_df.iloc[0]
    print(f"The product category with the highest average profit margin is {top_margin_category['product_category']} with an average profit margin of {top_margin_category['avg_profit_margin']}%")
    
    
    
    
if __name__ == "__main__":
    print_summary_insights()