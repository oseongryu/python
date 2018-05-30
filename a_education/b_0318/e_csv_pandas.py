#coding:euc-kr
import sys
import pandas as pd
# input_file = sys.argv[1]
input_file = "C:\\Python\\Python36-32\\supplier_data.csv"

# output_file = sys.argv[2]
output_file = "C:\\Python\\Python36-32\\pandas2_data.csv"


data_frame = pd.read_csv(input_file, encoding = 'euc-kr')
print(data_frame)
data_frame.to_csv(output_file, encoding = 'euc-kr')