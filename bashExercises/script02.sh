#!/bin/bash

python - <<END
import pandas as pd

# Make a data frame from .csv file

# filename = input('Enter CSV path : ')
# execs = pd.read_csv(filename)

execs = pd.read_csv('executions.csv')

# Get the dates for orders
execs['CreateTime'] = str(execs['CreateTime'])[6:17]

# Only get what you need to make seperate dataframes so that math can be done
total_execs = (execs.groupby('OrderId').sum()).reset_index()
total_execs = total_execs.iloc[:, [0, 2]]
avg_price = execs.iloc[:, [1, 6]]
avg_price = (avg_price.groupby('OrderId').mean()).reset_index()

# merge the two datasets
avg_price = avg_price.merge(total_execs, how='inner')

# Delete irrelevant
del execs['Id']
del execs['ExecQty']
del execs['ExecPrice']

# Merge with all data
avg_price = avg_price.merge(execs, how="inner")
avg_price = avg_price.drop_duplicates()
print(avg_price)
END



