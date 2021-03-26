import pandas as pd
import numpy as np

# list
a = ['williamhill', 'python', 'pandas']
df1 = pd.DataFrame(a)
# print(df1.shape)

# dict
info = {'ID': [101, 102, 103], 'Department': ['Science', 'Tech', 'Maths', ]}

df2 = pd.DataFrame(info)
# print(df2)

# How to get the minimum, 25th percentile, median, 75th, and max of a numeric series?
p = pd.Series(np.random.normal(14, 6, 22))
state = np.random.RandomState(120)
p = pd.Series(state.normal(14, 6, 22))

#
exam_data = {'name': ['Charles', 'Swati', 'Brian', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Derek'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

df3 = pd.DataFrame(exam_data)
print(df3)
print(df3.info())
print(df3.iloc[:3])
print("Select specific columns")
print(df3[['name', 'score']])
print("Select specific columns and rows:")
print(df3.iloc[[1, 3, 5, 6], [1, 3]])
print("Number of attempts in the examination is greater than 2:")
print(df3[df3['attempts'] > 2])
print("Rows where score is missing:")
print(df3[df3['score'].isnull()])
print("Rows where score between 15 and 20 (inclusive):")
print(df3[df3['score'].between(15, 20)])
print("Number of attempts in the examination is less than 2 and score greater than 15 :")
print(df3[(df3['attempts'] < 2) & (df3['score'] > 15)])
print("\nChange the score in row 3 to 11.5:")
df3.loc[3, 'score'] = 11.5
print("\nSum of the examination attempts by the students:")
print(df3['attempts'].sum())
print("\nMean score for each different student in data frame:")
print(df3['score'].mean())
print("\nAppend a new row:")
df3.loc[10] = [1, 'Viresh', 'yes', 15.5]
print("\nDelete the new row and display the original  rows:")
df3 = df3.drop(10)
df3.sort_values(by=['name', 'score'], ascending=[False, True])
print("Sort the data frame first by ‘name’ in descending order, then by ‘score’ in ascending order:")
print(df3)

# https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/
data_url = 'http://bit.ly/2cLzoxH'
gapminder = pd.read_csv(data_url)
print(gapminder.head(3))

is_2002 = gapminder['year'] == 2002
print(is_2002.head())

gapminder_2002 = gapminder[is_2002]
print(gapminder.shape)
print(gapminder_2002.head())

gapminder_2002 = gapminder[gapminder.year.eq(2002)]
print(gapminder_2002)

gapminder_not_2002 = gapminder[gapminder.year != 2002]
gapminder_not_2002 = gapminder[gapminder['year'] != 2002]

gapminder_no_NA = gapminder[gapminder.year.notnull()]

years = [1952, 2007]
gapminder.year.isin(years)

gapminder_years = gapminder[gapminder.year.isin(years)]
gapminder_years.year.unique()


continents = ['Asia', 'Africa', 'Americas', 'Europe']
gapminder_Ocean = gapminder[~gapminder.continent.isin(continents)]

# https://www.listendata.com/2019/07/how-to-filter-pandas-dataframe.html
flights = pd.read_csv(
    "https://raw.githubusercontent.com/JackyP/testing/master/datasets/nycflights.csv")
# print(flights)
