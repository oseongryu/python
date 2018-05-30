#coding:euc-kr
import urllib.request
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup


# 출력 파일 명
OUTPUT_FILE_NAME = 'daegu_output.txt'

page = urlopen("https://www.kica.or.kr/kyongbuk/sub04/sub04_job_list.jsp?kind=800")
document = page.read()
page.close()

soup = BeautifulSoup(document, 'html5lib')

questions = soup.find(class_="borad_data")
questions_list = questions.find_all("td")
count = 0
list = []
data = []
list_count = 0
max_count = len(questions_list)

for i in range(max_count):
    count += 1
    list.append(questions_list[i].get_text().rstrip().lstrip())
    # print(list[i])
    if count % 8 == 0 :
        # print(list[count-8] +"," +list[count-7] +"," + list[count-6] +"," + list[count-5] +"," + list[count-4] +"," + list[count-3] +"," + list[count-2] + list[count-1] )
        data.append([list[count-8], list[count-7], list[count-6], list[count-5], list[count-4], list[count-3], list[count-2], list[count-1]])
        list_count +=1
        # print(list_count)


with open('daegu.csv', 'w') as file:    # weather.csv 파일을 쓰기 모드로 열기
    file.write('no,company, subject, region, carrier, start_date, end_date회\n')
    for i in data:                                              # data를 반복하면서
        file.write('{0},{1},{2},{3},{4},{5},{6},{7}\n'.format(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))



#
# for i in list:
#     print(i)
#     # print(question.get_text().rstrip().lstrip())
#     # print(question.get_text().rstrip().lstrip())
#     # if count % 7 != 0 :
#     #     list.append(question.get_text().rstrip().lstrip())
#     # else:
#     #     count = count +1
#     #     print(count)


# for i in list:
#     print(i)
# print(questions_list)