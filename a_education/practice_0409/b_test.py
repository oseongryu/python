import requests  # 웹 페이지의 HTML을 가져오는 모듈
from bs4 import BeautifulSoup  # HTML을 파싱하는 모듈

# 웹 페이지를 가져온 뒤 BeautifulSoup 객체로 만듦
response = requests.get('https://www.kica.or.kr/kyongbuk/sub04/sub04_job_list.jsp?kind=800')
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', {'class': 'borad_data'})  # <table class="borad_data">을 찾음
data = []  # 데이터를 저장할 리스트 생성
for tr in table.find_all('tr'):  # 모든 <tr> 태그를 찾아서 반복(각 지점의 데이터를 가져옴)
    tds = list(tr.find_all('td'))  # 모든 <td> 태그를 찾아서 리스트로 만듦
    # (각 날씨 값을 리스트로 만듦)
    for td in tds:  # <td> 태그 리스트 반복(각 날씨 값을 가져옴)
        no = tds[0].text
        co = tds[1].text
        title = tds[2].text
        location = tds[3].text
        career = tds[4].text
        regDate = tds[5].text
        closeDate = tds[6].text
        data.append([no.lstrip().rstrip(), co.lstrip().rstrip(), title.lstrip().rstrip(),location.lstrip().rstrip(),career.lstrip().rstrip(),regDate.lstrip().rstrip(),closeDate.lstrip().rstrip()])
print(data)


with open('daegu.csv', 'w') as file:    # weather.csv 파일을 쓰기 모드로 열기
    file.write('no,company, subject, region, carrier, start_date, end_date회\n')                  # 컬럼 이름 추가
    for i in data:                                              # data를 반복하면서
        file.write('{0},{1},{2},{3},{4},{5},{6}\n'.format(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))