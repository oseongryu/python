# https://dojang.io/mod/page/view.php?id=1158
# coding:euc-kr
import requests
import urllib.request
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup

# 웹 페이지를 가져온 뒤 BeautifulSoup 객체로 만듦
response = requests.get('https://www.kica.or.kr/kyongbuk/sub04/sub04_job_list.jsp?kind=800')
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', {'class': 'box_board'})  # <table class="table_develop3">을 찾음
data = []
# for tr in table.find_all('tr'):
    # tds = list(tr.find_all('td'))
    # print(tds)
#
# for td in tds:
#     no = tds[0].text
#     company = tds[1].text
#     subject = tds[2].text
#     region = tds[3].text
#     carrier = tds[4].text
#     start_date = tds[5].text
#     end_date = tds[6].text
#     data.append([no, company, subject, region, carrier, start_date, end_date])
#
# with open('daegu.csv', 'w') as file:  # weather.csv 파일을 쓰기 모드로 열기
#     file.write('no,company, subject, region, carrier, start_date, end_date회\n')  # 컬럼 이름 추가
#     for i in data:  # data를 반복하면서
#         file.write('{0},{1},{2},{3},{4},{5},{6}\n'.format(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
