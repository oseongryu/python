#coding: euc-kr
import turtle # 터틀 그래픽 모듈을 불러온다.
import random # 난수 모듈을 불러온다.

screen = turtle.Screen()
image1 = "C:\\Users\\cpc-001\\PycharmProjects\\test0317\\images\\rabbit.GIF"
image2 = "C:\\Users\\cpc-001\\PycharmProjects\\test0317\\turtle.GIF"
screen.addshape(image1)
screen.addshape(image2)

t1 = turtle.Turtle() # 첫 번째 거북이를 생성한다.
t1.shape(image1)
t1.pensize(5) # 팬의 두께를 5로 한다.
t1.penup() # 펜을 든다.
t1.goto(-300, 0) # (-300, 0) 위치로 간다.

t2 = turtle.Turtle() # 두 번째 거북이를 생성한다.
t2.shape(image2)
t2.pensize(5) # 팬의 두께를 5로 한다.
t2.penup() # 펜을 든다.
t2.goto(-300, -200) # (-300, -100) 위치로 간다.

t1.pendown() # 첫 번째 거북이의 펜을 내린다.
t2.pendown() # 첫 번째 거북이의 펜을 내린다.
t1.speed(1)
t2.speed(1)

for i in range(100): # 100번 반복한다.
	d1 = random.randint(1, 60) # 1부터 60 사이의 난수를 .
	t1.forward(d1) # 난수만큼 .
	d2 = random.randint(1, 60) # 1부터 60 사이의 난수를 .
	t2.forward(d2)