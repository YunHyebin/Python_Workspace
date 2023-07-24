def add_some3(a, b):
    return a+b, a*b

result3 = add_some3(2,3)
print(result3)
# (5, 6) 두 return값 모두 반환됨. 튜플(컬렉션)로 구성됨.

sum, mul = add_some3(3,5)
print(sum)
print(mul)

def add_some4(a, b):
    return a+b # 이것만 수행됨 즉 return문은 하나만!
    return a*b

result = add_some4(3, 5)

print(result)

def introduce(name, adult = True):
    print("이름: %s" %name)
    if adult: #adult == True, True 이면
        print('성인입니다')
    else: # false이면
        print('성인이 아닙니다.')

# introduce("박보검") #생략가능 
# introduce("사무엘", False)
# # 이름: 박보검
# # 성인입니다
# # 이름: 사무엘
# # 성인이 아닙니다.

# # def introduce2(adult = True, name):#첫번째는 무조건 기본값으로 해야 함. 가변 매개변수.

# # 지역변수와 전역변수
# def func1():
#     a = 10 #지역변수
#     print(a)

# a = 20
# func1() #10 정의함수에선 지역변수가 우선
# print(a) #변수 a인 20을

# def func2():
#     global a
#     a = 10
#     print(a)

# a = 20
# func2() #10
# print(a) #10 전역변수 a를 찾아 변수 a에 덮어씌움
## [야구] ###############################################################################################
from logging import makeLogRecord
from random import *
from re import M

# 게임 함수
# for 함수로 하나씩 가져와
# computer의 첫번째 요소 == player 첫번쨰 요소 매치되는지 확인하여 strike를 카운트
# 매칭x -> in 을 써서 컴퓨터의 숫자가 player에 포함되는지 확인함
# 포함되면 ball 카운트, 포함안되면 넘어감

# 3개를 넣지 않은 경우, 중복 숫자를 넣은 경우, 범위 안의 숫자가 아닌 경우를 체크하는 함수
# set는 중복된 값을 필터링한 성질을 사용 & 길이가 3개가 되는지! 하지만 순서형으로 for문 돌릴거라 여기서만 사용!
# 함수로 만든 이유는 컴퓨터와 사용자 두 군데서 사용할 거라 함수로 만듬.
# def same_check(x_list):
#   x_set = set(filter(lambda x : 0 < x < 10, x_list))
#   if len(x_set) != 3 or len(x_list) != 3:
#     return False
#   else:
#     return True
  
# # 야구 결과 계산
# def baseball(com, user):
#     global strike
#     global ball
#     strike = 0
#     ball = 0
#     i = 0 #배열 요소 접근하기 위해
#     for current in user:
#         if current == com[i] :
#             strike += 1
#         elif current in com:
#             ball += 1
#         i += 1
    
# # 게임실행 함수
# # 멀티플레이게임 (도전문제4)를 위해 게임실행도 함수로 만듬
# def rungame():

#     while True:
#         #컴퓨터 숫자 리스트 형성
#         computer = [randint(1,9) , randint(1,9) ,randint(1,9) ]
#         while True:
#             if same_check(computer) == True:
#                 break
#             else: #실행이 안되면 컴퓨터 숫자를 다시 생성해서 검사.
#                 computer = [randint(1,9) , randint(1,9) ,randint(1,9) ]
        
#         # print(computer) #-> 스트라이크 3번을 확인하기 위해 테스트로
#         try:
#             player = input("1~9사이의 숫자 3개를 띄어 입력하세요 (종료0): ")
#             player_list = list(map(lambda x: int(x), player.split(" ")))
#         except: # 숫자가 아닌 문자를 넣은 경우
#             continue
    
#         # 종료 입력
#         if '0' == player:
#             print("종료합니다")
#             break
#         # 숫자 중복, 갯수 확인
#         if same_check(player_list) == False:
#             continue
        
#         # baseball 게임 실행
#         baseball(computer, player_list)
#         print(f"컴퓨터: {computer} / 플레이어: {player_list} → {strike}스트라이크 {ball}볼")
        
#         if strike >= 3:
#                 print('잘 맞추시네요! 승리하여 게임을 종료합니다~')
#                 break

# rungame()
# class로 만들고나선 객체에서 호출해야 한다.
# ex) week6.rungame()

# ###[369게임]###############################################
def game(num):
  global count
  count = 0
  for i in num:
    if int(i) % 3 == 0:#짝이 아닌 경우
      count += 1
    else: 
      continue
  return "짝" * count

while True:
  try:
    player = input("정수 입력: ")
  except:
    continue
  
  if player == '0':
    print("종료합니다")
    break

  game(player)


###<<단위변환기>>######################################################
def length_convert(num):
  global mm
  global cm
  global m
  global km
  mm = 0
  cm = 0
  m = 0
  km = 0
  print("\t\t\t\t<<변환할 값의 단위 메뉴>>\n1. mm 2. cm 3. m 4. km")
  try:
    convert = int(input("위의 단위 메뉴를 보고 변환할 값 단위의 해당 번호를 입력하세요: "))
    if convert == 1: # mm → mm, cm, m, km 변환
      mm = num
      cm = num*0.1
      m = num*0.001
      km = num*0.000001
    elif convert == 2: # cm → mm, cm, m, km 변환
      mm = num*10
      cm = num
      m = num*0.01
      km = 0.00002
    elif convert== 3: # m → mm, cm, m, km 변환
      mm = num*1000
      cm = num*100
      m = num
      km = num*0.001
    elif convert == 4: # km → mm, cm, m, km 변환
      mm = num*1000000
      cm = num*100000
      m = num*1000
      km = num
    print(f"{mm:.2f}mm // {cm:.2f}cm // {m:.2f}m // {km:.2f}km")
  except:
    print("잘못 입력하셨습니다")

def area_convert(num):
  global cm2
  global m2
  global km2
  global korean_area
  cm2 = 0
  m2 = 0
  km2 = 0
  korean_area = 0
  print("\t\t\t\t<<변환할 값의 단위 메뉴>>\n1. cm²\n2. m²\n3. km²\n4. 평")
  try:
    convert = int(input("위의 단위 메뉴를 보고 변환할 값 단위의 해당 번호를 입력하세요: "))
    # cm² → cm², m², km², 평 변환
    if convert == 1: 
      cm2 = num
      m2 = num*0.0001
      km2 = num*0.0000000001
      korean_area = num*0.0000605
    # m² → cm², m², km², 평 변환
    elif convert == 2: 
      cm2 = num*10000
      m2 = num
      km2 = num*0.000001
      korean_area = num*0.3025
    # km² → cm², m², km², 평 변환
    elif convert == 3: 
      cm2 = num*10000000000
      m2 = num*1000000
      km2 = num
      korean_area = num*302500
    # 평 → cm², m², km², 평 변환
    elif convert == 4: 
      cm2 = num*33057.85124
      m2 = num*3.305785
      km2 = num*0.0000033058
      korean_area = num
    print(f"{cm2:.2f}cm² // {m2:.2f}m² // {km2:.2f}km² // {korean_area:.2f}평")
  except:
    print("잘못 입력하셨습니다")

def weight_convert(num):
  global mg
  global g
  global kg
  global t
  mg = 0
  g = 0
  kg = 0
  t = 0
  print("\t\t\t\t<<변환할 값의 단위 메뉴>>\n1. mg\n2. g\n3. kg\n4. t")
  try:
    convert = int(input("위의 단위 메뉴를 보고 변환할 값 단위의 해당 번호를 입력하세요: "))
    # mg → mg, g, kg, t 변환
    if convert == 1: 
      mg = num
      g = num*0.001
      kg = num*0.000001
      t = num*0.000000001
    # g→ mg, g, kg, t 변환
    elif convert == 2:
      mg = num*1000
      g = num
      kg = num*0.001
      t = num*0.000001
    # kg → mg, g, kg, t 변환
    elif convert == 3:
      mg = num*1000000
      g = num*1000
      kg = num
      t = num*0.001
    # t → mg, g, kg, t 변환
    elif convert == 4:
      mg = num*1000000000
      g = num*1000000
      kg = num*1000
      t = num
    print(f"{mg:.2f}mg // {g:.2f}g // {kg:.2f}kg // {t:.2f}t")
  except:
    print("잘못 입력하셨습니다")

def volume_convert(num):
  global ml
  global l
  print("\t\t\t\t<<변환할 값의 단위 메뉴>>\n1. ml\n2. L ")
  try:
    convert = int(input("위의 단위 메뉴를 보고 변환할 값 단위의 해당 번호를 입력하세요: "))
    # ml → L 변환
    if convert == 1: 
      ml = num
      l = num*0.001
    # L → ml 변환
    elif convert == 2:
      ml = num*1000
      l = num
    print(f"{ml:.2f}ml // {l:.2f}L")
  except:
    print("잘못 입력하셨습니다")

def temperature_convert(num):
  global cel # 섭씨 ℃
  global fah # 화씨 ℉
  cel = 0
  fah = 0
  print("\t\t\t\t<<변환할 값의 단위 메뉴>>\n1. ℃\n2. ℉ ")
  try:
    convert = int(input("위의 단위 메뉴를 보고 변환할 값 단위의 해당 번호를 입력하세요: "))
    # ℃ → ℉ 변환
    if convert == 1: 
      cel = num
      fah = (num * 1.8) +32
    # ℉ → ℃ 변환
    elif convert == 2:
      fah = num
      cel = (num-32) / 1.8
    print(f"{cel:.2f}℃ // {fah:.2f}℉")
  except:
    print('잘못 입력하셨습니다.')

while True:
  print("\t\t\t\t<<변환 메뉴>>\n1. 길이 변환 2. 넓이 변환 3. 무게 변환 4. 부피 변환 5. 온도 변환 6. 종료")
  try:
    menu = int(input('변환 메뉴를 입력하세요: '))
    if menu == 6:
      print('단위 변환 프로그램을 종료합니다')
      break
    num = int(input("변환할 값을 입력해주세요: "))

    if menu == 1:
      length_convert(num)
    elif menu == 2:
      area_convert(num)
    elif menu == 3:
      weight_convert(num)
    elif menu == 4:
      volume_convert(num)
    elif menu == 5:
      temperature_convert(num)

  except:
    print("값을 잘못 입력하셨습니다")
    continue