#coding:euc-kr
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore, QtGui
from PIL import Image
import urllib.request
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup

#url html정보 가져오기
page = urlopen("http://kb.or.kr/p/?j=18")
document = page.read()
print(document)
page.close()

soup = BeautifulSoup(document, 'html5lib')



# 디렉토리가 없을 경우 디렉토리 생성
dirname = './images'
if not os.path.isdir(dirname):
    os.mkdir(dirname)

links = []
count = 1
for div in soup.find_all('td', 'center'):
    a = div.find('img', src=True)
    if a is not None:
        links = a['src']
        # print("http://kb.or.kr/" + links)
        # print("/images/temp"+str(count)+".jpg")
        name = str("./images/temp"+str(count)+".jpg")
        count += 1

        with urllib.request.urlopen("http://kb.or.kr/" + links[3:]) as url:
            with open(name, 'wb') as f:
                f.write(url.read())