import numpy as np
# 실습문제
arr = np.arange(1, 11)
print(arr)
print('ndim:', arr.ndim) #ndim은 최솟값?
print('shape:', arr.shape)
print('dtype:', arr.dtype)
print('size:', arr.size)
arr2 = np.arange(1, 11).reshape(2, 5)
print(arr2)
print("ndim 차원 수, 배열의 축 수:", arr2.ndim) #

a1 = np.arange(6)
print(a1)
print(a1[::2])

# 7주차 실습문제1
# 다음 코드를 완성하시오.
import numpy as np
arr= np.arange(1, 21)   
print(arr)             
print('마지막 원소:', arr[19])
print('모든원소의 합:', arr.sum(),',' ,np.sum(arr))
print('모든원소의 평균:',arr.mean(),',' ,np.mean(arr))
new_arr = arr.reshape(4,5)
new_arr2 = np.reshape(arr, (4, 5))
print(new_arr)
print(new_arr2)

# 7주차 실습문제2
# 다음 코드를 완성하시오
import numpy as np
salary=[200,150,180,220,250]
new_salary=np.array(salary,dtype='float64')*1.5 
#salary의 데이터 형을 실수로 바꾼 후 각 원소에 1.5배 곱함
print('인상된 금액 :',new_salary)
avg_salary= np.mean(new_salary) 
avg_salary2 = new_salary.mean()
print(f'평균 금액 :{avg_salary}, {avg_salary2}')
result=(new_salary >= avg_salary)
평균이상 = new_salary[result]
print('평균이상인 원소 :',new_salary[result])
print(f'평균이상인 원소의 개수 : {평균이상.size}, {np.size(평균이상)}')

# 7주차 도전문제1
import numpy as np
arr=np.random.random((6,5))
arr=np.round(arr*100,2)
print(arr)
# 전체의 최댓값
print('전체 최대값:', np.max(arr), arr.max())
# 각 행의 합
print('행(가로)의 합:', np.sum(arr, axis = 1))
# 각 행의 최댓값
print('행(가로)의 최대값:', np.max(arr, axis = 1))
# 각 열의 평균
print('열(세로)의 평균:', np.max(arr, axis = 0))
# 각 열의 최솟값
print('열(세로)의 최소값:', np.min(arr, axis = 0))

# 7주차 도전문제2
#3-1 정수 1~100 사이의 10*10 배열을 생성
import numpy as np
arr1= np.arange(1, 101).reshape(10, 10)
print(arr1)

#3-2 위 arr1 배열을 10*5 배열 2개로 분할
arr2, arr3 = np.hsplit(arr1, 2)
print('arr2: \n',arr2)
print('arr3: \n',arr3)

#3-3 위 arr2 배열을 5*5 배열 2개로 분할 후 수평으로 병합
arr4, arr5 = np.split(arr2, 2, axis = 0)
print('arr4:\n', arr4)
print('arr5:\n', arr5)

arr6 = np.hstack((arr4, arr5))
print('arr4+arr5 수평병합1: \n', arr6)

arr7 = np.concatenate((arr4, arr5), axis = 1)
print('arr4+arr5 수평병합2: \n', arr7)

arr8 = np.stack((arr4, arr5), axis = 1)
print('arr4+arr5 stack with axis 병합3: \n', arr8)
# stack은 축을 새로 생성한 후 병합하기 때문에 다름