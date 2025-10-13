import sqlite3
import pandas as pd
import os

db_path = os.path.join(os.path.dirname(__file__), '../data/hr_analyticsdata.db')

def run_query(query):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# -----------------------------
# Queries
# -----------------------------

def attrition_rate_by_department():
    """Attrition rate (%) per department"""
    query = """
    SELECT Department,
           ROUND(100.0 * SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS AttritionRate
    FROM employees
    GROUP BY Department
    ORDER BY AttritionRate DESC;
    """
    return run_query(query)

def average_income_by_jobrole():
    """Average monthly income per job role"""
    query = """
    SELECT Role,
           ROUND(AVG(Salary), 2) AS AvgIncome
    FROM employees
    GROUP BY Role
    ORDER BY AvgIncome DESC;
    """
    return run_query(query)

def performance_by_years_at_company():
    """Average performance rating by years at company"""
    query = """
    SELECT YearsAtCompany,
           ROUND(AVG(PerformanceScore), 2) AS AvgPerformance
    FROM employees
    GROUP BY YearsAtCompany
    ORDER BY YearsAtCompany;
    """
    return run_query(query)

def satisfaction_by_department():
    """Average job satisfaction per department"""
    query = """
    SELECT Department,
           ROUND(AVG(SatisfactionLevel), 2) AS AvgSatisfaction
    FROM employees
    GROUP BY Department
    ORDER BY AvgSatisfaction DESC;
    """
    return run_query(query)

def age_distribution():
    """Age distribution of employees"""
    query = """
    SELECT Age,
           COUNT(*) AS NumEmployees
    FROM employees
    GROUP BY Age
    ORDER BY Age;
    """
    return run_query(query)

def income_vs_performance():
    """Monthly income and performance rating for correlation analysis"""
    query = """
    SELECT Salary, PerformanceScore
    FROM employees;
    """
    return run_query(query)
