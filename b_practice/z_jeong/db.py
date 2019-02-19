import pymssql

server = 'localhost'
user = 'sa'
password = '1234'



conn = pymssql.connect(server, user, password, "NSK")
cursor = conn.cursor()
cursor.execute('SELECT * FROM Guests')
row = cursor.fetchone()
if row is None:
    print("null")
else:
    while row:
        print(str(row[0]))
        row = cursor.fetchone()

conn.close()