import csv
with open('test.csv','w',encoding='euc-kr',newline='') as fd:
    out = csv.writer(fd)
    out.writerow(['1','first'])
    out.writerow(['2','second'])