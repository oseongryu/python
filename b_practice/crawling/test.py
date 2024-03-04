import requests

from bs4 import BeautifulSoup

import pyautogui

import time


keyword = pyautogui.prompt("검색어를 입력하세요")
lastpage = pyautogui.prompt("마지막 페이지번호를 입력하세요")
pageNum = 1
# 10페이지 까지 가져와보자

for i in range(1, int(lastpage)*10, 10):
    print(f"{pageNum}번째 페이지 입니다=================")
    print(i)
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}")
    print(response.url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select('.news_tit') # 결과는 리스트
    for link in links:
        title = link.text # 태그 안에 있는 모든 글자
        url = link.attrs['href'] # href의 속성값
        print(title, url)
    pageNum = pageNum + 1
    time.sleep(0.5)