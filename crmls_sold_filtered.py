import pandas as pd
import os
 
# Load data 
sold = pd.read_csv("data/residential_sold.csv")
 
# Check property categories before filtering 
print("Unique property types and their counts:")
print(sold['PropertyType'].value_counts(dropna=False))
 
# Filter residential 
print("Before filter: {len(sold)} rows")
sold = sold[sold['PropertyType'] == 'Residential']
print(f"After filter: {len(sold)} rows — kept only PropertyType == 'Residential'")
 
# Null-count summary table
print("Null-count summary:")
print(sold.isnull().sum())
 
# Save null-count summary
null_summary = sold.isnull().sum().reset_index()
null_summary.columns = ['Column', 'MissingCount']
null_summary.to_csv("crmls_sold_filtered/null_count_summary.csv", index=False)
 
# Missing value report (columns above 90% null) 
missing = sold.isnull().sum() / len(sold)
flagged = missing[missing > 0.90]
print("Columns with >90% missing values:")
print(flagged)
 
# Save flagged columns report
flagged.to_csv("crmls_sold_filtered/missing_value_report.csv")

 
#Numeric distribution summary 
cols = ['ClosePrice', 'LivingArea', 'DaysOnMarket']
summary = sold[cols].describe(percentiles=[.10, .25, .50, .75, .90, .95, .99])
print("Numeric distribution summary:")
print(summary)
 
# Save distribution summary
summary.to_csv("crmls_sold_filtered/numeric_distribution_summary.csv")

 
# Save filtered dataset 
sold.to_csv("crmls_sold_filtered/residential_sold_filtered.csv", index=False)
print(f"Final shape: {sold.shape[0]:,} rows × {sold.shape[1]} columns")