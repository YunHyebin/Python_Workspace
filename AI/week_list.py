# A = [1, 2, 1, 3, 2, 4, 4, 5, 1]
# B = []
# for i in A:
#     if i not in B:
#         B.append(i) #중복된 값 뺀 고유값?

# 1. 메뉴판 만들기

class menu:
    def __init__(self, name, price): # 메뉴 클래스(객체)
        self.name= name
        self.price = price

    def get_payment(self, Qty): # 가격 구하는 함수
        return self.price * Qty

menu = [
    menu("아메리카노", 2500),
    menu("카푸치노", 3500),
    menu("핫초코", 4000)
]

for menu in menu:
    pass

list = [1, 3, 5, 6]
print(type(list[1]))


# for drinks,cost in menu:
#   print(f'{drinks}, 가격: {cost}')
# print(' ')

# # 2. 체크카드 잔액 조회하기
# card = 10000
# print(f'체크 카드 잔액: {card}')

# # 3. 메뉴 입력 받기
# while True:
#   order = input('메뉴 입력(종료 0): ')
#   if order == '0':
#     print('안녕히 가십시오')
#     break
#   else:
#     if order in menu:
#       Qty = int(input('수량 입력: '))
#     else:
#       Qty = int(input('수량 입력: '))
#       print('메뉴를 잘못 입력했습니다.\n 다시 입력해주세요.')

# payment = menu[order] * menu[Qty]
# print(payment)
# 4. 결제금액과 체크카드 잔액 비교해 계산하기
# 1) if 결제금액 < 체크카드 잔액:
# 결제금액 : 입력받은 메뉴 * 수량, 체크카드 잔액: 체크카드 잔액 - 결제금액
# if (order * Qty) < card:
#   print('')

# 2) else: 잔액 부족 출력

