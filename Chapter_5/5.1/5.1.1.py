import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8, ], [9, 10, 11, 12]])
print(arr)
'''
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
'''
print(arr.shape, len(arr))  # (3, 4) 3

# 2차원 배열의 인덱싱과 슬라이싱1
# 첫 번째(인덱스 0) 행 출력
print(arr[0])  # [1 2 3 4]
# 두 번째 행(인덱스 1)의 세 번째 원소(인덱스 2) 출력
print(arr[1][2])  # 7
# 세 번째 행(인덱스 2) 출력
print(arr[2, :])  # [ 9 10 11 12]
# 네 번째 열(인덱스 3) 출력
print(arr[:, 3])  # [ 4  8 12]

print(arr[1:3, :2])
'''
[[ 5  6]
 [ 9 10]]
'''
# 두 개의 2차원 배열 생성
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
arr4 = np.array([[1, 1], [2, 2], [3, 3]])
print(arr3)
'''
[[1 2 3]
 [4 5 6]]
 '''
print(arr3.shape)  # (2, 3)
print(arr4)
'''
[[1 1]
 [2 2]
 [3 3]]
'''
print(arr4.shape)  # (3, 2)

# 2차원 배열끼리의 곱
print(np.dot(arr3, arr4))
'''
[[14 14]
 [32 32]]
'''
# 1차원 배열
arr1 = np.array([1, 2, 3, 4])
print(np.sum(arr1), np.cumsum(arr1))  # 10 [ 1  3  6 10]
# 2차원 배열
print(arr)
'''
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
'''
print(np.sum(arr))  # 78
print(np.sum(arr, axis=0))  # [15 18 21 24]
print(np.sum(arr, axis=1))  # [10 26 42]

# 1차원 배열
print(np.prod(arr1), np.cumprod(arr1))  # 24 [ 1  2  6 24]
# 2차원 배열
print(np.prod(arr))  # 479001600
print(np.prod(arr, axis=0))  # [ 45 120 231 384]
print(np.prod(arr, axis=1))  # [   24  1680 11880]

print(arr1)
# [1 2 3 4]
# 1차원 배열
print(np.mean(arr1), np.std(arr1))  # 2.5 1.118033988749895
print(arr)
'''
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
'''
# 2차원 배열
print(np.mean(arr), np.std(arr))  # 6.5 3.452052529534663
print(np.mean(arr, axis=0), np.std(arr, axis=0))  # [5. 6. 7. 8.] [3.26598632 3.26598632 3.26598632 3.26598632]
print(np.mean(arr, axis=1), np.std(arr, axis=1))  # [ 2.5  6.5 10.5] [1.11803399 1.11803399 1.11803399]

# 1차원 배열
print(np.max(arr1), np.min(arr1))  # 4 1
# 2차원 배열
print(np.max(arr), np.min(arr))  # 12 1
print(np.max(arr, axis=0))  # [ 9 10 11 12]
print(np.min(arr, axis=1))  # [1 5 9]

print(arr1)
# [1 2 3 4]
# 1차원 배열
print(np.argmax(arr1), np.argmin(arr1))  # 3 0
print(arr)
'''
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
'''
# 2차원 배열
print(np.argmax(arr), np.argmin(arr))  # 11 0
print(np.argmax(arr, axis=0))  # [2 2 2 2]
print(np.argmin(arr, axis=1))  # [0 0 0]

arr5 = np.array([12, 5, 27, 9, 53, 14])
idx = np.where(arr5 < 10)
print(idx[0]) # [1 3]
new_arr5 = np.where(arr5 < 10, 1, 0)
print(new_arr5) # [0 1 0 1 0 0]
