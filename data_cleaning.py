# This file is using data wrangling technique to handle missing data in the dataset file
import pandas as pd

# import the original csv file and load it to a data frame
dataFrame_data = pd.read_csv('example_batch_records.csv',encoding = 'utf-8')

# fill missing data in column "nodes_used"  by using the mean value of the column and keep the column's data type as Integer
dataFrame_data['nodes_used'].fillna(value = dataFrame_data['nodes_used'].mean(), inplace=True)
dataFrame_data['nodes_used'] = dataFrame_data['nodes_used'].astype(int)

# fill missing data in column "submitted_at" by using forward fill technique
dataFrame_data['submitted_at'] = pd.to_datetime(dataFrame_data['submitted_at'])
dataFrame_data = dataFrame_data.sort_values(by = 'submitted_at')
dataFrame_data['submitted_at'] = dataFrame_data['submitted_at'].fillna(method='ffill')
# saving the updated version of the dataset (after filling missing data) into another csv file called "filled_data.csv"
dataFrame_data.to_csv('filled_file.csv', index=False)

