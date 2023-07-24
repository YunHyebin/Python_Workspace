# # 1
# students = [
#     {"name":"이정재", "korean":87, "math":98, "english":88, "science":95},
#     {"name":"정우성", "korean":92, "math":98, "english":96, "science":98},
#     {"name":"박보영", "korean":76, "math":96, "english":94, "science":90},
#     {"name":"나석주", "korean":98, "math":92, "english":96, "science":92},
#     {"name":"김태희", "korean":95, "math":98, "english":98, "science":98},
#     {"name":"송강", "korean":64, "math":88, "english":92, "science":92}
# ]
# # name, 국어, 수학, 영어, 과학 키/ 점수들이 값

# print("이름", "총점", "평균", sep ="\t")

# 결과
# for student in students:
# #   {'name': '이정재', 'korean': 87, 'math': 98, 'english': 88, 'science': 95}
# # {'name': '정우성', 'korean': 92, 'math': 98, 'english': 96, 'science': 98}
# # {'name': '박보영', 'korean': 76, 'math': 96, 'english': 94, 'science': 90}
# # {'name': '나석주', 'korean': 98, 'math': 92, 'english': 96, 'science': 92}
# # {'name': '김태희', 'korean': 95, 'math': 98, 'english': 98, 'science': 98}
# # {'name': '송강', 'korean': 64, 'math': 88, 'english': 92, 'science': 92}
#     score_sum = student["korean"] + student["math"] + student["english"] +student["science"]
#     # 학생들 점수 합계
#     score_average = score_sum / 4
#     print(student["name"], score_sum, score_average, sep = '\t')

# # 딕셔너리로 학생을 표현함. 딕셔너리로 구성된 학생을 묶어 리스트로 만들어 학생들을 만듬. 
# # 객체: 여러가지 속성을 가질 수 있는 대상. 학생과 여러 학생이란 속성을 가진 객체 모두 객체임

# # 2 학생(딕셔너리)를 리턴하는 함수 선언.
# def create_student(name, korean, math, english, science):
#     #이름, 점수들을 입력받으면 키 안에 밸류들을 각각 넣음.
#     return {
#         "name" : name,
#         "korean": korean,
#         "math": math,
#         "english" : english,
#         "science" : science
#     }

# students= [
#     create_student("정우성", 100, 99, 88, 77),
#     create_student("이정재", 98, 20, 85, 60),
#     create_student("박보영", 98, 98, 84, 30)
# ]

# 결과
# print("이름", "총점", "평균", sep ="\t")
# for student in students:
#     score_sum = student["korean"] + student["math"] + student["english"] +student["science"]
# #     # 학생들 점수 합계
#     score_average = score_sum / 4
#     print(student["name"], score_sum, score_average, sep = '\t')

# # 3. 학생(딕셔너리) 리턴 함수 + 학생 처리 함수
# def create_student(name, korean, math, english, science):
#     #이름, 점수들을 입력받으면 키 안에 밸류들을 각각 넣음.
#     return {
#         "name" : name,
#         "korean": korean,
#         "math": math,
#         "english" : english,
#         "science" : science
#     }

# def student_get_sum(studennt):
#     pass

# 잔액 동전환산 & 잔액계산 함수
def get_coin(Money):
  global NumberOf500
  global NumberOf100
  global ect
  global total
  total = Money
  NumberOf500 = Money // 500 #500원 갯수
  Money = Money % 500
  NumberOf100 = Money // 100 #100원 갯수
  ect = Money % 100
  current_money = total
  return NumberOf500, NumberOf100, ect, total

# # 잔액계산 함수
# def total_check(Money):
#   get_coin(Money)
#   return NumberOf500 + NumberOf100 + ect

menu = {"콜라" : 1000, "사이다" : 1000, "환타":1200, "커피":1000, "생수":800}

print("**자판기 판매 메뉴**")
for drink, cost in menu.items():
  print(f"{drink} : {cost} /", end =" ")
print(" ")

while True:
  try: 
    print("")
    money = int(input("돈을 투입하세요: ")) 
    current_money = money
    if money == 0:
      print("자판기 종료")
      break

  except:
    continue
  
  while True:
    print("")
  
    choice = input("메뉴 선택 (종료0): ")
    if choice in menu:
        # 메뉴 중 최저 가격보다 적은 것으로 했을 때 문제는
        # 잔액이 최저 가격음료보다 돈이 적은데 구매가 성공되는 것임 따라서 내가 고른 메뉴보다 돈이 적을 떄로 바꿈.
        
        # 구매하기
        if current_money >= (menu[choice]): 
            print(f"{choice}구매 완료")
            current_money -= menu.get(choice)
            get_coin(current_money)
            print(f"총 잔액: {total}원")
  
        # 잔돈 반환하기
        else: #최저 가격 음료보다 돈 없을 때 잔돈 반환
            get_coin(current_money)
            print(f"500원 동전 : {NumberOf500}개 반환")
            print(f"100원 동전 : {NumberOf100}개 반환")
            print(f"그 외 동전 {ect}원 반환")
            print(f"총 잔액: {total}원")
            print('자판기 종료')
            break
  
    elif choice == "0":
        get_coin(current_money)
        print(f"500원 동전 : {NumberOf500}개 반환")
        print(f"100원 동전 : {NumberOf100}개 반환")
        print(f"그 외 동전 {ect}원 반환")
        print(f"총 잔액: {total}원")
        print('자판기 종료')
        break
    
    else:
        print('메뉴에 없는 음료\n다시 선택')
