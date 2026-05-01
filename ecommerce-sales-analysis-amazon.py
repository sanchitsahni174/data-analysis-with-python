# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 20:57:07 2025

Questions  to be answered

-How many sales have they made with amounts more than 1000
-How many sales have they made that belong to the category "Tops"" and have a quantity of 3
-The total sales by category
-Average Amount by category and status
-Total Sales by Fulfilment and shipment Type

@author: aress
"""


import pandas as pd

#Load the sales data from the excel file into a oandsas Dataframe

sales_data = pd.read_excel('sales_data.xlsx')

# =============================================================================
# # Exploring Data
# =============================================================================
#get summary of sales data

sales_data.info() #can also check data types

sales_data.describe()

#looking at columns
print(sales_data.columns)

#having a look at the first few rows of data
print(sales_data.head())

#check the data types

print(sales_data.dtypes)

# =============================================================================
# Cleaning Data
# =============================================================================

#check for missing values in our sales data
print(sales_data.isnull().sum())
 
#drop any rows that has any missing  values
sales_data_dropped = sales_data.dropna()

#drop rows with missing amounts based on the amount column
sales_data_cleaned = sales_data.dropna(subset = ["Amount"])

print(sales_data_cleaned.isnull().sum())

# =============================================================================
# SLicing and Filtering Data
# =============================================================================

#select a subset of our data based on the category column
category_data= sales_data[sales_data['Category'] == 'Top']
print (category_data)

#select a subset of our data where the amount is > 1000
high_amount_data = sales_data[sales_data['Amount']> 1000]
print(high_amount_data)

#select a subset of data based on multiple conditions

filtered_data = sales_data[(sales_data['Category'] == 'Top') & (sales_data['Qty'] == 3)]
print(filtered_data)

# =============================================================================
# Aggregating Data
# =============================================================================
                           
#Total sales by category
category_totals = sales_data.groupby('Category')['Amount'] .sum ()
category_totals = sales_data.groupby('Category', as_index= False )['Amount'] .sum()
category_totals =category_totals.sort_values('Amount', ascending =False)

# Calculate Average Amount by category and fulfilment
fulfilment_averages = sales_data.groupby(['Category','Fulfilment'])['Amount'].mean()
fulfilment_averages = sales_data.groupby(['Category','Fulfilment'] ,as_index =False)['Amount'].mean()
fulfilment_averages =fulfilment_averages.sort_values('Amount' , ascending=False)

# Calculate Average Amount by category and status

status_averages= sales_data.groupby(['Category','Status']) ['Amount'].mean()
status_averages= sales_data.groupby(['Category','Status'], as_index =False) ['Amount'].mean()
status_averages=status_averages.sort_values('Amount' , ascending= False)

#Total Sales by Fulfilment and shipment Type

Total_sales_Shipandfull= sales_data.groupby(['Courier Status','Fulfilment'], as_index =False) ['Amount'].sum()
Total_sales_Shipandfull=Total_sales_Shipandfull.sort_values('Amount' , ascending= False)
Total_sales_Shipandfull.rename(columns={'Courier Status': 'Shipment'} , inplace =True)

# =============================================================================
# Exporting the Data
# =============================================================================

status_averages.to_excel('Average_sales_by_Category&status.xlsx' , index=False)
Total_sales_Shipandfull.to_excel('Total_Sales_by_ship&fulfill.xlsx', index= False)

































































