#coding:euc-kr
from bs4 import BeautifulSoup
html ="""
<html><body>
<h1>삼순이 호떡집</h1>
<p>호떡의 생명은 밀가루인가?</p>
<p>충남의 랜드마크 - 천안아산역에서 5분거리</p>
</body></html>
"""
# 파싱을 통해서 한 줄로 나열된 소스를 보기 쉽게 한다.
soup = BeautifulSoup(html, 'html.parser')
h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling
print("h1 = " + h1.string)
print("p1 = " + p1.string)
print("p2 = " + p2.string)

