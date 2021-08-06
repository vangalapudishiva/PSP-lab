# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
my_arr = np.arange(10000)
#print(type(my_arr))
#print(my_arr)
#2D
import numpy as np
a = np.array([(1,4,3),(4,5,6)])
#print(a)
#3D
import numpy as np
a = np.array([(2,3,4),(4,5,6),(8,9,3)])
#print(a)
import numpy as np
my_list = list(range(100))
#print(my_list)
import numpy as np
array = np.array([[10,20,30],[40,50,90]])
#print(array*2)
import numpy as np
a = np.random.random((2,5))
#print(a)
import numpy as np
a = np.random.rand(3,3,3)
#print(a)
import numpy as np
a = np.random.randn(2,3)
#print(a*2)
import numpy as np
a = np.array([[-0.2047, 0.4789, -0.5194],[-0.5557, 1.9658, 1.3934]])
a1 = np.array([[ -2.0471, 4.7894, -5.1944],[ -5.5573, 19.6578, 13.9341]])
#print(a+a1)
import numpy as np
a = np.array([[1,2,3],
             [2,3,4],
             [4,5,6]])
#print(a)
b = np.shape(a)
#print(b)
import numpy as np
arr = np.array([127,-128],dtype = np.int32)
#print(arr.dtype)
import numpy as np
a = [6, 7.5, 8, 0, 1]
arr = np.array(a)
#print(a)
import numpy as np
a = ([[1, 2, 3, 4],
     [5, 6, 7, 8]])
arr = np.array(a)
#print(arr)
a = np.shape(arr)
#print(a)
b = arr.ndim
#print(b)
import numpy as np
a = [6, 7.5, 8, 0, 1]
a =  np.array([6, 7.5, 8, 0, 1],dtype = float)
#print(a.dtype)
import numpy as np
a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8]],dtype = int)
#print(a.dtype)
import numpy as np
p = np.zeros(10)
#print(p)
import numpy as np
c = np.zeros((3, 6))
#print(c)
import numpy as np
k = np.empty([2, 3, 2])
#print(k)
#print(k.dtype)
import numpy as np
a = np.arange(3,6)
#print(a)
import numpy as np
arr1 = np.array([1, 2, 3], dtype=np.float64)
arr2 = np.array([1, 2, 3], dtype=np.int32)
#print(arr1.dtype)
#print(arr2.dtype)
import numpy as np
s =  np.array([1, 2, 3, 4, 5], dtype=np.int64)
#print(s.dtype)
import numpy as np
float_arr = arr.astype(np.float64)
#print( float_arr.dtype)
import numpy as np
arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
#print(arr)
import numpy as np
a = arr.astype(np.int32)
#print(a)
#print(a.dtype)
import numpy as np
numeric_strings = np.array(['1.25','-9.6','42'], dtype=np.string_)
numeric_strings.astype(float)
#print(numeric_strings.astype(float))
import numpy as np
int_array = np.arange(10)
calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
int_array.astype(calibers.dtype)
#print(int_array.astype(calibers.dtype))
import numpy as np
empty_uint32 = np.empty(8, dtype='u4')
#print(empty_uint32)
import numpy as np
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
#print(arr)
#print(arr*arr)
#print(arr+arr)
#print(arr-arr)
#print(1 / arr)
#print(arr*2)
import numpy as np
c =  np.array([[0., 4., 1.], [7., 2., 12.]])
#print(c)
import numpy as np
arr =  np.array([[1., 2., 3.], [4., 5., 6.]])
c = np.array([[0., 4., 1.], [7., 2., 12.]])
k = c>arr
#print(k)
#print(k.dtype)
import numpy as np
v =  np.arange(10)
#print(v)
import numpy as np
v = np.arange(10)
#print(v[5])
#print(v[5:8])
v[5:8] = 12
#print(v)
import numpy as np
v =  np.arange(10)
v_slice = v[5:8]
#print(v_slice)
import numpy as np
v =  np.arange(10)
v_slice = v[5:8]
v[5:8] = 12
v_slice[:] = 64
#print(v_slice)
v_slice[1] = 12345
#print(v)
import numpy as np
a2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a2d[2]
#print(a2d[2])
import numpy as np
a2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a2d[0][2]
a2d[0, 2]
#print(a2d[0][2])
#print(a2d[0, 2])
import numpy as np
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
#print(arr3d)
#arr3d[0] is a 2 × 3 array
#print(arr3d[0])
old_values = arr3d[0].copy()
arr3d[0] = 42
#print(arr3d)
arr3d[0] = old_values
#print(arr3d)
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr3d[1,0]
#print(arr3d)
x = arr3d[1]
#print(x)
x[0]
#print(x[0])
import numpy as np
arr = np.arange(10)
arr_slice = arr[5:8]
arr[5:8] = 64
#print(arr)
arr_slice = arr[1:6]
#print(arr_slice)
import numpy as np
a2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#print(a2d)
a2d[:2]
#print(a2d[:2])
a2d[:1, 2:]
#print(a2d[:1, 2:])
#print(a2d[:2])
a2d[1, :2]
#print(a2d[1, :2])
a2d[:2, 2]
#print(a2d[:2,2])
a2d[:, :1]
#print(a2d[:,:1])
import numpy as np
a2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a2d_slice = a2d[:2,1:]
a2d[:2,1:] = 0
#print(a2d)
import numpy as np
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
a = np.random.randn(7,4)
#print(names.dtype)
#print(names == 'Bob')
#print(a[names == 'Bob'])
#print(a[names == 'Bob', 2:])
#print(a[names == 'Bob', 3])
#print(names != 'Bob')
#print(a[~(names == 'Bob')])
cond = names == 'Bob'
#print(a[~cond])
k = (names == 'Joe') | (names == 'Bob')
#print(k)
#print(names.dtype)
k = a[a < 0]
a[a < 0] = 0
#print(a)
a[names != 'Joe'] = 7 
#print(a)
import numpy as np
np.empty((6, 4))
for i in range(6):
    a[i] = i
    #print(a[i])
import numpy as np
np.empty((4,3))
for i in range(4):
    #print([[4, 3, 0, 6]])
    #print([[-3, -5, -7]])
    h = [[-3, -5, -7]]
    #print(h)
y = np.arange(32).reshape((8, 4)) 
#print(y)   
#print(y[[1, 5, 7, 2], [0, 3, 1, 2]])
#print(y[[1, 5, 7, 2]][:, [0, 3, 1, 2]])
r = np.arange(15).reshape((3, 5))
#print(r)
#print(r.T)
sr = np.random.randn(6, 3)
#print(sr)
ss = np.dot(sr.T, sr)
#print(ss)
import numpy as np
a = np.arange(20).reshape(5,4)
b = np.reshape(a,(5,4),)
g = np.transpose(a)
#print(g)
import numpy as np
a = np.arange(16).reshape((2,2,4))
l = a.swapaxes(1,2)
#print(l)
import numpy as np
z = np.arange(10)
x =np.sqrt(z)
#print(x)
h = np.exp(z)
#print(h)
import numpy as np
x = np.random.randn(8)
y = np.random.randn(8)
#print(x)
#print(y)
#print(np.maximum(x,y))
import numpy as np
ss= np.random.randn(7) * 5
#print(ss)
ss= np.random.randn(7) * 5
remainder, whole_part = np.modf(ss)
#print(remainder)
#print(whole_part)
import numpy as np
e = np.random.randn(7) * 5
#print(np.sqrt(e))
points = np.arange(-5, 5, 0.01) 
xs, ys = np.meshgrid(points, points)
#print(ys)
z = np.sqrt(xs ** 2 + ys ** 2)
#print(z)
import numpy as np
re = np.random.randn(4, 4)
#print(re)
re>0
#print(re>0)
f = np.where(re > 0, 2, -2)
#print(f)
c = np.where(re > 0, 2, re) 
#print(c)
import numpy as np
arr = np.random.randn(5, 4)
#print(arr)
#print(arr.mean())
#print(np.mean(arr))
#print(arr.sum())
import numpy as np
#print(arr.mean(1))
#print(arr.sum(0))
import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
#print(arr.cumsum())
arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
#print(arr)
#print(arr.cumsum(axis=0))
#print(arr.cumprod(axis=1))
import numpy as np
pp = np.random.randn(100)
#print((pp > 0).sum() )
import numpy as np
bools = np.array([False, False, True, False])
#print(bools.any())
#print(bools.all())
import numpy as np
arr = np.random.randn(6)
#print(arr)
arr = np.random.randn(5, 3)
print(arr)
print(arr.sort(1))
print(arr)




























