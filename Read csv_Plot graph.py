# wap in python to read csv file using pandas and plot graph using matplotlib 
import pandas as pd
import matplotlib.pyplot as plt
DF = pd.read_csv("tips.csv")
DF.plot(x="tip", y="size", kind="line", figsize=(6, 8))
plt.show()