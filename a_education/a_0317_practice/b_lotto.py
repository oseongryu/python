#coding:euc-kr


import random

print("="*50)
print("로또 번호")
print("="*50)

while True:
      put_money = int(input("금액을 입력하시오. : "))
      print("\n")
      game_cnt = put_money // 1000
      if put_money % 1000 == 0:

          for i in range(game_cnt):
              lotto = random.sample(range(1,46),6) # 로또라는 변수에 1~45
                                               # 숫자 중 6개를 임의로 추출
              lotto.sort() # 무작위로 추출되는 숫자 정렬
              print("{0:>2} GAME : {1}".format(i+1,lotto))
              if (i+1) == 5:
                  print("="*50)
      else:
          print("1000원 단위로 입력하세요. : ")
          print("\n")
      if put_money == 0:
         break