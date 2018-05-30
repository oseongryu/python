#coding: euc-kr
import turtle
t = turtle.Turtle()
t.shape("turtle")

x1 = int(input("큰 원의 중심좌표 x1: "))
y1 = int(input("큰 원의 중심좌표 y1: "))
r1 = int(input("큰 원의 반지름: "))
x2 = int(input("작은 원의 중심좌표 x2: "))
y2 = int(input("작은 원의 중심좌표 y2: "))
r2 = int(input("작은 원의 반지름: "))

t.penup()
t.goto(x1, y1)
t.pendown()
t.circle(r1)

t.penup()
t.goto(x2, y2)
t.pendown()
t.circle(r2)

dist = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
if dist <= r1-r2:
    turtle.write("두번째 원이 첫번째 원의 내부에 있습니다.")
elif dist <= r1+r2:
    turtle.write("두번째 원이 첫번째 원과 겹칩니다.")
else:
    turtle.write("두번째 원이 첫번째 원과 겹치지 않습니다.")