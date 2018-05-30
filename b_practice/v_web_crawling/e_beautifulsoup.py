from urllib.request import urlopen
from bs4 import BeautifulSoup

page = urlopen("http://stackoverflow.com/questions/tagged/python")
document = page.read()
page.close()

soup = BeautifulSoup(document, 'html5lib')

questions = soup.find(id="questions")
questions_list = questions.find_all("a", class_="question-hyperlink")

for question in questions_list:
    print(question.get_text())
    print('http://stackoverflow.com' + question.get('href'))