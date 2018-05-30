import pymysql

conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    db = 'korea',
    charset = 'utf8'
)

try:
   cur = conn.cursor()
   cur.execute('select * from sample ')
   print(cur.fetchone())
finally:
   cur.close()
   conn.close()