#coding:euc-kr
from bs4 import BeautifulSoup
html ="""
<html><body>
<div id = "food">
    <h1> 초밥이 먹고 싶을 때 </h1>
    <ul class = "items">
        <li> 유부초밥</li> 
        <li> 연어초밥</li>
        <li> 광어 사시미</li>
    </ul>
</div>
</body></html>
"""
# 제목 부분 추출하기
soup = BeautifulSoup(html,'html.parser')
# 하나만 수집 div id =food 안에 h1을 가져온다.
h1= soup.select_one("div#food > h1")
print( "h1 =" ,h1.string) # string은 문자만 추출 해낸다.
# 목록 부분 추출
# ul class = items안에 li를 모두 가져온다.
li_list = soup.select("div#food > ul.items > li" )
for li in li_list:
    print("li = ", li.string) # string = 문자만 가져온다.