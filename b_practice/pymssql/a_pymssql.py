#coding:euc-kr
import pymssql

server = 'localhost'
user = 'sa'
password = '1234'



conn = pymssql.connect(server, user, password, "WOOJE",charset='cp949',as_dict=True)
cursor = conn.cursor()
cursor.execute('SELECT *  FROM TB_CHNL_CD')
row = cursor.fetchone()
if row is None:
    print("null")
else:
    while row:

        print(str(row['CHNL_CD']),str(row['CHNL_NM']))
        row = cursor.fetchone()

conn.close()