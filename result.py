import numpy as np

arr1 = np.array([[1, 2, 3],[4, 5, 6]])
arr = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
arr2 = np.array([[7, 8, 9]])
arr3 = arr2.reshape(3,1)
print(arr3)
arr1_Append = np.append(arr1, arr2)  #축 지정x
print('arr1 + arr2: \n' ,arr1_Append)

arr1_Axis0 = np.append(arr1, arr2, axis = 0) # axis = 0 행 기준
print('arr1 + arr2 (axis = 0) : \n', arr1_Axis0)

# arr1 으로 넣었을 땐 행이 하나 부족해서 에러가 남
# arr으로 넣었을 땐 arr3와 arr1의 행과 열의 갯수가 같아 append 가능
arr1_Axis1 = np.append(arr, arr3, axis = 1) 
print(arr1_Axis1)


import numpy as np
# arr=np.arange(1, 31).reshape(6,5)
# print(arr)
# # 전체의 최댓값
# print('전체 최대값:', np.max(arr), arr.max())
# # 각 행의 합
# print('행(가로)의 합:', np.sum(arr, axis = 1))
# # 각 행의 최댓값
# print('행(가로)의 최대값:', np.max(arr, axis = 1))
# # 각 열의 평균
# print('열(세로)의 평균:', np.mean(arr, axis = 0))
# # 각 열의 최솟값
# print('열(세로)의 최소값:', np.min(arr, axis = 0))

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print('concatenate로 가로 병합:\n', np.concatenate((a, b), axis = 1))
print('hstack로 가로 병합:\n', np.hstack((a, b)))

print('concatenate로 세로 병합:\n', np.concatenate((a, b), axis = 0))
print('vstack로 가로 병합:\n', np.vstack((a, b)))

h1 = np.array([1, 2, 3])
h2 = np.array([4, 5, 6])
print('hstack수평병합1:\n', np.hstack((h1,h2)))
# h1과 h2는 1차원임. ndim =1 이 유지되어 병합됨.
print('stack with axis 수평병합2:\n', np.stack((h1,h2), axis = 1))
# stack((h1, h2), axis =1)은 차원이 하나가 더 생성되어 1차원이었던 h1과 h2가 2차원으로 됨.

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print('vstack 수직병합1:\n', np.vstack((v1,v2)))
print('stack with axis 수직병합2:\n', np.stack((v1,v2), axis = 0))