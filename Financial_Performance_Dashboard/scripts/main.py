import pandas as pd 
import sqlite3 
import os 
from analysis import (plot_avg_profit_margin_by_department, plot_monthly_profit_trend,
                      plot_total_revenue_by_department, plot_yearly_financial_summary,
                      plot_top_months_by_profit)

import analysis

def print_summary_insights():
    print("Summary Insights:")
    print("-" * 50)
    df_revenue = analysis.total_revenue_by_department()
    top_dept = df_revenue.iloc[0]
    print(f"Top Department by Revenue: {top_dept['department']} with ${top_dept['total_revenue']:.2f}")
    df_profit_trend = analysis.monthly_profit_trend()
    best_month = df_profit_trend.iloc[df_profit_trend['total_profit'].idxmax()]
    print(f"Best Month by Profit: {best_month['month']} with ${best_month['total_profit']:.2f}")
    df_avg_margin = analysis.avg_profit_margin_by_department()
    best_margin_dept = df_avg_margin.iloc[0]
    print(f"Best Department by Average Profit Margin: {best_margin_dept['department']} with {best_margin_dept['avg_profit_margin']:.2f}%")
    df_yearly = analysis.yearly_financial_summary()
    best_year = df_yearly.iloc[0]
    print(f"Best Year by Profit: {best_year['year']} with ${best_year['total_profit']:.2f}")
    df_top_months = analysis.top_months_by_profit()
    print("Top 5 Months by Profit:")
    for idx, row in df_top_months.iterrows():
        print(f"  {row['month']}: ${row['total_profit']:.2f}")
    print("-" * 50)
    
    
    
if __name__ == "__main__":
    print_summary_insights()
    plot_total_revenue_by_department()
    plot_monthly_profit_trend()
    plot_avg_profit_margin_by_department()
    plot_yearly_financial_summary()
    plot_top_months_by_profit()
    print("Analysis complete and plots saved.")