import pandas as pd

# Load dataset
df = pd.read_csv("online_sales_dataset.csv")

print("First 5 rows")
print(df.head())

print("\nDataset Info")
print(df.info())

print("\nSummary")
print(df.describe())

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Convert InvoiceDate column
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Create Total Sales column
df["TotalSales"] = df["Quantity"] * df["UnitPrice"]

# Extract month
df["Month"] = df["InvoiceDate"].dt.month

# Save cleaned dataset
df.to_csv("cleaned_sales_data.csv", index=False)

print("\nCleaning Complete ✅")