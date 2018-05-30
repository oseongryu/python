#coding:euc-kr
class Car:
    def __init__(self):
        self.drive()
    def drive(self):
        self.speed = 60

myCar = Car()
# myCar.speed = 0
myCar.color = "blue"
myCar.model = "E-Class"
myCar.year = "2017"


# print(myCar.speed)


print("자동차 객체 생성")
print("자동차 속도 : ",myCar.speed)
print("자동차 색상 : ",myCar.color)

print("자동차 모델 : ",myCar.model)
myCar.drive()
print("자동차 속도 : ",myCar.speed)

