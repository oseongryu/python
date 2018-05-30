from pandas import Series, DataFrame

raw_data = { 'col0' : [1, 2, 3, 4]
             , 'col1' : [10, 20, 30, 40]
            }

data = DataFrame(raw_data)
print(data)