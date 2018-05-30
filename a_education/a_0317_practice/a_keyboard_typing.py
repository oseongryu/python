# coding:euc-kr

import random
import time

print("="*40)
print("타자 연습")
print("="*40)
start = time.time()
ex = ["강아지","고양이","원숭이","호랑이","사자","코뿔소","기린","표범","코끼리", "사슴","곰","하마"]
cnt = 1
while True:
      ex2 = random.choice(ex)
      print("문제.({})".format(cnt))
      print(ex2)
      ex_answer = input()

      if ex2 == ex_answer:
         print("통과")
         cnt += 1
      else:
         print("실패...재시도!")
      if cnt == 6:
         end = time.time()
         res = end - start
         print("총 시간은 {0}초 입니다.".format(res))
         break