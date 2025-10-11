from analysis import (plot_avg_profit_margin_by_category, plot_avg_profit_margin_by_category, plot_monthly_sales_trend,
                      plot_top_product_categories, plot_top_sales_reps, plot_total_sales_by_region,
                      print_summary_insights)

def main():
    
    # Print insights
    print("Starting sales data analysis... \n")
    print_summary_insights()
    
    #Visualizations
    print('Generating visualizations... \n')
    plot_total_sales_by_region()
    plot_top_product_categories()
    plot_monthly_sales_trend()
    plot_top_sales_reps()
    plot_avg_profit_margin_by_category()
    
    print("Analysis complete. Visualizations saved as PNG files.")
    
if __name__ == '__main__':
    main()