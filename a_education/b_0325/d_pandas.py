import pandas as pd
import numpy as np


pandas_series = pd.Series([3000,3100,3200],\
                          index=['2018-01-10','2017-12-12','2016-11-20'])
print(type(pandas_series))
print(pd.DataFrame(pandas_series))

#원하는 인덱스 위치부터 가져올 수 있음
print(pd.DataFrame(pandas_series[2:]))
