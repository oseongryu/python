#coding:euc-kr
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup

#네이버 주식 http://finance.naver.com/ 에서 업체옆에 숫자입력
company_code = '000020'

file_name = "C:/Temp/{0}.txt".format(company_code)
f = open(file_name, 'w')


# print("      날짜    /종가    /전일비   /시가   /고가   /저가   /거래량   ")
f.write("  날짜    / 종가/전일비/시가/고가/저가/ 거래량   \n")
for x in range(1,10):
    url = "http://finance.naver.com/item/sise_day.nhn?code={0}&page={1}".format(company_code,x)

    page = urlopen(url)
    document = page.read()
    page.close()

    soup = BeautifulSoup(document, 'html5lib')

    tables = soup.find("table",class_="type2")
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
        # print(list[i])
        if count % 7 == 0:
            print(list[count - 7] + "/" + list[count - 6] + "/" + list[count - 5] + "/" + list[count - 4] + "/" + list[count - 3] + "/" + list[count - 2] + "/" + list[count - 1])
            f.write(list[count - 7] + "/" + list[count - 6] + "/" + list[count - 5] + "/" + list[count - 4] + "/" + list[count - 3] + "/" + list[count - 2] + "/" + list[count - 1] +"\n")
            list_count += 1


f.close()