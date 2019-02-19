# from pandas.io import data, wb
# from pandas_datareader import data,wb
import pandas_datareader as pdr

print(pdr.get_data_fred('GS10'))