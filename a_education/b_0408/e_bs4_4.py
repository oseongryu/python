#coding:euc-kr
import urllib.request

# naver 홈페이지에서 이미지 링크를 복사
url = "https://ssl.pstatic.net/tveta/libs/1173/1173551/cd062c53dbb106a5f2bd_20180115165020097.jpg"

savename ='imagetest1.jpg'# 이미지를 저장할 파일명 지정

mem = urllib.request.urlopen(url).read()
with open(savename, mode = "wb") as frank:  # wb = write binary
    frank.write(mem)
    print("저장되었습니다")