import numpy as np

a = np.array([1.1,2.2,3.3,4.4,5.5])
# print(a[3:])
print(a[:3])

print(a.sum())
print(a.std())
print(a.cumsum())



print("기본값",a)
print("제곱",a*2)
print("거듭제곱",a**2)
print("루트값",np.sqrt(a))


b = np.array([a, a**2])
print(b)

print("axis=0 배열의 세로축 합계값을 구함",b.sum(axis=0))
print("axis=1 배열의 가로축 합계값을 구함",b.sum(axis=1))


print(np.array([[[0,0,0],[1,2,3]]]))

values = np.zeros((1,2,3),dtype='i')


print(values)


val = np.zeros((1,2,3),dtype='f')
print(val)