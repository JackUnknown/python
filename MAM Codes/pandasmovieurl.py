import pandas as pd
#if data doesnt have header use "header=None"
df=pd.read_table('http://bit.ly/movieusers',sep="|",header=None)
df.info()
df.columns=['userid','age','gender','profile','views']

df['views'].replace(to_replace='[a-zA-Z]{1,}', regex=True, value=0,inplace=True)
df['views1']=df['views'].astype(int);
df.views1.mean()

df['profile'].unique()
#OR
index=pd.unique(df['profile'])

df1=pd.value_counts(df['profile'])
print(df1)

import matplotlib.pyplot as plt
plt.pie(df1,labels=df1.index, shadow=True,startangle=90,rotatelabels = 270 )

plt.bar(df1.index, df1)
plt.xticks(rotation=90)
