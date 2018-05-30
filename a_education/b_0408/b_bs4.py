#coding:euc-kr

import requests
r = requests.get('https://en.wikipedia.org/wiki/Main_Page')
html_doc = r.text


from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')