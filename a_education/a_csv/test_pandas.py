#coding:euc-kr
import sys
import pandas as pd
input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file, encoding = 'euc-kr')
print(data_frame)
data_frame.to_csv(output_file, encoding = 'euc-kr')