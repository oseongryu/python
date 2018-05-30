class Person:
    def __init__(self,_name,_no):
        self.name = _name
        self.no = _no


p1 =Person('홍길동','111-1111')
p2 =Person('김철수',('2'*3) +"-" +('2'*4))
p3 =Person('이영희','333-3333')

li = []
li.append(p1)
li.append(p2)
li.append(p3)

for i in li:
    print(i.name +":"+i.no)
