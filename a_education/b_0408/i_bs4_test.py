#coding:euc-kr
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup


for i in range(5):

    url = "https://www.neweracap.com/All-Headwear/c/AHE?q=%3Arelevance&page={0}&scroll=toListing".format(i)

    page = urlopen(url)
    document = page.read()
    page.close()

    soup = BeautifulSoup(document, 'html5lib')

    questions = soup.find("div",class_="col-sm-12 col-md-12")
    # questions_list = questions.find_all("div", class_="product-item--visible")
    list = []
    questions_name = questions.find_all("div", class_="product-item__name")
    # print(questions_name)
    questions_price = questions.find_all("span", class_="discount-price")
    # print(questions_price)
    # print(len(questions_name))
    # print(len(questions_price))

    max_count  = len(questions_name)

    for i in range(max_count):
        print("name:" +questions_name[i].get_text().lstrip().rstrip()+", price:"+questions_price[i].get_text().lstrip().rstrip())



#
# for question in questions_name:
#     print(question.get_text())

#
# print(questions_list)
result = """ """
# for question in questions_list:
#     self.listWidget.addItem(question.get_text())
#     # result += question.get_text() + "\n"
#     # self.label_history.setText(str(result))
#
# # self.label_history.setText(str("abc@abc.co.kr"))
#
# # self.listWidget.addItem('aaaaaa')