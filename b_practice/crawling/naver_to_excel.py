import requests
from bs4 import BeautifulSoup
import openpyxl


codes = ['000660', '005930']

fpath =  './test.xlsx'
wb = openpyxl.load_workbook(fpath)
ws = wb.active

row = 2
for code in codes:
    
    url = f'https://finance.naver.com/item/sise.naver?code={code}'
    response = requests.get(url)

    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    price = soup.select_one("#_nowVal").text
    price = price.replace(',','')
    print(price)
    ws[f'B{row}'] = int(price)
    row = row + 1

wb.save(fpath)