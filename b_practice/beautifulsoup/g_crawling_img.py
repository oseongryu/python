from urllib.request import urlopen
from bs4 import BeautifulSoup

page = urlopen("http://kb.or.kr/p/?j=18")
document = page.read()
page.close()

soup = BeautifulSoup(document, 'html5lib')

questions = soup.find(class_="round-box")
# questions_list = questions.find_all("p", class_="lpad15")

print('http://kb.or.kr/' +questions.get('src'))
# http://kb.or.kr/data/staff/staff_1475835454_u4xxPr7LpE.jpg
# for question in questions_list:
#     print(question.get_text())
    # print('http://stackoverflow.com' + question.get('href'))