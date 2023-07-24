# <기본형 강의 1~2>
# 변수

animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

# 애완동물을 소개해 주세요~
print("우리집 " + animal + "의 이름은 " + name + "에요")
print(name + "는 " + str(age) + "이며, " + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요?" + str(is_adult))

# 여기서 연탄이의 이름을 해피로 바꿔야 한다면?
# 사람이 일일히 바꾼다면 놓칠 수 있는 부분이 있을 수 있어서 변수를 사용
# 변수란 값을 저장하는 공간


#정수와 boolean(참과 거짓)은 str()를 써서 해야 함
# 띄어쓰기와 str() "", ++ 표시 잘 확인하기

#,로도 표현 가능

print("우리집 " + animal + "의 이름은 " + name + "에요")
hobby = "달리기"
print(name, "는 ", age, "이며, ", hobby,"을 아주 좋아해요")
print(name + "는 어른일까요?" + str(is_adult))

# = 주석 : 프로그램 코드 내엔 포함되어 있지만 실행되지 x
# 여러 문장을 주석처리 할 경우
''' 이번엔
이렇게 
예시를
해볼까?'''

 

#주석 해제시에도 드래그 후 ctrl + /

# quiz) 변수를 이용하여 다음 문장을 출력하시오.
# - 변수명 : Station
# - 변수 값 : "사당", "신도림", "인천공항" 순서대로 입력
# - 출력 문장: XX행 열차가 들어오고 있습니다.


# <기본형 강의3>
print(1+1)
print(3-2)
print(5*2)
print(6/3)

#2의 3승
print(2**3)

#나누기에서 나머지 값
print(5%3)
print(10%3)

#나누기에서 몫 구하기
print(5//3)
print(10//3)

#크거나 같다도 가능
print(4 >= 7)
print(10 > 3)
print(5 >= 3)

# 앞의 값과 뒤의 값이 같은지
print (3 == 3)
print(4 == 4)
print(3 + 4 == 7)

# 같지 않다도 가능
print(1 != 3)
#not은 실제 값의 반대를 표현함
print(not(1 != 3))

#2개 이상의 항을 한번에 연산
print(( 3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))
#만약 2개의 항 중 하나만 틀려도 False 나옴

#앞의 항이나 둘 중 하나만이라도 만족해도 True 가 나오려면?
print((3 > 0) or (3 > 5))
print((3 > 0) | (3 > 5))

print( 5 > 4 > 3)
print(5 > 4 > 7)

#간단한 수식
print(2 + 3 * 4)
print((2 + 3) * 4)
number = 2 + 3 * 4
print(number)
number = number + 2
print(number)
number += 2
print(number)
number *= 2
print(number)
number /= 2
print(number)
number -= 2
print(number)
number %= 5
print(number)
# %는 나머지 구함

#///#


# 숫자 처리 함수
#절댓값: abs, pow:제곱, max: 큰 수 표현, min: 작은 수 표현,round:반올림
print(abs(-5))
print(pow(4, 2)) #4^2 = 4*4
print(max(5, 12))
print(min(5, 12))
print(round(3.14))
print(round(4.99))

# math library를 이용
from math import *
# math란 library 안에 있는 모든 것들을 이용
# floor은 내림
print(floor(4.99))
# ceil은 올림
print(ceil(3.14))
# sqrt는 제곱근
print(sqrt(16))

#랜덤 함수
#무작위로 숫자 선정
from random import *
print(random()) #0.0~1.0 의 미만의 임의의 값 생성
print(random() * 10) #0.0 ~ 10.0 미만의 임의의 값 생성
#소숫점 없이 온리 정수만
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10))
print(int(random() * 10))

#만약 1로 시작하고 싶다면?
print(int(random() * 10) + 1)
print(int(random() * 10) + 1)
print(int(random() * 10) + 1)

#로또 번호처럼 1~45숫자
print(int(random() * 45) + 1) # 1 ~ 45 이하이 임의의 값
print(randrange(1, 46)) #1 ~ 46미만의 임의의 값 생성
print(randint(1, 45)) # a, b를 포함한 그 사이의 값 생성

# Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

# 조건 1 : 랜덤으로 날짜를 뽑아야 함.
# 조건 2 : 월별 날짜는 다름을 감안하여 최소 일수인 28일 이내로 정함
# 조건 3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

# (출력문 예제)
# 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.

date = randint(4, 28)
date = randrange(4, 29)
date = int(random() * 28) + 4
print("오프라인 스터디 모임 날짜는 매월" + str(date) + "일로 선정되었습니다.")

# <기본형 강의 4>
# 문자형 '' 차이, ""차이, """을 이용해 여러 문장을 한번에 줄바꿔서 만들기
sentence = 'my name is Hyebin'
print(sentence)
sentence2 = "i wanna be a teacher"
print(sentence2)
sentence3 = """
my name is hyebin
and i wanna be a teacher
"""
print(sentence3)

#슬라이싱
# : text 에서 어느 한 부분만 가지고 와서 쓰고싶은 경우
code = "000924-4352617"

print("성별 :" + code[7])
print("생년 :" +code[0:2]) #0부터 2 직전까지 즉 0, 1
print("생월 :" +code[2:4])
print("생일 :" +code[4:6])
print("생년월일" +code[0:6])
print("뒤 7자리" +code[7:])
print("뒤 7자리(뒤에서부터) :" +code[-7:])

#문자열 처리함수
python = "Python is Amazing"
print(python.lower()) #모든 글자를 소문자로
print(python.upper()) #모든 글자를 대문자로
print(python[0].isupper()) #첫글자가 대문자인지 검사
print(len(python)) # python의 문장 길이를 다 나타냄
print(python.replace("Python", "Java")) #특정 문자를 다른 문자로 변환

index= python.index("n")
#n이란 글자가 어느 위치에 있는지 숫자로 표시
print(index)
index = python.index("n", index + 1)
#2번째 n의 위치 표시
print(index)
print(python.find("n"))

# '''find 함수와 index 함수의 차이 :
# print(python.find("Java")) #java란 단어가 없기 때문에 -1로 표시
# print(python.index("Java")) #여기선 index에 java란 단어가 없기 때문에 에러남'''

# n이 몇번이나 표시되었는지 확인
print(python.count("n"))

# 문자열 포맷
# print("a" + "b") -> ab
# print("a", "b") -> a b이외에도 포맷하는 방법

#방법 1 : %
print("나는 %d살 입니다" % 20) #d는 무조건 정수만 표현
print("나는 %s을 좋아해요" % "파이썬") #s는 문자열
print("Apple 은 %c로 시작해요." % "A") #c는 캐릭터 한 글자만
print("나는 %s와 %s을 좋아해요" % ("운동", "음악"))

#방법 2 :{} & .format()
print("나는 {}살입니다.".format(20))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨강"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨강"))

#방법 3 :{} & .format(age = , color = )
print("나는 {age}살이고, {color}색을 좋아해요.".format(age = 22, color = "검정"))

#방법 4 :
age = 22
color = "검정"
print(f"나는 {age}살이며, {color}색을 좋아해요")

#탈출문자 : \n 줄바꿈
print("""백문이 불여일견 
백견이 불여일타""")

# print("백문이 불여일견
# 백견이 불여일타") -> 이렇게 하면 오류남 so 탈출문자 \n을 사용함

print("백문이 불여일견\n백문이 불여일타")
# print("나는 "윤혜빈"입니다") 라고 하면 문자열을 인식하는 ""가 두개가 들어가 오류남 so
print('나는 "윤혜빈"입니다')
print("나는 \"윤혜빈\"입니다")
print("i'm Yun Hyebin")
print('i\'m Yun Hyebin')

#\\ : 문장 내에서 하나의 \
print("C:\\Users\\msi\\Desktop\\python work space>")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

#\b : 백스페이스(한 글자 삭제)
print("Redd\bApple")

#\t : Tab 역할
print("Red\tApple")

#Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.
# 예) http://naver.com 
# 규칙1 : http:// 부분은 제외 => naver.com 
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver 
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
#                (nav)                (5)         (1)              (!)
# 예) 생성된 비밀번호 : nav51!

# <기본형 강의 5>
# 5-1 리스트 [] : 순서를 가지는 객체 집합

#지하철 칸별로 10, 20, 30명이 타고 있음
subway1 = 10
subway2 = 20
subway3 = 30
# 이것들을 하나로 연속적인 공간에 묶기
subway = [10, 20, 30]
print(subway)
subway = ["유재석", "조세호", "박명수"]
print(subway)

#조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))
# 유재석은 0번째칸, 조세호는 1번째칸, 박명수는 2번째칸

#다음 정류장에 하하씨가 다음 칸에 탐
#~~.append = 더하다는 뜻
subway.append("하하")
print(subway)

#정형돈씨를 유재석과 조세호 사이에 태워봄
#~~.insert
subway.insert(1, "정형돈")
print(subway)

#지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

#같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# #순서 뒤집기 가능
num_list.reverse()
print(num_list)
#모두 지우기
num_list.clear()
print(num_list)

#다양한 자료형 함께 사용
num_list = [5,4,3,2,1]
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장 (2개 이상의 리스트 합치기)
num_list.extend(mix_list)
print(num_list)

# 5-2 사전 : 단어를 찾을 수 있고 단어에 대한 설명이 나옴 {}
# 예를 들어 사우나에서 특정 키를 가지고 해보자
cabinet = {3 : "유재석", 100 : "김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
#그럼 유재석이 어떤 키를 가지고 있는지 찾을 수 있나?
# print(cabinet[5])라고 하면 5라는 키를 가지고 있지 않기 때문에 오류발생
# print(cabinet.get(5))를 하면 5라는 키를 가지고 있지 않기 때문에 none 이라고 나옴
print(cabinet.get(5, "사용 가능"))

#캐비넷에 3과 5라는 키가 있는지 확인하려면?
print(3 in cabinet)
print(5 in cabinet)

cabinet = {"A-3" : "유재석", "B-100" : "김태호"}
print(cabinet.get("A-3"))
print(cabinet.get("B-100"))

#새 손님이 와서 캐비넷에 할당하려면?
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["c-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

#key들만 출력
print(cabinet.keys())
#value들만 출력
print(cabinet.values())
#key, value 쌍으로 출력
print(cabinet.items())

#목욕탕 폐점
cabinet.clear()
print(cabinet)

# 5-3 튜플 : 내용 변경이나 추가할 수 없음 but 속도가 리스트가 빠름 so 변경되지 않는 리스트
menu = ("돈가스", "치즈까스")
print(menu[0])
print(menu[1])

#메뉴 추가하고 싶어서 했다면?
# menu.add("생선까스") -> error
#튜플은 add 라는 함수를 쓰지 않음

# 튜플 다른거 예시
# name = "윤혜빈"
# age = 22
# hobby = "코딩"
# print(name, age, hobby)
#이거를 튜플을 이용한다면?

(name, age, hobby) = ("윤혜빈", "22", "코딩")
print(name, age, hobby)

# 5-4 세트 = 집합
#중복 안됨, 순서 없음
my_set = {1,2,3,3,3} #r값만 나열
print(my_set)

my_set = {1,3,2,2,2}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])
#? 근데 만약 set ([])안하면 어떻게 될까? 실험 유무 [ ]
#교집합 (java와 python 모두 개발할 수 있는 사람)
print(java & python)
print(java.intersection(python))

#합집합 (java 할 수 있거나 python  둘 중 하나할 수 있는 사람)
print(java | python)
print(java.union(python))

#차집합(java를 할 수 있지만 python을 할 수 없는 개발자)
#즉 java - python
print(java - python)
print(java.difference(python))

#교육을 받아서 python 할 줄 아는 사람이 늘어남
#so python 집합에 사람을 넣으려고 할 떄
python.add("김태호")
print(python)

#김태호가 java를 까먹어서 java 집합에서 뺴려할 떄
java.remove("김태호")
print(java)

# 5-5 자료구조의 변경
#커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

#퀴즈 4
from random import *
# users = [ 1,2,3,4,...]을 하기엔 너무 길어 그러니
users = range(1, 21) # 1부터 20까지 숫자를 생성
#print(type(users)) #하면 range는 list가 아니여서 list에서 쓰고자 하는 함수를 사용못함 so
users = list(users)
#print(type(users))

shuffle(users)
print(users)

# 무작위로 추첨하되 중복은 불가능하니 한번에 4명을 뽑아보도록 합니다
winners = sample(users, 4)
print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print(" -- 축하합니다 -- ") 

# <6-1> if : 이런 상황에선 A실행, 저런 상황에선 B 실행하라
weather = "비"
# if 조건 : 
#     실행 명령문
if weather == "비" :
    print("우산을 챙기세요")
elif weahter == "미세먼지" :
    print("마스크를 챙기세요")
else:
    print("준비물이 필요 없어요.")

# #if 첫째 문장에서 조건이 들어맞으면 실행 후 바로 빠짐
# 첫째 조건이 성립안되면 두번쨰 조건 elif로 실행 후 바로 빠짐
#  두번째 조건 elif의 조건이 성립안되면 그 외의 else로 실행후 빠짐
# else가 없다면 출력이 아예없음.
weather = input("오늘 날씨는 어때요? ")
if weather == "비" or weather == "눈" :
    print("우산을 챙기세요")
elif weather == "미세먼지" :
    print("마스크를 챙기세요")
else:
    print("준비물이 필요 없어요.")

# input은 항상 값을 문자열로 받기 때문에 가끔 int 함수가 필요

temp = int(input("기온은 어때요? "))
if 30 <= temp :
    print("너무 더워요. 나가지 마세요.")
elif 10 <= temp and temp < 30 :
    print("괜찮은 날씨에요")
elif 0 <= temp < 10 :
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요.")

# <6-2> for : 반복문
# print("대기번호 : 1")
# print("대기번호 : 2")
# 이것을 100번까지 쓰기는 힘듬
# in [0, 1, 2, 3, 4]는 특정 번호로
# 순차적으로 커지는 숫자를 쓸 땐 range 함수
# range(1, 6) -> 1, 2, 3, 4, 5

for waiting_number in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_number))

for waiting_number1 in range(20) :
    print("대기번호 : {0}".format(waiting_number1))

for waiting_number2 in range(1, 5) :
    print("대기번호 : {0}".format(waiting_number2))

starbucks = ["ironman", "thor", "roki"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))

# <6-3> while
customer = "thor"
index = 5
while index >= 1:
    print("{0}, 커피가 준비되었습니다. {1} 번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다")

# 위의 커피숍과 달리 손님이 나올 때까지 계속 부른다면?
# customer = "ironman"
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출 {1}회".format(customer, index))
#     index += 1

# -> 무한루프에 걸림 이 문장을 끝내기 위해선 ctrl +c를 누르면 강제 종료
# 이름을 물어본 후 커피가 준비되면 주는 식으로 바꿔보기

customer = "thor"
person = "Unknown"

while person != customer :
    print("{0}, 커피가 준비되었습니다".format(customer))
    person = input("이름이 어떻게 되세요? ")

# -> thor가 아니면 계속 thor, 커피가 준비되었습니다. "이름이 어떻게 되세요? " 가 반복되고
# -> thor가 맞으면 끝맺음 즉 조건에 맞을 때 까지 계속 반복문을 실행

# <6-4> continue & break
# : 반복문 내에서 쓸 수 있음.
absent = [2, 5] #결석 학생
no_book = [7] #책을 안가져옴
# 결석한 학생인 경우 넘어가고 다른 학생들을 책 읽게 하는 경우
for student in range (1, 11) : #1,2,3,~,10
    if student in absent : 
        continue
    elif student in no_book :
        print("오늘 수업 여기까지. {0}는 교무실로 따라와.".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))

# continue는 조건값이 없으면 skip하고 바로 다음으로 넘어가는데, break는 문장을 끝냄

# <6-5> 한줄 for
# 0출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104.
students = [1, 2, 3, 4, 5]
print(students)
# i에다가 100을 더한 값을 넣을텐데 i는 students 리스트를 불러오면서 100을 더한값을 list에 집어 넣어라.
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["ironman", "thor", "spiderman"]
students = [len(i) for i in students]
print(students)

# lenth는 문자열이나 값의 길이를 의미하는데, 그 길이ㅣ에 사용된 변수는 students라는 list를 하나씩 반복하면서 추출한 길이ㅡ의 값을 집어넣겠다. 

# 학생이름을 대문자로 변환
students = ["ironman", "thor", "i am groot"]
students = [i.upper() for i in students]
print(students)

# 7-1 함수
# 함수란 어떤 역할을 하는 박스

# 모바일 뱅킹에서 새로운 계좌를 만들려고 함
# open account란 함수를 정의하려고 함.
def open_account():
    print("새로운 계좌가 생성되었습니다.")
# ->이렇게 하면 아무결과 x, 함수는 정의만 할 뿐 실제로 호출하기 전까진 실행x
open_account()

# 7-2 전달값과 반환값
def deposit(balance, money): #입금함수 만들기
    print("입금이 완료되었습니다. 잔액은 {} 원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money) : 
    if balance >= money : # 잔액이 출금보다 많으면
         print("출금이 완료되었습니다. 잔액은 {} 원입니다.".format(balance - money))
         return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance)) #money를 빼지 않기 떄문에 format 안에 only balance
        return balance

def withdraw_night(balance, money): #저녁에 출금해서 수수료 ㅇ
    commission = 100 #수수료 100원
    return commission, balance - money - commission
#commission에다가 수수료까지 합산한 출금결과를 tuple형식으로 보여줌 2개의 값을 컴마로 구분해서 반환


balance = 0 # 잔액 변수 만들기
balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 500)
# balance = withdraw(balance, 2000)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))

# 7-3 기본값 방법
def profile(name, age, main_lang):
    print("name : {0}\tage : {1}\tmain language : {2}" \
        .format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 같은 학교, 같은 학년, 같은 반, 같은 수업. 매번 프로필을 만들 때마다 age, main lang 안써도 될 떄 기본값 ㅏㅅ용
def profile(name, age = 17, main_lang = "파이썬"):
    print("name : {0}\tage : {1}\tmain language : {2}" \
        .format(name, age, main_lang))

profile("유재석")
profile("김태호")

#7-4 키워드 값
def profile(name, age, main_lang) :
    print(name, age, main_lang)

profile(name = "유재석", main_lang = "파이썬", age = 20)
profile(main_lang="자바", age=25, name="김태호")

#가변인자
#할 수 있는 언어가 많을 때?
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("name : {0}\tage : {1}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)

#end = " "는 이 프린트 문이 끝날 때 줄바꿈을 하지 않고 끝낸다.

profile("유재석", 20, "python", "java", "C", "C++", "C#")
profile("김태호", 25, "kotlin", "swift", "", "", "")

#만약 유재석이 할 수 있는 함수가 하나가 더 늘었다면 lang6를 만들고 그 외 사람들도 ""를 늘리기 힘듬
# 또 여러 사람들이 할 수 없는 함수가 여러개라 계속 ""쓰기가 힘듬 이때 가변인자 사용

def profile(name, age, *language):
    print("name : {0}\tage : {1}\t".format(name, age), end=" ")
    for lang in language :
        print(lang, end=" ")
    print()

profile("유재석", 20, "python", "java", "C", "C++", "C#")
profile("김태호", 25, "kotlin", "swift")

#서로 다른 갯수의 값을 넣어줄 땐 가변인자 즉 *로 시작하는 매개변수로 활용!

#<7-6> 지역변수와 전역변수
# 지역변수는 함수 내에서만 쓸 수 있음. 호출될 때 사용됬다가 함 함수 호출이 끝나면 사라짐
# 전역변수는 모든 공간에서 프로그램 내에서 어디서든 부를 수 있음
# 총이 10자루 있음. 경계근무 나가는 군인들
gun = 10

def checkpoint(soldiers): #경계근무
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun)) # 2명이 경계근무 나가면 총이 총 몇자루를 남았는지

#이렇게 하면 오류남 왜냐면 gun이라는 함수는 할당도 안됬기 때문
# 667의 gun은 다른 gun 초기화가 안됬기 때문에 쓸 수 없음 checkpoint 안에서!
# 밖에 있는 gun의 변수가 변하지 않았기 때문에 checkpoint안에서 사용 (할당안됨) = 지역변수!!!!!

gun = 10

def checkpoint(soldiers): 
    gun = 20
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) 
print("남은 총 : {0}".format(gun)) #이렇게 하면 밖에 있는 gun 값이 18 될 줄 알았는데 여전히 10자루로 나와.!!!!!

# 전역변수는?

gun = 10

def checkpoint(soldiers): 
    global gun #전역 공간에 있는 gun이란 변수를 checkpoint 안에서 쓰겠다! 란 의미 -> 밖에 있는 gun의 변수 내용도 바뀜
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) 
print("남은 총 : {0}".format(gun))

# 일반적으로 전역변수 쓰면 어려워짐 권장하진 않음 (내 생각엔 모든 밖에 있는 gun이란 변수가 다 값이 변경되서 그런듯)
# 함수의 전달값(특정 값)으로 던져서 계산하고 반환값을 받아서 사용하는 방법

gun = 10

def checkpoint(soldiers): 
    global gun #전역 공간에 있는 gun이란 변수를 checkpoint 안에서 쓰겠다! 란 의미 -> 밖에 있는 gun의 변수 내용도 바뀜
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers #gun자체도 지역변수로 됨 따라서 밖에 있는 gun의 값이 바뀌진 않음
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun #return을 사용해서 바껴진 gun의 값을 밖에 있는 gun에 넣을 수 이씅ㅁ


print("전체 총 : {0}".format(gun))
# checkpoint(2) 
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))

# <8-1> 표준입출력
print("python", "Java") # -> python Java
print("python" + "java") #-> pythonjava
print("python", "java", sep = ",") #sep를 통해서 띄어쓰기를 할지, 붙여쓰기를 할지 지정 ㅇ
#, 사이 사이에 들어감
print("python", "java", "javascript", sep = "vs")
print("python", "java", sep = ",", end = "?")
print("무엇이 더 재밌을까요?)") # -> 위의 문장과 뒤의 문장이 한 줄에 출력됨
#end : 문장의 끝부분을 ?표로 끝내달라. ?????

import sys
print("python", "java", file=sys.stdout)
print("python", "java", file=sys.stderr)
# 출력하면 똑같은 결과처럼 보이지만 stdout는 표준 출력으로
# stderr은 표준 에러로 처리됨
# 즉 에러는 확인을 해서 프로그램 코드를 수정해야 하니 stderr을 따로 에러처리를 함

scores = {"math" :0, "english": 50, "coding":100}
for subject, score in scores.items(): #items로 하면 subject라는 키와 score이라는 밸류로 튜플로 나옴
    # print(subject, score) # -> 이 출력문장의 점수부분을 오른쪽으로 정렬하고 싶어!
    print(subject.ljust(8), str(score).rjust(4), sep=":") #l은 left. 왼쪽으로 정렬하는데, 8개의 공간을 확보하고 정렬!
#즉 한 문장을 만들 때 8칸의 공간을 확보하고(만들고) 왼쪽정렬을 하고 수학글자를 표시해라.
#score 점수는 오른쪽 정렬을 하고 총 4칸의 공간을 확보함. 

# 은행 대기순번표
# 001, 002, 003,... 으로 보통 만들어짐
for num in range(1, 21): #1부터 20까지의 숫자를 출력하려 함)
    print("대기번호 : " +str(num).zfill(3)) 
#3개만큼의 공간을 확보하고 값을 만드는데, 값이 없는 공간엔 0을 채워달라 라는 의미의 .zfill(3)

#표준 입력에 대해
answer = input("아무 값이나 입력하세요: ")
#위의 문장은 사용자가 아무 값이나 입력하면 (input)이기 때문에. answer이란 변수에 들어가게 됨.
print("입력하신 값은 " + answer + "입니다.")
#주의할 점 : 문자와 숫자는 잘 되는데, 보통 숫자일 경우엔print("입력하신 값은 " + str(answer)...로 해야됨
#근데 위의 문장이 오류가 안난 이유는? str과 int의 차이를 찾아보자
#사용자 입력의 값을 받게 되면 항상 문자열로 받게 됨.

#<8-2> 다양한 출력포맷
# 빈자리는 빈공간으로 두고, 오른쪽으로 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500)) #앞쪽의 있는 0이 빈공간으로 넣고 오른쪽 정렬을 하되 > 
#  양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<+10}".format(500))
# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(100000000000))
# 3자리마다 콤마찍어주기, +-부호도 붙이기
print("{0:+,}".format(1000000000))
print("{0:+,}".format(-1000000000))
# 3자리 마다 콤마찍어주고 부호도 붙이고 자릿수 확보하기
# 빈자리는 ^로 채워주기
print("{0:^<+30,}".format(100000000))
# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자리수까지만 표시
print("{0:.2f}".format(5/3))

# <8-3> 파일 입출력
score_file = open("score.txt", "w", encoding="utf8")
# open이란 함수로 파일을 열 수 ㅇ. utf8을 정의하지 않으면 한글썼을 때 이상한 문자로 나올 수 있음
print("수학 : 0", file = score_file)
print("영어 : 50", file=score_file)
score_file.close()
# 파일을 열었을 땐 항상 닫아주는 것까지 해야함.
# 이렇게 하면 file이 생기고, 썻떤 내용도 들어감.

score_file = open("score.txt.", "a", encoding="utf8")
# "a"로 열어봄. w로 쓰면 쓰기용도. 덮어쓰기. a는 뒤에서 이어서 쓰고 싶을 때
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()
# print는 자동으로 줄바꿈이 됨. write는 줄바꿈이 안되기 때문에 \n으로 줄바꿈을 함.

# 파일을 가지고 읽어 올 때 (한번에 다 읽어올 때)
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

# 한줄 한줄 읽어올 때
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.reading()) #줄별로 읽음.  한줄 읽고 커서는 다음ㅈ물로 이동
print(score_file.reading())
print(score_file.reading())
print(score_file.reading())
score_file.close()
# 만약 줄바꿈 안하고 싶으면 print(score_file.reading(), end="")로 하기

# 몇줄인지 모를 때 가져와야 할 때
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() #list형태로 저장
for line in lines:
    print(line, end="")

score_file.close()

# <8-4> pickle
# 프로그램 상에서 사용하는 데이터를 파일 형태로 저장하는 방법
import pickle
profile_file = open("profile.pickle", "wb")
# 쓰기 목적으로 w, pickle을 쓰기 위해 b를 써야함
profile = {"이름" : "박명수", "나이" : 30, "취미" : ["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) #profile 에 있는 정보를 file에 저장.
profile_file.close()

# 저 파일에서 데이터를 가지고 오는 방법
import pickle
profile_fiole = opne("profile.pickle", "rb")
profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

# 가ㅣㅈ고 있는 데이터를 pickle을 이용해서 어떤 ㄹ파일에 저장하고 그 파일에 이는 데이터를 road를 통해 불러와서 변수에 저장해 계속 쓸수있게 함

# <8-5> with
# 지금까지 파일을 열고, 처리하고 닫는것까지 하는데 with는 조금 더 편리
import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

#  지금까지 만든 데이터를 불러옴. profile.pickle, rb를 profile_file이란 변수에 저장하고
# 이 파일 내용을 pickle.road를 통해 불러아ㅗ서 출력함.
# -> 따로 open 하지 않아도 됨

# pickle을 쓰지 않고 with를 ㅏㅅ용하는 방법
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

#이렇게 하면 매번 간단히 할 수 ㅣㅆ고 매번 close를 안해도 됨.

# <9-1> class
# 스타크래프트 3개의 종족 게임 테란종족!
# 마린 : 공격 유닛, 군인. 총을쏠 수 ㅇ
name = "마린"
hp = 40 # 유닛의 체력
damage = 5 # 유닛의 공격력

print("{} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\ㅜ". format(hp, damage))

#탱크 : 공격유닛, 탱크, 포를쏠 수 ㅇ 일반모드 / 시즈 모드.
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\ㅜ".format(tank_hp, tank_damage))

# 만약 공격한다면?
def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format( \
        name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)

# 만약 탱크가 더 추가된다면?
name = "마린"
hp = 40 # 유닛의 체력
damage = 5 # 유닛의 공격력

print("{} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\ㅜ". format(hp, damage))

#탱크 : 공격유닛, 탱크, 포를쏠 수 ㅇ 일반모드 / 시즈 모드.
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\ㅜ".format(tank_hp, tank_damage))

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\ㅜ".format(tank_hp, tank_damage))

# 만약 공격한다면?
def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format( \
        name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank_name, "1시", tank2_damage)

# 매번 유닛을 생성하기엔 너무 힘드니 class 를 이용함
# class는 붕어빵 틀과 같음. 틀에 재료를 넣으면 틀에 맞춰서 붕어빵을 무한장만듬. 틀은 하나 붕어빵은 여러개 만드는
# CLASS는 서로 연관있는 변수와 집합정도로 이해하기.

class Unit:
    def __init__(self, name, hp, damage): 
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
# 유닛이란 클래스르 만들었고, def __itit__...을 통해서 필요한 값을 정의함.

marine1 = Unit("마린", 40, 50)
marine2 = Unit("마린", 40, 50)
tank = Unit("탱크", 150, 35)

# <9-2> __init__
# 생성자. 객체가 만들어질 때 자동으로 호출되는 부분.
# 클래스로부터 만들어지는 녀석들을 객체로 표현. 마린과 탱크는 유닛 클래스의 인스턴스라고 함.
# 객체가 생성될 땐 함수에 정의된 개수와 동일하게 해야함. name, hp, damage를. 생략하면 오류남.

# <9-3> 멤버변수
# self.name, self.hp, selp.damage가 멤버변수
# 클래스 내에 정의된 변수고 그 변수를 가지고 우리가 쓸 수 있고 실현할 수 있음

# 레이스 : 공중유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))
# .으로 멤버변수에 접근할 수 있음
# 즉 멤버변수를 외부에서 쓸 수 있음

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True #clocking : 이라는 기능이 업그레이드 됬다고 하자

if wraith2.cloking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# clokingㅇ이란 변수는 원래 unit 만들 때 없었음. 이름, 체력, 공격력만 넣었는데 외부에서 변수 clocking를 추가로 할당함
# 어떤 객체에 추가로 변수를 외부에서 만들어서 쓸 수 있음 차이는
# wraith1에는 clocking은 없음.

# <9-4> 메소드
class Unit:
    def __init__(self, name, hp, damage): 
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# 공격 유닛을 만드는 클래스를 만들어보자.
class AttackUnit:
    def __init__(self, name, hp, damage): 
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0 :
            print("{0} : 파괴되었습니다.".format(self.name))
# self는 자기 자신을 말하는 것이고, class 내에서 메소드 앞에 항상 self를 적어준다.
# init 괄호 안에 있는 것을 입력받아 self에 넣어서 쓴다. print(안에 있는 location까지도)

# 파이어뱃 : 공격 유닛, 화염방사기 사용
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)

