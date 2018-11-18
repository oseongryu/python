import sqlite3
import csv

conn = sqlite3.connect("C:\\Temp\\sqlitedb.db")


cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS stocks')

cur.execute\
("""
CREATE TABLE stocks
(   id text
, pw text
)
""")
conn.commit()

f=open('C:\\Temp\\csvfile3.csv','r') # open the csv data file
# next(f, None) # skip the header row
reader = csv.reader(f)
for row in reader:
    cur.execute('INSERT INTO  stocks VALUES (?,?)', row)
conn.commit()


for row in cur.execute("SELECT * FROM stocks"):
    print(row)
f.close()

conn.close()
