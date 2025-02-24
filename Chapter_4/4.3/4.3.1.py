import numpy as np

list_var1 = [1, 2, 3, 4]
arr1 = np.array([1, 2, 3, 4])
print(list_var1, type(list_var1))
print(arr1, type(arr1))
print(arr1.shape, len(arr1))
'''
[1, 2, 3, 4] <class 'list'>
[1 2 3 4] <class 'numpy.ndarray'>
(4,) 4
'''

print(3 * list_var1)  # [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
print(3 * arr1)  # [ 3  6  9 12]

print(arr1 + 10)  # [11 12 13 14]

list_var2 = [5, 6, 7, 8]
arr2 = np.array([5, 6, 7, 8])

print(list_var1 + list_var2)  # [1, 2, 3, 4, 5, 6, 7, 8]
print(arr1 + arr2)  # [ 6  8 10 12]

print(arr1 * arr2)  # [ 5 12 21 32]

'''
print(list_var1 * list_var2)

Traceback (most recent call last):
  File 4.3.1.py, line 25, in <module>
    print(list_var1 * list_var2)  # [1, 2, 3, 4, 5, 6, 7, 8]
          ~~~~~~~~~~^~~~~~~~~~~
TypeError: can't multiply sequence by non-int of type 'list'
'''

# 초깃값 있는 1차원 배열 생성
print(np.zeros(5))  # [0. 0. 0. 0. 0.]
print(np.ones(5))  # [1. 1. 1. 1. 1.]
