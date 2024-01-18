# # Scatter Plot using Matplotlib Plot
# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("tips.csv")
# plt.scatter(df['day'],df['tip'])
# plt.title("Scatter_Plot")

# plt.xlabel('Day')
# plt.ylabel('Tip')
# plt.show()

# ----------------------------------------------------------------

# # Q. Barplot
# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.read_csv("tips.csv")

# plt.bar(df['day'],df['tip'])

# plt.title('Bar_Chart')

# plt.xlabel('Day')
# plt.ylabel('Tip')

# plt.show()

# ----------------------------------------------------------------
# # Q. Histogram plot
# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("tips.csv")

# plt.hist(df['total_bill'])
# plt.title('Histogram')
# plt.show()

# ----------------------------------------------------------------
# Q. Line Plot

# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("tips.csv")

# plt.plot(df['total_bill'],df['tip'])
# plt.title("Line Plot")
# plt.show()
