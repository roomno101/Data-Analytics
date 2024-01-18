#Data Cleaning 10/11/2023

import pandas as pd
import numpy as np
df = pd.read_csv("shopping_trends.csv")[0:5]

## check null value is avilable in df or not...
# print(df.isnull())
# print(df.isnull().sum())

# #remove column from table 
# remove=['Age','Item Purchased']
# df.drop(remove,inplace=True,axis=1)
# print(df[0:2])

# # In place of null it place some values are missing and place with some other value at that place
# print(df.fillna('Nil')[0:2])
# print(df)

## check any column have duplicate value or not...
# print(df['Gender'].duplicated())

## remove duplicate values in a column...
# print(df['Gender'].drop_duplicates())

## it describe about data
# print(df.describe())

# # locate a particular value and assign a new value
# df.loc[2,'Gender'] = 'Female'
# print(df['Gender'])

## convert to lower case of a column value
# print(df['Gender'].str.lower())

# # title funtion
# print(df['Gender'].str.title())