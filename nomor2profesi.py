import pandas as pd
import numpy as np

df = pd.read_csv('profesi.csv',delimiter='|')


a = df['occupation'].value_counts()
print(len(a))
print(a.index.tolist())

df2 = df.groupby([df['occupation'],df['gender']]).describe()
df2 = df2['age'][['max','min','mean']]
df2.rename(columns={'max':'max_usia','min':'min_usia','mean':'rerata_usia'},inplace=True)
print(df2)

gender = pd.crosstab(df.occupation, df.gender).apply(lambda r: r/r.sum(), axis=1) * 100
gender['%total'] = gender['F']+gender['M']
gender.rename(columns={'F':'%female','M':'%male'},inplace=True)
gender = gender[['%male','%female','%total']]
print(gender)