import pandas as pd



if __name__ == "__main__":
    data = {
        'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
        'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai',
                 'Manchester', 'Cairo', 'Osaka'],
        'age': [41, 28, 33, 34, 38, 31, 37],
        'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
    }

    row_variables = [101, 102, 103, 104, 105, 106, 107]

    df = pd.DataFrame(data=data, index =  row_variables)
    print(df)
    print(df.head(2))
    print(df.tail(2))
    cities = df['city']
    print(cities)

    #if the name fo the column is a string, then use '.'.
    print(df.city)

    #single value access
    print(cities[102])

    #single row
    print(df.loc[103])

    #creating pandas DataFrame

    #dictionary

    import numpy as np
    
    d = {'x': [1, 2, 3], 'y': np.array([2, 4, 8]), 'z': 100}
    df = pd.DataFrame(data=d)
    print(df)

    df = pd.DataFrame(data=d, index=[100, 200, 300], columns=['z', 'y', 'x'])

    #using list
    
    l = [{'x': 1, 'y': 2, 'z': 100},
        {'x': 2, 'y': 4, 'z': 100},
        {'x': 3, 'y': 8, 'z': 100}]

    df =  pd.DataFrame(data=l)

    l = [[1, 2, 100],
        [2, 4, 100],
        [3, 8, 100]]

    df = pd.DataFrame(data=l, columns=['x','y','z'])

    print(df)

    arr = np.array([[1, 2, 100],
                   [2, 4, 100],
                   [3, 8, 100]])

    df = pd.DataFrame(data=arr, columns=['x','y','z'])
    
    arr[0,0] = 1000
    print(df)

    df.to_csv('data.csv')

    df = pd.read_csv('data.csv', index_col=0)
    print(df)


    df = pd.DataFrame(data=data, index = row_variables)

    #retreiving labels
    
    print(df.index)

    print(df.columns)

    print(df.columns[1])

    df.index = np.arange(10,17)

    print(df.index)

    print(df)

    #data as numpy array

    df.to_numpy()



    #data types

    print(df.dtypes)

    
    df_ = df.astype(dtype={'age':np.int32, 'py-score':np.float32})

    print(df_.dtypes)

    print(df_.ndim)

    print(df_.shape)

    print(df_.size)

    print(df_.memory_usage())

    print(df['name'])

    print(df.loc[10])

    print(df.iloc[0])

    print(df.loc[:, 'city'])

    print(df.iloc[:, 1])

    print(df.loc[11:15, ['name',  'city']])

    print(df.iloc[1:6, [0,1]])


    #setting data with accessors

    df.loc[:13, 'py-score'] = [40,50,60,70]
    df.loc[14:, 'py-score'] = 0

    print(df['py-score'])

    df.iloc[:,  -1] = np.array([88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0])


    #inseritng and deleting rows

    print(df)

    john = pd.Series(data=['John', 'Boston', 34, 79], index = df.columns, name = 17)

    df = df.append(john)
    print(df)
    
          
    df = df.drop(labels=[17], inplace=False)

    print(df)


    #inserting and deleting columsn

    df['js-score'] = np.array([71.0, 95.0, 88.0, 79.0, 91.0, 91.0, 80.0])

    print(df)

    df['total-score'] = 0.0

    print(df)

    df.insert(loc=4, column='django-score', value = np.array([86.0, 81.0, 78.0, 88.0, 74.0, 70.0, 81.0]))

    print(df)

    #deleting

    del df['total-score']

    df.pop('js-score')

    df = df.drop(labels='age', axis=1, inplace=False)

    print(df)


    #arithmetic operations

    df['py-score'] + df['django-score']

    df['py-score'] / 100


    #sorting

    df.sort_values(by='django-score', ascending=False)

    print(df)

    df.sort_values(by=['django-score', 'py-score'], ascending=[False, False])

    print(df)

    #filtering data

    filter_ = df['py-score'] >= 80

    print(filter_)


    print(df[filter_])


    print(df[(df['py-score'] >= 80) & (df['py-score'] >= 80)])

    df['django-score'].where(cond=df['django-score'] >= 80, other=0.0)

    print(df)


    #data statistics

    print(df.describe())

    print(df.mean())

    print(df['py-score'].mean())

    print(df.std())

    print(df['py-score'].std())


    #handling missing data

    import numpy as np

    df_ = pd.DataFrame({'x':[1,2,np.nan,4]})

    print(df_)

    print(df_.mean(skipna=False))

    print(df_.mean(skipna=True))

    print(df_.fillna(value=0, inplace=False))

    print(df_.fillna(method='ffill', inplace=False))

    print(df_.fillna(method='bfill', inplace=False))

    print(df_.interpolate())
    
    df_.dropna(inplace=False)


    #iterating over pandas frames

    for col_label, col in df.iteritems():
        print(col_label, col, sep='\n', end='\n\n')


    for row_label, row in df.iterrows():
        print(row_label, row, sep='\n', end='\n\n')

    for row in df.loc[:, ['name', 'city', 'total']].itertuples():
        print(row)
 

    

    
                              

    