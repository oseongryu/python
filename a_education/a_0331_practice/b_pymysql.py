import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    db='korea',
    charset='utf8'
)

def selectTableList(_no):
    cur = conn.cursor()
    sql = "SELECT no, name, tel, etc FROM sample WHERE no = %s"
    cur.execute(sql, (str(_no)))
    # cur.execute\
    #     ('''
    #            SELECT no
    #                 , name
    #                 , tel
    #                 , etc
    #             FROM sample
    # ''')
    # print(cur.fetchone())

    rows = cur.fetchall()

    for row in rows:
        # print(row)
        print(row)
def selectTableList():
    cur = conn.cursor()
    sql = "SELECT no, name, tel, etc FROM sample ORDER BY no asc"
    cur.execute(sql)

    rows = cur.fetchall()

    for row in rows:

        print(row)

def insertTable(_no, _name,_tel,_etc):
    # cur = conn.cursor()
    # cur.execute \
    #     ("""
    # INSERT INTO sample
    # (
    #    no
    #  , name
    #  , tel
    #  , etc
    # )
    # VALUES
    # (
    #   6
    # , 'abc'
    # , '010-4424-502'
    # , '기타내용'
    # )
    # """)
    #
    #
    # conn.commit()
    # cur.close()
    # conn.close()
    cur = conn.cursor()
    sql = "INSERT INTO sample (no, name, tel, etc) VALUES (%s, %s, %s, %s)"
    cur.execute(sql, (str(_no), _name,_tel,_etc ))
    conn.commit()
    # cur.close()
    # conn.close()

def updateTable(_name,_no):
    cur = conn.cursor()
    sql = """UPDATE sample SET name = %s  WHERE no = %s"""
    cur.execute(sql, (_name,str(_no), ))
    conn.commit()


def deleteTable(_no):
    cur = conn.cursor()
    sql = """DELETE from sample WHERE no = %s"""
    cur.execute(sql, str(_no))
    conn.commit()



# insertTable( 10, 'abc', '010-9999-9999','etceee')
# updateTable('bbe',10)
# deleteTable(10)

selectTableList()


