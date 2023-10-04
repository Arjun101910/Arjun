import pandas as pd
data ={ 'A':[2 , 3 , 1 , 4,5],'B':[3,  1,   2 , 4,5]}
df=pd.DataFrame(data)
correlation_matrix=df.corr()
print(correlation_matrix)
correlation_AB = df['A'].corr(df['B'])
print(correlation_AB)
import seaborn as sns
import matplotlib.pyplot as plt

# Using the same dataframe and correlation_matrix from above
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)

plt.show()
