# Task 1 – Data Immersion & Wrangling

## ApexPlanet Data Analytics Internship

### Objective
The objective of this task is to understand, clean, and prepare a dataset for analysis. This includes exploring the dataset, identifying data quality issues, performing data cleaning, and transforming the data into an analysis-ready format.

---

## Dataset
Dataset used: Online Sales Dataset

The dataset contains sales transactions including product details, quantities, pricing, shipping information, and order details.

---

## Dataset Columns
- InvoiceNo – Unique invoice number
- StockCode – Product code
- Description – Product description
- Quantity – Number of items sold
- InvoiceDate – Date of transaction
- UnitPrice – Price per unit
- CustomerID – Customer identifier
- Country – Customer location
- Discount – Discount applied
- PaymentMethod – Payment method used
- ShippingCost – Shipping charges
- Category – Product category
- SalesChannel – Online or In-store sales
- ReturnStatus – Returned or not
- ShipmentProvider – Shipping company
- WarehouseLocation – Warehouse location
- OrderPriority – Order priority

---

## Steps Performed

### 1. Data Loading
Loaded dataset using Python Pandas.

### 2. Data Exploration
Explored dataset using:
- head()
- info()
- describe()

### 3. Data Quality Check
Checked for:
- Missing values
- Duplicate rows
- Incorrect data types

### 4. Data Cleaning
Performed:
- Removed duplicates
- Converted InvoiceDate to datetime format

### 5. Feature Engineering
Created new columns:
- TotalSales = Quantity × UnitPrice
- Month extracted from InvoiceDate

### 6. Export Clean Dataset
Saved cleaned dataset as:
cleaned_sales_data.csv

---

## Technologies Used
- Python
- Pandas
- GitHub

---

## Files in Repository
- data_cleaning.py
- online_sales_dataset.csv
- cleaned_sales_data.csv
- data_dictionary.md
- README.md

---

## Outcome
The dataset was successfully cleaned and prepared for further analysis and visualization.

---

## Author
Abhishek Sonpethkar  
ApexPlanet Data Analytics Internship
