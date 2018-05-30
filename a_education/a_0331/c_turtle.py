# import turtle as f
# import time
# f.speed(0)
# for i in range(286):
#  f.forward(i*2)
#  f.left(225)
# time.sleep(2)
# f.clear()
#
# for i in range(115):
#  f.forward(i)
#  f.left(i*2)
# time.sleep(2)
# f.clear()
#
# for i in range(300):
#  f.forward(i)
#  f.left(125)
# time.sleep(2)
# f.clear()


# import turtle
#
# def flower(t,n,r,angle):
#
#     for i in range(n):
#         for i in range(2):
#             t.circle(r,angle)
#             t.left(180-angle)
#         t.left(360/n)
#
# def move(t, length):
#     t.pu()
#     t.fd(length)
#     t.pd()
#
# b = turtle.Pen()
# b.color("violet")
# move(b,-100)
#
# for i in range(3):
#     flower(b, 6, 30+(10*i), 60.0)
#     b.width(2*i)



# import turtle as t
#
# t.bgcolor("black")
# t.speed(0)
#
# for x in range(200):
#     if x%5==0:
#         t.color("red")
#     if x%5==1:
#         t.color("yellow")
#     if x%5==2:
#         t.color("green")
#     if x%5==3:
#         t.color("blue")
#     if x%5==4:
#         t.color("violet")
#     t.forward(x*2)
#     t.rt(121)




import turtle
a=50
turtle.bgcolor("black")
turtle.color("pink")
turtle.speed(100)
for b in range(a):
   turtle.circle(50)
   turtle.lt(360/a)