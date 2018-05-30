import sqlite3

conn = sqlite3.connect("test.db")

cur = conn.cursor()

cur.execute\
("""
CREATE TABLE stocks
(   date text
, trans text
, symbol text
, qty real
, price real
)
""")

cur.execute\
("""
INSERT INTO stocks
VALUES
( 
'2016-01-06'
, 'BUY'
, 'RHAT'
, 200
, 15035
)
""")
conn.commit();

for row in cur.execute("SELECT * FROM stocks ORDER BY price"):
    print(row)

cur.close()



