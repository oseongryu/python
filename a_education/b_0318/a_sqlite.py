import sqlite3

conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('''CREATE TABLE stocks
         (date text, trans text, symbol text, qty real, price real)''')
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',150,35.2)")
c.execute("INSERT INTO stocks VALUES ('2006-01-06','BUY','RHAT',170,35.17)")
conn.commit()

for row in c.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)

c.close()