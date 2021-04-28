# %% Importing The Library
import pandas as pd
# %% Loading The DataFrame
df = pd.read_csv('E:/Work/Youtube Channel/Codes/Crime.csv')
print(df.head(2))
print(df.tail(2))
# %% Loading a txt file
df2 = pd.read_csv('E:/Work/Youtube Channel/Codes/Crime.txt',
                  delimiter='\t', index_col=0)
print(df2.head(2))
# %% Selecting a column
crime_rate = df2['CrimeRate']
print(type(crime_rate))
print(type(df2))
# %% Selecting Multiple Columns
X1 = df2[['Youth', 'Southern', 'CrimeRate']]
print(X1.head())
# %% Column Names of a Dataframe
col_names = df2.columns
print(col_names)
# %% Selecting a Row with iloc
print(X1.iloc[0])
# %% Selecting Multiple Rows with iloc
print(X1.iloc[[0, 1]])
# %% Selecting a row and a column with iloc
print(X1.iloc[0, 0])
# %% Selecting Multiple Rows and Columns with iloc
print(X1.iloc[[0, 1], [0, 1]])
# %% Selecting a row with loc
print(X1.loc[0]) 
# %% Selecting a row and column with loc
print(X1.loc[[0, 1], 'Youth'])
# %% Selecting Multiple Rows and Columns with loc
print(X1.loc[[0, 1], ['Youth', 'Southern']])
# %% Difference between loc and iloc
print(X1.iloc[0:2])
print(X1.loc[0:2])
print(df2.iloc[0:3, 0:6])
print(df2.loc[0:2, 'CrimeRate':'LabourForce'])
# %% Count the values of a column
print(X1['Southern'].value_counts())
# %% Descriptive statistics
print(X1.describe())
# %% Dropping Columns
X2 = X1.drop(columns=['Youth', 'Southern'])
print(X2.head())
# %% drop vs select
X3 = X1['CrimeRate']
print(X3.head())
print(type(X2))
print(type(X3))
# %% Adding Dataframes and Series
X4 = X1.head()
print(X4)
# %%
y1 = [150, 1, 55]
y2 = [i for i in range(6)]
print(y2)
# %%
df3 = pd.DataFrame([y1], columns=X4.columns)
# %%
X5 = pd.concat([X4, df3])
print(X5)
# %%
X5['Integer'] = y2
print(X5)
# %%
s1 = pd.Series(y2, name='Integer2', index=X5.index)
print(s1)
# %%
X6 = pd.concat([X5, s1], axis=1)
print(X6)
# %% Saving a File
X6.to_csv('Crime_head.csv')  # csv
X6.to_csv('Crime_head.txt', sep='\t') # txt
# %% Resetting the Index
X6 = X6.reset_index()
print(X6)
# %% Conditions in dataframes
print(X1.head())
print(X1.tail())
X7 = X1.loc[(X1['CrimeRate'] > 60) & (X1['CrimeRate'] < 80)]
X8 = X1.loc[(X1['CrimeRate'] > 80) | (X1['CrimeRate'] < 60)]
print(X7.head())
print(X8.head())
# %% Grouping by a column
X1.groupby(['Southern']).mean()
# %%
