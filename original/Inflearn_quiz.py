# 자료형 quiz
''' 변수를 이용하여 다음 문장을 출력하시오
변수명: station
변수값: "사당", "신도림", "인천공항" 순서대로 작성
출력문항: xx 행 열차가 들어오고 있습니다.'''

# 자료형 answer
'''
station = "사당"
print(station + "행 열차가 들어오고 있습니다.")

station = input("열차이름 입력: ")
print(station + "행 열차가 들어오고 있습니다.")
'''

# 연산자 quiz
'''당신은 최근 코딩 스터디 모임을 새로 만들었습니다.
월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 합니다.
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.'''

''' 
조건1 : 랜덤으로 날짜를 뽑기 
조건2: 28일 이내
조건3: 1~3일은 스터디 준비해야 하므로 제외
출력문: 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.
'''

from random import *
date1 = int(random() * 28) + 4
date2 = randint(4, 28)
date3 = randrange(4, 29)
print("오프라인 스터디 모임 날짜는 매월 " + str(date1) + "일, " + str(date2) + "일, " + str(date3) + "일로 선정되었습니다.")