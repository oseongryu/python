f="name : %s age: %d" %('name', 29)
print(f)


f="x= %0.5f, y= %5.2f" %(1.234567, 9.87654321)
print(f)

print("i={0} f={1} s={2} s1={3}" .format(123, 1.12345, 'python', "python"))

print("name= {name} age={age}" .format(name="han", age=30))


print("name= {age} age={name}" .format(irum="han", nai=30))

int(7.5)

float(1.6)

2e5



a=None
a is None


bool("false")

0b1010

0o12

print('''Hello, Python''')



for i in range(1,10,3):

   print("{} dan".format(i).center(10), end="\t");
   print("{} dan".format(i+1).center(10), end="\t");
   print("{} dan".format(i+2).center(10));
   print("="*10, end="\t")
   print("="*10, end="\t")
   print("="*10)

   for j in range(1,10):
     for k in range(3):
       print("{} x {} = {}".format(i+k, j, j*(i+k)).center(10), end="\t")
     print()
   print("")



