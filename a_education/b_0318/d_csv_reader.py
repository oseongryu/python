import csv

with open('test.csv', 'r', encoding='euc-kr') as fd:
 cin = csv.reader(fd)
 arrCsv = [row for row in cin]
 print( arrCsv )
