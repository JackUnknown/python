#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



import seaborn as sns
# Load the data

tips = sns.load_dataset("tips")
print(tips.shape)
#x=tips["total_bill"]
# Create violinplot

sns.violinplot(x = "total_bill", data=tips)
# Show the plot

plt.show()


print(tips['sex'].value_counts())
x = tips['sex'].value_counts().index
y = tips['sex'].value_counts()
plt.bar(x,y)
plt.show()

# OR

sns.countplot(x="sex",data=tips)

sns.countplot(x="smoker",data=tips)
sns.countplot(x="smoker",hue = 'sex' ,data=tips)

sns.countplot(x="time", data=tips)
sns.countplot(x="time",hue = 'sex', data=tips)

sns.countplot(x="day",data=tips)
sns.countplot(x="day",hue = 'sex',data=tips)



sns.boxplot(x="day",y="total_bill",data=tips)

sns.distplot(tips["total_bill"],kde=True,bins=20,color="darkgreen")

sns.set(style="darkgrid")
sns.histplot(x="total_bill",data=tips,bins=10)






