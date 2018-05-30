import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
import pymssql
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup

conn = pymssql.connect('localhost', 'sa', '1234', "NSK")

def selectTableList():
    cur = conn.cursor()
    sql = "SELECT MKT_CD FROM TB_STK_MKT WHERE MKT_CLSS_CD = 0"
    cur.execute(sql)

    rows = cur.fetchall()

    return rows

def set_theme_market(comcd, _t7,_t6,_t4,_t3,_t2,_t1):
    cur = conn.cursor()
    t7 = _t7.replace(".","")
    t6 = _t6.replace(",","")
    t4 = _t4.replace(",","")
    t3 = _t3.replace(",","")
    t2 = _t2.replace(",","")
    t1 = _t1.replace(",","")

    sql = """
                INSERT INTO TB_STK_MKT_HIS 
                (
                  MKT_CD
                , MKT_DT
                , MKT_OPN_PRC
                , MKT_CLZ_PRC
                , MKT_HIGH_PRC
                , MKT_LOW_PRC
                , MKT_VOL_QTY
                , CRE_USR_ID
                , CRE_DT
                , UPD_USR_ID
                , UPD_DT
                ) 
                VALUES 
                (
                  %s
                , %s
                , %d
                , %d
                , %d
                , %d
                , %d
                , 'MIG_USR'
                , GETDATE()
                , 'MIG_USR'
                , GETDATE()

                )
                """
    cur.execute(sql,(comcd, t7,t6,t4,t3,t2,t1) )
    conn.commit()

if __name__ == "__main__":
    rows = selectTableList()
    for row in rows:

        company_code = str(row[0])

        for x in range(1, 30):
            url = "http://finance.naver.com/item/sise_day.nhn?code={0}&page={1}".format(company_code, x)

            page = urlopen(url)
            document = page.read()
            page.close()

            soup = BeautifulSoup(document, 'html5lib')

            tables = soup.find("table", class_="type2")
            # questions_list = questions.find_all("div", class_="product-item--visible")
            list = []
            tables_spans = tables.find_all("span")
            # for table_span in tables_spans:
            #     print(table_span.get_text().lstrip().rstrip())

            count = 0
            list = []
            list_count = 0
            max_count = len(tables_spans)

            for i in range(max_count):
                count += 1
                list.append(tables_spans[i].get_text().rstrip().lstrip())
               #print(list[i])
                if count % 7 == 0:
                    print(company_code + '/' + list[count - 7] + "/" + list[count - 6] + "/" + list[count - 5] + "/" + list[count - 4] + "/" + list[count - 3] + "/" + list[count - 2] + "/" + list[count - 1])
                    set_theme_market(company_code,list[count - 7], list[count - 4],list[count - 6],list[count - 3],list[count - 2],list[count - 1])



