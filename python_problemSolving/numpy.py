import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
print(f"시도1: {arr1}\n")

arr2 = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
print(f"시도2:\n{arr2}\n")

arr3 = np.array([[1, 2, 3],[1, 2, 3]])
print(f"시도3:\n{arr3}\n")

arr4 = np.array([[1, 2, 3, 4], [1, 3, 5]]) #행 2개의 열 길이가 같지 않을 땐 list() 각각 반환하는건가
print(f"시도4:\n{arr4}\n")

print(np.zeros(10)) #float 실수가 디폴트

# 1차원, 2차원, 3차원 배열
import numpy as np
arr1 = np.array([1, 2, 3, 4])
print(f"1차원 배열:\n{arr1}\n")

arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(f"2차원 배열:\n{arr2}\n")

arr3 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                 [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
                 [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])
print(f"3차원 배열:\n{arr3}\n")

a = np.array([[1, 2, 3, 7],[4, 5, 6, 8]])
#  a = np.array([[1, 2, 3, 7],[4, 5, 6]])
# [list([1, 2, 3, 7]) list([4, 5, 6])] (행과 열의 길이가 맞지 않으면 리스트로 반환하는 것 같다.)
print(a)

zeros1 = np.zeros(3)
zeros2 = np.zeros((3,3))
zeros3 = np.zeros((3,3,3))
print(f"""
zeros1결과:\n{zeros1}\n
zeros2결과:\n{zeros2}\n
zeros3결과:\n{zeros3}
""")

ones1 = np.ones(10)
ones2 = np.ones((2,2))
ones3 = np.ones((2,2,2))
print(f"""
ones1결과:\n{ones1}\n
ones2결과:\n{ones2}\n
ones3결과:\n{ones3}
""")

ara = np.arange(1,11) # np.aragne(x, y): x부터 y전까지의 배열생성
print(ara)
# ara2 = np.arange((1,11, 3)) 실행안됨
arr = np.arange(1,10)
print('ndim:', arr.ndim) #ndim: 1 ndim은 무엇이지?
print('shape:', arr.shape) #(9,)

import numpy as np
# arr4 = np.array([[1, 2, 3, 4], [1, 3, 5]])
# print(f"시도4:\n{arr4}\n")

# zeros(): 지정된 shape 배열 만든 후 모든 요소 0으로
a = np.zeros(3)
print(f'np.zeros(3)의 결과:\n{a}\n')
b = np.zeros([2, 3]) #원소가 0이고 2행 3열인 2차원 배열
print(f'np.zeros([2, 3])의 결과:\n{b}\n')
c = np.zeros((2, 3))
print(f'np.zeros((2, 3))의 결과:\n{c}\n')
d = np.zeros(3, dtype= int) #소수점이 붙어진 float 실수형이 아닌 정수형
print(f'np.zeros(3, dtype= int)의 결과:\n{d}\n') 
e = np.zeros((2,3,4), dtype = 'i') # 행 3개, 열 4개, 축 2개인 배열 그리고 정수형 타입의 3차원 배열
print(f'e = np.zeros((2,3,4))의 결과:\n{e}\n')

# order에 대한 이해 'c'는 행을 우선으로 요소를 넣음. 'f'는 열을 우선으로 요소를 넣음
array = np.arange(18)
print(array)
arrayC = np.reshape(array, (2, 9), order = 'C') # (2, -1) -1은 대체 뭐지?
arrayF = np.reshape(array, (3, 6), order = 'F') 
print(f'행 우선:\n{arrayC}\n')
print(f'열 우선:\n{arrayF}\n')
# -1은 데이터 갯수를 자동으로 계산해주는 나머지 자동계산
# 행과 열 둘중에만 -1 사용가능

# one(): 지정된 shape 배열 만든 후 모든 요소 1로
one1 = np.ones(4)
print(f'one1의 결과:\n{one1}\n')
one2 = np.ones((4, 4))
print(f'one2의 결과:\n{one2}\n')
one3 = np.ones((2, 3))
print(f'one3의 결과:\n{one3}\n')
one4 = np.ones((2, 3), dtype= 'i')
print(f'one4의 결과:\n{one4}\n')

# full(): 지정된 shape 배열 생성 후 모든 요소를 지정한 값으로
full1 = np.full((3, 3), 4) #행3, 열3 생성 후 모든 요소를 4로
print(f'np.full((3, 3), 4) 결과:\n{full1}\n' )
full2 = np.full(5, 3) #1차원 행1개만 생성 후 모든 요소를 3으로
print(f'np.full(5, 3) 결과:\n{full2}\n')
full3 = np.full((4,2), 3, dtype= float)
print(f'np.full((4,2), 3, dtype= float) 결과:\n{full3}\n')


# identity(): (정사각형)대각행렬. 대각선이 1인 행렬
identity1 = np.identity(n = 4, dtype = int)
print(f'np.identity(n = 4, dtype = int) 결과:\n{identity1}\n')

# eye(): (직각, 정사각형) 단위행렬함수
eye1 = np.eye(3)
print(f'eye1의 결과:\n{eye1}\n')
eye2 = np.eye(N=3, M=5, k=1, dtype=int)
print(f'eye2의 결과:\n{eye2}\n')
# 행렬 크기 3*5 identity matrix 시작은 1열부터 시작

# ??
# reshape(5, -1) -1은 대체 뭘까

# empty()
em1 = np.empty((3,3), dtype = int)
print(f'em1결과:\n{em1}\n')

# arange()
arange1 = np.arange(1, 11, 2) #1부터 11까지 2개 간격으로
print(f'np.arange(1, 11, 2)결과:\n{arange1}\n')
arange2 = np.arange(1, 11,  dtype = float)
print(f'np.arange(1, 11, 2)결과:\n{arange2}\n')

# linspace(): 요소 개수 기준으로 균등한 간격의 배열 생성
lin1 = np.linspace(0, 10, 5) #0부터 10사이를 5개로 균등한 간격으로 배열 생성
print(f'lin1결과:\n{lin1}\n')
lin2 = np.linspace(1, 2, 10) #1부터 2사이를 10개로 균등한 간격으로 배열생성
print(f'lin2 결과:\n{lin2}\n')
endpoint = np.linspace(1, 2, 10, endpoint=False) #endpoint = False로 끝점 포함x
print(f'endpoint=False 결과:\n{endpoint}\n')
retstep = np.linspace(1, 2, 10, endpoint= False, retstep = True)
print(f'retstep = True결과:\n{retstep}\n') #간격이 0.1 이라는 것을 알 수 있음.

# logspace(): 로스 스케일의 linspace 함수. 로그 스케일로 요소 개수 기준으로 균등한 간격 배열 생성
log1 = np.logspace(1, 2, 5)
print(log1)

# 난수
# randint
int1 = np.random.randint(1, 10)
print(f'int1 결과:\n{int1}\n') #랜덤으로 정수 1개만 나옴
int2 = np.random.randint(1, 33, (4, 8))
print(f'int2 결과:\n{int2}\n') #4*8 배열 생성 후 랜덤으로 1부터 33 미만의 사이의 숫자 랜덤으로 요소 넣음

arr = np.arange(1, 11)
print(arr)
print('ndim:', arr.ndim) #ndim은 최솟값?
print('shape:', arr.shape)
print('dtype:', arr.dtype)
print('size:', arr.size)
reshape = arr.reshape(2,5)
print(f'행렬을 2차원으로 2*5로 바꾸기\n{reshape}\n')

# 슬라이싱
test = np.arange(1, 25).reshape(3, 8)
print(f'test:\n{test}\n')
print('1행:', test[1])
print('1행부터 끝까지:\n', test[1:])
print('0행부터 1행까지\n', test[0:2])
print('역순 시작으로 1행:\n', test[-1:])
print('역순 시작으로 2행:\n', test[-2:])
print('역순 시작으로 3행:\n', test[-3:])
print('2칸 간격으로:\n', test[::2])
print('[1::2] 1행부터 끝까지 2칸 간격으로 \n', test[1::2])
print('[::-1] 행을 처음부터 끝까지 1칸 간격으로 역순\n', test[::-1])

matrix = np.arange(1, 25).reshape(3, 8)
print(matrix)
print('')
print('1~2행에서 1~3열:\n', matrix[1:3, 1:4])
print('0~2행에서 0~2열:\n', matrix[:3, :3])
print('행: 처음부터 2칸 간격 & 열: 1열부터 3칸 간격:\n', matrix[::2, 1::3])
print('행: 2행부터 & 열: 역순으로 시작해서 2칸 간격으로:\n', matrix[2:, ::-2])
print('행: 0~3행을 2칸 간격으로:\n', matrix[0:3:2])


# Boolean 인덱싱
num = np.arange(1, 6)
print(num)
Booleans = [True, False, False, True, False]
print(num[Booleans]) # [1, 4] 해당 인덱스의 True만을 조회
# Boolean 요소와 배열 요소의 갯수가 같지 않다면?
# num1 = np.arange(1,6)
# Booleans1 = [True, False, False, True, False, False] 
# print(num1[Booleans1]) # 배열의 갯수보다 Boolean의 갯수가 많을 땐 오류
# IndexError: boolean index did not match indexed array along dimension 0; dimension is 5 but corresponding boolean dimension is 6
# num2 = np.arange(1, 5)
# Booleans2 = [True, False, False, True, False]
# print(num2[Booleans2]) # 배열의 갯수보다 Boolean의 갯수가 적을때 오류
# IndexError: boolean index did not match indexed array along dimension 0; dimension is 4 but corresponding boolean dimension is 5

# num1 = np.arange(1,11).reshape(2, 5)
# print(num1)
# Booleans1 = ['True, False, True, False, True\nTrue, False, True, False, True'] 
# print(num1[Booleans1])
# 문자형태는 받지 않나보구만. 에러 뜸

# 넘파이 배열 형태 변경
x = np.arange(20)
y = x.reshape(4, 5)
print(y)
x[0] = 10
print(x)
print(y)

listdata = [1, 2, 3, 4, 5, 6]
# print(listdata.reshape(3,2)) #리스트는 형변환 불가능
data = np.array(listdata) #리스트를 배열로 변경.
print('listdata 타입: ', type(listdata))
print('data타입: ', type(data))
print(data.reshape(3,2)) # 배열은 형변환 가능


# resize(객체, (원하는 배열모양)) : 배열 모양 변경 중 배열 원소 수 줄이거나 늘임
x = np.arange(20) #총 20개
print('resize 전: \n', x)
y = np.resize(x, (5,4)) # 원소에 변경 x
print('resize 후: \n',y)
#원소 하나를 다른 것으로 바꾼다면?
# resize는 원래 배열과 동일한 메모리를 공유하지 않기 때문에 데이터 변경은 다른 배열에 매핑x
x[0] = 10 
print('변수 x로 접근해 y의 원소 바꾸기: \n' ,y)
y[0] = 10
print('변수 y로 접근해 y의 원소 바꾸기: \n' ,y)

ResizeExtend = np.resize(x, (5,6)) #열이 2개 늘어남. 원소개수 20->30
print('열 원소 증가: \n',ResizeExtend)
ResizeReduce = np.resize(x, (5,3)) #열이 3개로 줄어듬. 원소개수 20 -> 15
print('열 원소 감소: \n',ResizeReduce)
# TestReshape = np.reshape(x, (5,3)) #reshape는 원소의 갯수를 조작 불가능

# append(객체, 원소, axis) : 원소 끝에 배열 및 원소 추가 (axis로 추가 축 지정)
a = np.arange(3)
a_Append = np.append(a, 3) #3을 끝에 집어넣음.
print(a_Append)

b = np.arange(1, 11).reshape(2, 5)
print(b)
b_Append = np.append(b, 11)
print(b_Append)
# 축을 지정하지 않으면 1차원 배열로 변환되어 추가됨

# arr1 = np.array([[1, 2, 3],[4, 5, 6]])
# arr2 = np.array([[7, 8, 9]])
# arr3 = arr2.reshape(3,1)
# print(arr3)
# arr1_Append = np.append(arr1, arr2)  #축 지정x
# arr1_Append0 = np.append(arr1, arr2, axis = 0) # axis = 0 행 기준
# arr1_Append1 = np.append(arr1, arr3, axis = 1) #오류남
# print(arr1_Append)
# print(arr1_Append0)
# print(arr1_Append1)

# insert(객체, 위치(축), 추가할 원소) : 지정 위치에 원소 추가
a = np.array([1, 2, 3])
b = np.insert(a, 1, 5)
print(a)
print(b)

a1 = np.array([[1, 1],[2, 2],[3, 3]])
b1 = np.insert(a1, 1, 5)
print('a1: \n',a1)
print('b1: \n',b1)
# 축 지정x -> 1차원 배열로 변환 후 1첫째 위치에 5를 추가함

a2=np.array([[1, 1], [2, 2]])
b2=np.insert(a2, 1, 5, axis=0) #행 기준으로 넣음
c2=np.insert(a2, 1, 5, axis=1) # 열 기준으로 넣음
print('a2: \n',a2)
print('b2: \n',b2) 
print('c2: \n',c2)

# delete(객체, 원소 or 축)): 배열의 원소 또는 축 삭제
del1 = np.arange(1, 13).reshape(3,4)
print(del1)
print(np.delete(del1, 1))
# 축 지정하지 않으면 1차원으로 변환 후 삭제됨
print('행기준 axis = 0\n', np.delete(del1, 1, axis = 0)) #행 기준 첫번째 행 삭제됨.
print('열기준 axis = 1\n',np.delete(del1, 1, axis = 1)) #열 기준 첫번째 열 삭제됨

# 배열 결합, 병합
# 1. concatenate((객체1, 객체2), axis): axis로 병합 축 지정
Con1 = np.array([[1, 2, 3]])
Con2 = np.array([[4, 5, 6]])
Con_axis0 = np.concatenate((Con1, Con2), axis = 0)
print('axis 0 행 기준 병합: \n', Con_axis0)
Con_axis1 = np.concatenate((Con1, Con2), axis = 1)
print('axis 1 열 기준 병합: \n', Con_axis1)

# 2. hstack((객체1, 객체2)) : 수평병합 / 괄호 2개 주의!
h1 = np.array([1, 2, 3])
h2 = np.array([4, 5, 6])
print('수평병합1:\n', np.hstack((h1,h2)))
# 3. vstack((객체1, 객체2)) : 수직병합 / 괄호 2개 주의!
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print('수직병합1:\n', np.vstack((v1,v2)))

h1 = np.array([1, 2, 3])
h2 = np.array([4, 5, 6])
print('수평병합2:\n', np.stack((h1,h2), axis = 1))
# 3. vstack((객체1, 객체2)) : 수직병합 / 괄호 2개 주의!
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print('수직병합2:\n', np.stack((v1,v2), axis = 0))

# h or v stack의 차이와 stack with axis의 차이 찾아보기
# 차원이 높아지는 것과 차원이 유지되면서 합해지기 찾아보기

# concatenate는 차원이 증가하지 않고 병합
# h or v stack도 차원이 증가하지 않고 병합
# stack with axis는 새로운 축을 생성하고 연결.
# stack은 ndim의 수 증가. concatenate, hstack, vstack은 ndim수 똑같음
#  -> stack은 병합하려는 각 객체들의 차원 수가 동일하지 않아도 병합 가능
#  -> concatenate, hstack, vstack은 각 객체들의 차원 수가 동일하지 않으면 error

# 홀수 행이나 홀수 열은 나눌 수 없다. 딱 반으로 나눌 수 없어서. 딱 맞아 떨어져야 나눌 수 있음.
# 행과 열의 갯수를 나눌 때 그 갯수의 약수로 나눠야만 나눌 수 있음

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
print('arr4+arr5 수평병합3: \n', arr8)
# stack은 축을 새로 생성한 후 병합하기 때문에 다름

import numpy as np
# 브로드캐스팅 사용하지 않을 때
a = np.arange(1, 6)
# a = [1, 2, 3, 4, 5]
b = np.ones((1, 5), dtype = int)
# b = [1, 1, 1, 1, 1]

print(a+b)
# a+b = [1+1, 2+1, 3+1, 4+1, 5+1]

# 브로드캐스팅 사용!
b = 100
print('브로드캐스팅 사용시: ', a+b)

a = np.arange(1, 11).reshape(2, 5)
b = 100
print('브로드캐스팅 방법1: \n', a+b, '\n')
print('브로드캐스팅 방법2: \n', a+100, '\n')

a = np.arange(5).reshape((1,5))
print(a)
b = np.arange(5).reshape((5, 1))
print(b)

print('a+b : \n', a+b)

Children = np.arange(1, 25).reshape(3, 8)
print(Children)

print('5세 평균 학급당 유아수: 28명')
print('4세 평균 학급당 유아수: ', 194/8)
print('3세 평균 학급당 유아수: ', 108/6)


import numpy as np

# arr1 = np.array([[1, 2, 3],[4, 5, 6]])
# arr = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
# arr2 = np.array([[7, 8, 9]])
# arr3 = arr2.reshape(3,1)
# print(arr3)
# arr1_Append = np.append(arr1, arr2)  #축 지정x
# print('arr1 + arr2: \n' ,arr1_Append)

# arr1_Axis0 = np.append(arr1, arr2, axis = 0) # axis = 0 행 기준
# print('arr1 + arr2 (axis = 0) : \n', arr1_Axis0)

# # arr1 으로 넣었을 땐 행이 하나 부족해서 에러가 남
# # arr으로 넣었을 땐 arr3와 arr1의 행과 열의 갯수가 같아 append 가능
# arr1_Axis1 = np.append(arr, arr3, axis = 1) 
# print(arr1_Axis1)


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