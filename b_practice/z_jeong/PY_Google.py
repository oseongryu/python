import pandas as pd
from datetime import datetime
from pandas_datareader import data

start = datetime(2017, 1, 1)
end = datetime(2017, 4, 30)

df = data.get_data_google("KRX:KOSPI", start, end)
df.head()