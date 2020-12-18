import pandas as pd
df = pd.read_csv('/Applications/projects/AdvancedPython/data/gapminder.tsv', sep='\t')
df.head()
df.shape
df.columns
df.dtypes
df.info()
country_df = df['country']
country_df.head()
country_df.tail()
subset = df[['country', 'continent', 'year']]
subset.head(2)
subset.tail(10)
small_range = list(range(5))
subset = df.loc[0]
subset
df.loc[99]
df.iloc[-1]
df.loc[[0, 99, 999]]
df.iloc[[0, 99, 999]]