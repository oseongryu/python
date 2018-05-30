#============================================#
# -*- coding: utf-8 -*-                      #
# coffee.py                                  #
#============================================#

print("#=====================================#")
print("#                                     #")
print("#          츤데레 커피 자판기         #")
print("#                                     #")
print("#=====================================#")

print("커피값은 500원입니다.\n")

coffee = 500
while True:
    money = int(input("ㄷ..돈이나 빨리 넣어!\n\n돈: "))
    if money == 500:
        print("자.. 여기.ㄸ..딱히 좋아서 주는건 아냐!")
        coffee = coffee -1
    elif money > 500:
        print("거스름돈 %d원 여기.. 다음에도 올거지.?" % (money -500))
        coffee = coffee -1
    else:
        print("돈 더 가지고와.. 안가져오면 안줄거야!")
        print("흠.. 커피%d개 남았네.. 누구주지..?" % coffee)
    if not coffee:
        print("이제 커피가 없네.. 안주고 싶어서 안준게 아니라구!")
        break
