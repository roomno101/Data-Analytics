# Seaborn Bar plot
# # importing packages
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

# # reading the database
# data = pd.read_csv("tips.csv")
# #pass to seaborn function
# sns.barplot(x='day',y='tip', data=data, hue='sex')
# #Visualization of data
# plt.show()
# ----------------------------------------------------------------
# seaborn histogram

# # importing packages *histogram
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

# # reading the database
# data = pd.read_csv("tips.csv")

# sns.histplot(x='total_bill', data=data, kde=True, hue='sex')

# plt.show()

# ----------------------------------------------------------------
# seaborn line plot
# importing packages 
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd


# # reading the database
# data = pd.read_csv("tips.csv")

# # draw lineplot
# sns.lineplot(x="sex", y="total_bill", data=data)

# # setting the title using Matplotlib
# plt.title('Using Matplotlib Function')

# plt.show()

# ----------------------------------------------------------------
# Seaborn Scatter Plot without hue value without colour
# # importing packages
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

# # reading the database
# data = pd.read_csv("tips.csv")

# sns.scatterplot(x='day', y='tip', data=data,)
# plt.show()

# --------------------------------------------------
# # 2. scatter plot with colour 
# importing packages
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

# # reading the database
# data = pd.read_csv("tips.csv")

# sns.scatterplot(x='day', y='tip', data=data, hue='sex')
# plt.show()

# ----------------------------------------------------------------
# seaborn lineplot with data drop
# importing packages
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd


# # reading the database
# data = pd.read_csv("tips.csv")

# # using only data attribute
# sns.lineplot(data=data.drop(['total_bill'], axis=1))
# plt.show()