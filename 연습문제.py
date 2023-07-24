
import re
p = re.compile('[a-z]+')
m = p.search("5 python")
print(m.start() + m.end()) #10 출력. 왜 10이 출력되지?
# "python"이라는 문자열의 시작 인덱스는 2이고 마지막 인덱스는 8이므로 10이 출력된다.

"""
part 010-9999-9999
kim 010-8888-3231
lee 010-2324-4645
"""

import re
data = """
part 010-9999-9999
kim 010-8888-3231
lee 010-2324-4645
"""
pattern = '\d\d\d-\d\d\d\d-\d\d\d\d'
sentence = 'hello, world! my name is Hyebin'
print(re.search('^hello', sentence))
print(re.search('^world', sentence))
print(re.search('Hyebin$', sentence))

import re
pattern = '^010-[0-9]{4}-[0-9]{4}'
while True:
    phone = input("폰 번호 입력: ")
    if phone == '0': break
    if re.search(pattern, phone) != None:
        print("폰번호 맞음")
    else:
        print("폰번호 틀림")
# 주민번호 과제
while True:
    num = input("주민번호 입력(종료 0 입력): ")
    if num == '0':
        break
    elif re.match('[0-9]{6}-[0-9]{7}', num) != None:
        print("주민번호 맞음\n")
    else: 
        print("형식 틀림\n")

# 학번 과제
import re
pat = re.compile('^9[1-9]{2}[0-9]{2}[0-9]{3}')
while True:
    number = input("학번 입력(종료: 0): ")
    if number == '0': break
    elif p.match(number) != None:
        print("학번입력 완료")
    else: print("학번형식 틀림")

# 가위바위보 게임.
import random as rd
while True:
    computer = rd.randint(1, 3)
    if computer == 1: computer = '가위'
    elif computer == 2: computer = '바위'
    else: computer = '보'

    print(computer)

    player = input("가위바위보!: ")
    if computer == '가위':
        if player == '가위':
            print('다시!')
            continue
        elif player =='바위':
            print('사용자 승리!')
        elif player == '보':
            print('컴퓨터 승리!')
    elif computer == '바위':
        if player == '바위':
            print('다시!')
            continue
        elif player =='보':
            print('사용자 승리!')
        elif player == '가위':
            print('컴퓨터 승리!')
    elif computer == '보':
        if player == '보':
            print('다시!')
            continue
        elif player =='가위':
            print('사용자 승리!')
        elif player == '바위':
            print('컴퓨터 승리!')

# type(변수명)
test = '테스트' #str
test2 = 2       #int
test3 = '테스트3'#str
test4 = 23.432   #float

member = input("회원이십니까? (y/n) : ")
if member == 'y':
    print("어서 오십시오.")
elif member == 'n':
    print('회원가입을 해주세요.')
else:
    print("잘못 입력하셨습니다.")

# 놀이동산 입장료
