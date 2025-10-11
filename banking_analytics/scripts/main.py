import pandas as pd
import sqlite3
import analysis
from queries import top_customers, monthly_spending, spending_by_category, spending_by_city, payment_method_usage

def print_insights():
    top = top_customers()
    month = monthly_spending()
    category = spending_by_category()
    city = spending_by_city()
    payment = payment_method_usage()
    
    print('\n------ Top Customers -------')
    print(top)
    print('\n------ Top Monthly Customers -------')
    print(month)
    print('\n------ Top Customers By Category -------')
    print(category)
    print('\n------ Top Customers by City -------')
    print(city)
    print('\n------ Payment Method Usage -------')
    print(payment)

    print('\n------ Key Insights -------')
    print(f"Top Customers spent: ${top['total_spent'][0]}")
    print(f"Month with highest spending: {month.loc[month['total_spent'].idxmax(), 'Month']}")
    print(f"Most popular category: {category.iloc[0]['category']}")
    print(f"Most Popular City: {city.iloc[0]['city']}")
    print(f"Most used payment method: {payment.iloc[0]['payment_method']}")
    
def main():
    print("Running customer spending analysis.... \n")
    print_insights()
    analysis.plot_monthly_trend()
    analysis.plot_category_spending()
    analysis.plot_payment_distribution()
    print("\n Analysis check complete. Charts Saved.")
    
    
if __name__ == "__main__":
    main()
    

