# wap in python to read csv file using pandas.
import pandas as pd
DF = pd.read_csv("tips.csv")
print(DF)
print(DF.describe())
print(DF["total_bill"].value_counts())

 