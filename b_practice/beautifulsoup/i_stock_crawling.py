from datetime import datetime
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup


today_date = datetime.now().strftime("%Y.%m.%d")
company_code = str("352820")
url = "http://finance.naver.com/item/sise_day.nhn?code={0}&page={1}".format(company_code, 1)
page = urlopen(url)
document = page.read()
page.close()
soup = BeautifulSoup(document, 'html5lib')
tables = soup.find("table", class_="type2")
list = []

tables_spans = tables.find_all("span")

count = 0
max_count= len(tables_spans)
for i in range(max_count) :
    count +=1
    list.append(tables_spans[i].get_text().rstrip().lstrip())
    if count % 7 == 0 and today_date == list[count -7]:
        print(company_code + '/' + list[count - 7] + "/" + list[count - 6] + "/" + list[count - 5] + "/" + list[count - 4] + "/" + list[count - 3] + "/" + list[count - 2] + "/" + list[count - 1])
