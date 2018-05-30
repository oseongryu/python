import urllib.request

# naver 홈페이지에서 이미지 링크를 복사
url = "https://ssl.pstatic.net/tveta/libs/1173/1173551/cd062c53dbb106a5f2bd_20180115165020097.jpg"

savename ='imagetest.jpg'# 이미지를 저장할 파일명 지정

urllib.request.urlretrieve(url, savename)
print('save..........')