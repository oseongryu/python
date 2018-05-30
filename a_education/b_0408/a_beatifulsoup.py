# from urllib.request import urlopen
# html = urlopen('http://www.naver.com')
# doc = html.read().decode('utf-8')
# print(doc)

#방식 1

from urllib.request import *
html = urlopen('http://www.naver.com')
doc = html.read().decode('utf-8')
# html = urlopen('https://www.kica.or.kr/kyongbuk/sub04/sub04_job_list.jsp?kind=800')
# doc = html.read().decode('euc-kr')

print(doc)


#방식 2

import requests
r = requests.get('http://www.naver.com')
print(r.text)
