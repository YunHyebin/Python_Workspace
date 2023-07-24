try_number = 0
answer_number = 0

def fail():
    return "3번의 기회가 끝났습니다. 다시 도전해보세요!"
def win():
    answer_number += 1
    print("축하축하 정답")
    print(f"총 틀린 횟수: {try_number}")
    print("총 정답 횟수 {0}".format(answer_number))

def num_game():
    import random
    com = random.randint(1, 30)
    print('숫자맞히기 게임 시작')
    print("기회는 3번입니다")
    print(com) #실행 잘되는지 테스트 용
    for a in range(3):
        player = int(input("1에서 30까지의 숫자 입력(종료:0)"))
        if player == 0:
            break
        elif player == com:
            win()
        elif player > com:
            if try_number < 2:
                hint1 = com - player
                print(f"{hint1}만큼 빼보세요.")
                try_number += 1
            elif try_number == 2:
                pass
        elif player < com:
            try_number += 1
            hint2 = com - player
            print(f"{hint2}만큼 더해보세요")
        

def gugudan_game():
    import random
    try_number = 0
    answer_number = 0
    print('구구단 게임 시작')
    print("기회는 3번입니다")
    for x in range(3):
        com_num1 = random.randint(2, 9)
        com_num2 = random.randint(2, 9)
        answer = com_num1 * com_num2
        print(answer) #실행 잘되는지 테스트 용
        player = int(input("숫자 입력(종료:0)"))
        if player == 0:
            print("종료합니다.")
            break
        elif player == answer:
            answer_number += 1
            print("축하축하 정답")
            print(f"총 틀린 횟수: {try_number}")
            print("총 정답 횟수 {0}".format(answer_number))
        else:
            print("틀렸습니다. 재도전하세요!")
            try_number += 1

def game_369():
    print("369 게임 시작")
    while True:
        num = int(input('1~100사이 정수 입력(0 입력 시 종료): '))
        a = num // 10 
        b = num % 10 
        if num == 0:
            print("게임을 종료합니다")
            break
        elif a == 3 or a == 6 or a ==9:
            if b == 3 or b == 6 or b == 9:
                print('짝짝')
            else:
                print('짝')
        elif b == 3 or b == 6 or b == 9:
            print('짝')
        else:
            print('다음 수')


while True:
    which_game = int(input("1. 숫자맞추기 2. 구구단 맞추기 3. 369 게임 0. 종료: "))
    if which_game == 1:
        num_game()
    elif which_game == 2:
        gugudan_game()
    elif which_game == 3: 
        game_369()
    elif which_game == 0:
        print("게임을 종료합니다")
        break 
    else:
        print("값을 잘못 입력하셨습니다")

# 정규표현식 과제1
pattern = '[0-9]{3}-[0-9]{4}-[0-9]{4}'
import re
# print(re.match(pattern, phone)) # <re.Match object; span=(0, 13), match='010-2222-3333'>

while True:
    phone = input("폰번호 입력: ")
    if phone == '0': 
        break
    elif re.match(pattern, phone) != None: #왜 elif가 아니라 if지?
        print("폰번호 맞음")
    else:
        print("폰번호 틀림")



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
    
# player = input("가위바위보!: ")
#     if computer == '가위':
#         if player == '가위':
#             print('다시!')
#             continue
#         elif player =='바위':
#             print('사용자 승리!')
#         elif player == '보':
#             print('컴퓨터 승리!')
#     elif computer == '바위':
#         if player == '바위':
#             print('다시!')
#             continue
#         elif player =='보':
#             print('사용자 승리!')
#         elif player == '가위':
#             print('컴퓨터 승리!')
#     elif computer == '보':
#         if player == '보':
#             print('다시!')
#             continue
#         elif player =='가위':
#             print('사용자 승리!')
#         elif player == '바위':
#             print('컴퓨터 승리!')
#     elif player == 0:
#         break


x = 5
print('hello')

def print_lyrics():
    print("i'm a lumberjack, and i'm okay.")
    print('I sleep all night and I work all day.')

print('Yo')
print_lyrics()
x = x + 2
print(x)

# hello
# Yo
# "i'm a lumberjack, and i'm okay."
# 'I sleep all night and I work all day.'
# 7
