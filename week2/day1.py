import pandas as pd
data = pd.Series([1, 3, 5, 7, 9])
data2 = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 34, 29, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}
df = pd.DataFrame(data2)
print(df)

# df = pd.read_csv('C:/Users/ned17/DIMA/DevelopersInstitute/test_df.csv')
print(df[df['Age']>30])
df.to_csv('C:/Users/ned17/DIMA/DevelopersInstitute/test_df.csv')