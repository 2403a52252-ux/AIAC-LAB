import pandas as pd
import numpy as np
# Read the sales dataset
sales_data = pd.read_csv('sales_data.csv')
# Display initial information about the dataset
print("Initial Dataset Info:")
print(sales_data.info())
print("\nMissing Values:")
print(sales_data.isnull().sum())
# Handle missing values
# Fill numeric columns with mean
numeric_columns = sales_data.select_dtypes(include=[np.number]).columns
sales_data[numeric_columns] = sales_data[numeric_columns].fillna(sales_data[numeric_columns].mean())
# Fill categorical columns with mode
categorical_columns = sales_data.select_dtypes(include=['object']).columns
sales_data[categorical_columns] = sales_data[categorical_columns].fillna(sales_data[categorical_columns].mode().iloc[0])
print("\nAfter handling missing values:")
print(sales_data.isnull().sum())
# Manual Min-Max scaling
def min_max_scale(x):
    return (x - x.min()) / (x.max() - x.min())
# Manual Standard scaling
def standard_scale(x):
    return (x - x.mean()) / x.std()
# Apply normalizations
sales_data['transaction_amount_minmax'] = min_max_scale(sales_data['transaction_amount'])
sales_data['transaction_amount_standard'] = standard_scale(sales_data['transaction_amount'])
# Display the first few rows of the processed dataset
print("\nProcessed Dataset (First 5 rows):")
print(sales_data.head())
# Save the cleaned and normalized dataset
sales_data.to_csv('cleaned_sales_data.csv', index=False)
print("\nCleaned and normalized dataset has been saved to 'cleaned_sales_data.csv'")
# Display summary statistics of original and normalized columns
print("\nSummary Statistics:")
print(sales_data[['transaction_amount', 'transaction_amount_minmax', 'transaction_amount_standard']].describe())