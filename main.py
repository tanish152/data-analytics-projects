import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("data1.csv")
print(df.head(5))
print(df.columns)
print(df.describe())
df.info()
df.isnull().sum()

df = df.drop("Unnamed: 0", axis=1)
print(df.head(5))

#  gender distribution
plt.figure(figsize=(5,5))
ax=sns.countplot(data=df,x="Gender")
ax.bar_label(ax.containers[0])
plt.show()

# from the above  chart we have analyzed that the number of females 
# in the data is more than the numbers of males


gb=df.groupby('ParentEduc').agg({"MathScore":np.mean,"ReadingScore":np.mean,"WritingScore":np.mean})
print(gb)

sns.heatmap(gb,annot=True)
plt.show()

gb1=df.groupby("ParentMartialStatus").agg({"MathScore":np.mean,"ReadingScore":np.mean,"WritingScore":np.mean})
print(gb1)

sns.heatmap(gb1,annot=True)
plt.show()


sns .boxplot(data=df,x="MathScore")
plt.show()
