#1
# class Person:
#     def __init__(self,_name,_no):
#         self.name = _name
#         self.no = _no
#
#
# inputname = input("이름 입력")
# inputnumber = input("전화번호 입력")
#
# c1 = Person(inputname, inputnumber)
#
# print(c1.name, c1.no)


#2
class Person:
    def __init__(self):
        self.name = input("이름 입력")
        self.no = input("전화번호 입력")


li = []
for i in range(4):
    li.append(Person())

for i in li:
    print(i.name +":"+i.no)
