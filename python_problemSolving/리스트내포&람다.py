
# for 반복문
# for 숫자변수 in 범위:
#   코드

# for 구구단

for a in range(2, 10):
    for b in range(2, 10):
        print(a * b, end=" ") 

# a가 2부터 시작 -> b가 1~10까지 반복
# 그다음 a 3부터 시작 -> b가 1~10까지 반복
# 순서 중요할 듯

# 리스트 내포

array = []
for i in range(0, 20, 2):
    array.append(i*i) #array 리스트에 0~20 사이의 짝수들의 제곱들을 넣음
print(array)


array1 = [i*i for i in range(0, 20, 2)]
print(array1)

a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3) # a 리스트 안에 있는 요소를 3씩 곱한 다음 result 리스트 안에 넣음
print(result)
# -> 리스트 내포로 한다면?
b = [1, 2, 3, 4]
result2 = [num * 3 for num in b]
print(result2)

# 리스트 내포: for 과 if

a = [1, 2, 3, 4]
result = [num * 3 for num in a if num %2 == 0]

# num %2 == 0 은 0으로 나눌 때 0이라면 넣음 즉, 짝수만.
# [표현식 for 반복자 in 반복가능객체(리스트 or range) if 조건문]

# 리스트 내포 for 문 2개이상
# 표현식 for 반복자1 in 반복가능객체1 if 조건1
#        for 반복자2 in 반복가능객체2 if 조건2
#        for 반복자3 in 반복가능객체3 if 조건3

result = [x*y for x in range(2, 10) for y in range(1, 10)]
print(result)

# 람다 함수: 함수를 매개변수로 전달하기 위한 한줄 정의 def 함수
# map(함수, 반복가능객체): 리스트의 요소를 함수에 넣고 리턴된 값으로 새로운 리스트 구성
# filter(함수, 반복가능객체): 반복가능객체의 요소를 함수에 넣고 리턴된 값이 True인 것으로 새로운 리스트를 구성
# filter와 map 함수를 사용하기 위해선 매개변수 1에 함수를 넣어야 하므로 함수 정의가 필요함
# 함수를 따로 일일히 정의하기 힘드므로 lambda 함수 사용
# lambda 매개변수 1, 매개변수 2 ... : 매개변수를 이용한 표현식
# = lambda 매개변수 : 리턴값

def add (x, y):
    return x + y
print(add(1,3))

# 이것을 람다함수를 사용해서 표현한다면
func = lambda x, y : x+y # 한줄로 입력 가능한 람다함수
print(func(1,2))


def flunk(x):
    return x < 60

# a = flunk(30)
# print(a)

score = [35, 67, 45, 21, 81]
result = list(filter(flunk, score))
print(result)

# 이걸 람다함수를 사용한다면?
score = [35, 67, 45, 21, 81]
result = list(filter(lambda x : x < 60, score))
print(result)

def half(x):
    return x/2
score = [35, 67, 45, 21, 81]
result = list(map(half, score))
print(result)

# 람다함수 사용한다면
score = [35, 67, 45, 21, 81]
result = list(map(lambda x: x/2, score))
print(result)


def power(item):
    return item * item
def under_3(item):
    return item > 3

input_a = [1, 2, 3, 4, 5]

output_a = list(map(power, input_a))
print("# map() 함수의 실행결과")
print("map(power, input_a):", output_a)
print()

output_b = list(filter(under_3, input_a))
print("# filter() 함수 실행결과")
print("filter(under_3, input_a): ", output_b)

# filter와 map 함수를 사용하기 위해선 매개변수 1에 함수를 넣어야 하므로 함수 정의가 필요함
# 함수를 따로 일일히 정의하기 힘드므로 lambda 함수 사용


power = lambda item: item * item
under_3 = lambda item: item < 3

input_a = [1, 2, 3, 4, 5]
output_a = list(map(power, input_a))
output_b = list(filter(under_3, input_a))

print("# map() 함수 실행결과")
print("map(power(함수), input_a(반복가능객체): ", input_a)

print("# filter() 함수 실행결과")
print("filter(under_3(함수), input_a) : ", output_b)

# output_a = list(map(power, input_a))
output_a = list(map(lambda item: item * item, input_a))
# output_b = list(filter(under_3, input_a)) 이것을 람다함수 사용한다면 따로 under_3 라는 변수 안만들어도 됨
output_b = list(filter(lambda item: item < 3, input_a))

files = ['color','happy.png','sky.jpg','spec.xslx','report.hwp']
exp = filter(lambda x: 'hwp' in x or 'xslx' in x or 'doc',files)
doc_list = list(exp)
print(doc_list)