# 🧑‍💼 Customer Data Analysis Pipeline

A complete ETL (Extract, Transform, Load) and analysis pipeline for customer data from the **AdventureWorksLT2019** SQL Server database. This project automates the extraction, cleaning, and preparation of customer records for business intelligence and marketing analytics.

---

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)

---

## ✨ Features

- **Automated Data Extraction**: Connect to SQL Server and export customer data seamlessly
- **Comprehensive Data Cleaning**: Remove duplicates, standardize formats, and handle missing values
- **Feature Engineering**: Extract email domains and create customer segments for persona analysis
- **Ready-to-Analyze Output**: Generate clean CSV files optimized for BI tools and statistical analysis
- **Jupyter Notebook Analysis**: Interactive exploration and visualization of customer data

---

## 📁 Project Structure

├── main.py # Data extraction script (SQL Server → CSV)
├── Analysis.ipynb # Data cleaning and analysis notebook
├── customers_export.csv # Raw data exported from database
├── cleaned_customers.csv # Intermediate cleaned dataset
├── customers_analysis_ready.csv # Final analysis-ready dataset
├── requierment.txt 
└── README.md # Project documentation

## 🔧 Prerequisites

Python 3.7+
SQL Server with AdventureWorksLT2019 database
### Required Python Libraries:
pandas - Data manipulation and CSV handling
pyodbc - SQL Server connectivity
numpy - Numerical operations
matplotlib - Data visualization
seaborn - Statistical plotting
