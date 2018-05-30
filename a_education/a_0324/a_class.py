class A(object):
    def __init__(self,val1, val2):
        self.val1 = val1
        self.val2 = val2
    def add(self):
        return self.val1 + self.val2




b= A(3,5)

print(b.add())

