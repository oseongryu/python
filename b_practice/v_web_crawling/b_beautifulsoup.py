# -*- coding: utf-8 -*-
# jsc 페이지 post 로 호출하기
import requests

payload = {'query': '202.30.50.51', 'ip': '본인의 IP 주소'}
r = requests.post("https://whois.kisa.or.kr/kor/whois.jsc", data=payload)
r.encoding = 'utf-8'
# print(r.text)


# 결과에서 주소 얻어오기
import re

pattern = re.compile("주소.*: ([^0-9].*)")
match = re.findall(pattern, r.text)
print(match[0])
