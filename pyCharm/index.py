import numpy as np
import pickle
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
arange = np.arange(1, 10, 2)
array1 = np.array([1, 3.4])
# print(array1.size)
# print(type(arange))
# print(np.zeros(5))
# print(np.zeros([2, 3]))
# print(np.eye(5))
a = np.arange(1,10)
# print(a[1:5])
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(b[0,0])
# print(b[:2,1:])
rana = np.random.randn(10)
ranb = np.random.randint(10, size =20).reshape(4, 5)
ranc = np.random.randint(10, size =20).reshape(5, 4)
# print(ranb)
# print(ranc)
# print(ranb+ranc)
# print(ranb*ranc)
# print(ranb/ranc)
mat = np.mat([list1, list2])
# print(mat)
A = np.mat(ranb)
B = np.mat(ranc)
# print(A)
# print(B)
# print(A+B)
# print(A-B)
# print(A*B)
# print(A/B)
u1 = np.unique(ranb)
# print(ranb)
# print(sum(ranb[:,0]))
# print(ranb.max())

x = np.arange(10)
# f = open('x.pkl', 'wb')
# pickle.dump(x, f)
# np.save('one_array', x)
# print(np.load('one_array.npy'))
y = np.arange(20)
# print(y)
# np.savez('two_array.npz', a=x,b=y)
z = np.load('two_array.npz')
print(z['a'])
print(z['b'])