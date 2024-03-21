import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('titanic.csv')
#print(df.head())



# Data Inspection and Exploration
#print(df.duplicated())


#print(df.info())


# Check the Categorical and Numerical Columns.
# Categorical columns
cat_col = [col for col in df.columns if df[col].dtype == 'object']
print('Categorical columns :',cat_col)
# Numerical columns
num_col = [col for col in df.columns if df[col].dtype != 'object']
#print('Numerical columns :',num_col)


#Check the total number of Unique Values in the Categorical Columns
#print(df[cat_col].nunique())

# Removing all the unwanted data
#print(df['Ticket'].unique()[:50])

# Drop name and ticket column
df1 = df.drop(columns=['Name','Ticket'])
print(df1.shape)
