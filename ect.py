data = """
박00 800905-1049118
김00 700905-1059119
"""
# isdigit 함수
# print(str.isdigit(data[12:]))
# print(data[:].isdigit()) # false
# print(data.isdigit()) #false

# split 함수
people = "윤혜빈,윤강철,김민홍,윤명진,이효숙,보리,강아지,나무"
print("1. ", data.split())
name = people.split(",")
print(name)

# 탈출문자
print('가나다라\n마바사')
print('나는 \'윤혜빈\' 입니다.')
print("나는 \\윤혜빈\\입니다.")
print("C:\\Users")
print("Red Apple\rRine")
print("너는 윤혜빈입니다\r나는")
print("나는\b윤혜빈입니다.")
print("나는\t윤혜빈입니다.")

# find() & index() 함수
# 변수.find("찾을 문자", 시작점, 종료점)
# find() 함수는 찾는 문자가 없는 경우 -1을 출력

# 변수.index("찾을 문자", 시작점, 종료점)
# index() 함수는 찾는 문자가 없는 경우 ValueError 에러 발생
print('oxoxoxoxoxox'.index('x', 2)) # 3 x가 처음 위치한 자리
a = 'hello'
print(a.find('o', 1, 3)) # -1: find는 찾는 값이 없을 때 -1을 출력