import matplotlib.pyplot as plt
import seaborn as sns
from queries import (attrition_rate_by_department, average_income_by_jobrole,
                     performance_by_years_at_company, satisfaction_by_department,
                     age_distribution, income_vs_performance)



sns.set_theme(style='whitegrid')

def plot_attrition_rate_by_department():
    df = attrition_rate_by_department()
    plt.figure(figsize=(10,6))
    sns.barplot(data=df, x='Department', y='AttritionRate', palette='mako')
    plt.title(' Attrition Rate By Department')
    plt.ylabel('Attrition Rate (%)')
    plt.xlabel('Department')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('attrion_rate_by_department.png')
    plt.show()
    
def plot_average_income_by_jobrole():
    df = average_income_by_jobrole()
    plt.figure(figsize=(10,6))
    sns.barplot(data=df, x='Role', y='AvgIncome', palette='rocket')
    plt.title('Average Income by Job Role')
    plt.ylabel('Average Monthly Income')
    plt.xlabel('Job Role')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('average_income_by_jobrole.png')
    
    plt.show()
    
def plot_performance_by_years_at_company():
    df = performance_by_years_at_company()
    plt.figure(figsize=(10,6))
    sns.lineplot(data=df, x='YearsAtCompany', y='AvgPerformance', marker='o')
    plt.title('Average Performance by Years at Company')
    plt.ylabel('Average Performance Rating')
    plt.xlabel('Years at Company')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('performance_by_years_at_company.png')
    plt.show()
    
def plot_satisfication_by_department():
    df = satisfaction_by_department()
    plt.figure(figsize=(10,6))
    sns.barplot(data=df, x='Department', y='AvgSatisfaction')
    plt.title('Average Job Satisfaction By Department')
    plt.ylabel('Average Job Satisfaction')
    plt.xlabel('Department')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('satisfaction_by_department.png')
    plt.show()
    
def plot_age_distribution():
    df = age_distribution()
    plt.figure(figsize=(10,6))
    sns.barplot(data=df, x='Age', y='NumEmployees', palette='magma')
    plt.title('Age Distribution of Employees')
    plt.ylabel('Number of Employees')
    plt.xlabel('Age')
    plt.tight_layout()
    plt.savefig('age_distribution.png')
    plt.show()
    
def plot_income_vs_performance():
    df = income_vs_performance()
    plt.figure(figsize=(10,6))
    sns.scatterplot(data=df, x='Salary', y='PerformanceScore', hue='PerformanceScore', palette='viridis', s=60)
    plt.title('Income vs Performance Rating')
    plt.ylabel('Performance Rating')
    plt.xlabel('Monthly Income')
    plt.tight_layout()
    plt.savefig('income_vs_performance.png')
    plt.show()
    

def print_summary_insights():
    print("Summary Insights: \n")
    
    df = attrition_rate_by_department()
    top_attrition = df.iloc[0]
    print(f"Highest Attrition Rate: {top_attrition['Department'] } at {top_attrition['AttritionRate']}%")
    
    df = average_income_by_jobrole()
    top_income = df.iloc[0]
    print(f"Highest Average Income: {top_income['Role']} at ${top_income['AvgIncome']}")
    
    df = performance_by_years_at_company()

    # Peak performance (maximum)
    peak_perf = df.loc[df['AvgPerformance'].idxmax()]
    print(f"Peak average performance rating ({peak_perf['AvgPerformance']}) occurs at {peak_perf['YearsAtCompany']} years at the company.")

        # Performance of long-tenured employees
    long_tenured_perf = df.iloc[-1]
    print(f"Performance rating of long-tenured employees ({long_tenured_perf['AvgPerformance']}) with {long_tenured_perf['YearsAtCompany']} years at the company.")

    
    df = satisfaction_by_department()
    top_satisfaction = df.iloc[0]
    print(f"Highest Job Satisfaction: {top_satisfaction['Department']} with an average satisfaction of {top_satisfaction['AvgSatisfaction']} ")
    
    df = age_distribution()
    most_common_age = df.iloc[df['NumEmployees'].idxmax()]
    print(f"Most Common Age: {most_common_age['Age']} with {most_common_age['NumEmployees']} employees.")
    
    
def main():
    plot_attrition_rate_by_department()
    plot_average_income_by_jobrole()
    plot_performance_by_years_at_company()
    plot_satisfication_by_department()
    plot_age_distribution()
    plot_income_vs_performance()
    print_summary_insights()
    
if __name__ == "__main__":
    main()