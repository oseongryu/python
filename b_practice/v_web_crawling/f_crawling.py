from urllib.request import urlopen
from bs4 import BeautifulSoup

page = urlopen("http://kb.or.kr/p/?j=18")
document = page.read()
page.close()

soup = BeautifulSoup(document, 'html5lib')

questions = soup.find(class_="pad5 lh_140")
questions_list = questions.find_all("p", class_="lpad15")

# print(questions_list)


for question in questions_list:
    print(question.get_text())
    # print('http://stackoverflow.com' + question.get('href'))