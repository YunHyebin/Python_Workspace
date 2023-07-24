def min_coin(money, coin_arr):
    count = 0
    for x in coin_arr:
        count += money//x
        print(f'{x}원: {money//x}')
        money -= (money//x)*x
    return count

coin_arr = [500, 100, 70, 10]
# print(f"\n총 동전수: {min_coin(140, coin_arr)}")

## [실습문제2] ######################
def min_coin(money):
    count = 0 # 동전 갯수
    coins = [500, 100, 50, 10, 5, 1]
    for coin in coins:
        count += money // coin
        money %= coin
    return count
try:
    money = int(input("금액 입력: "))
    print(f"필요한 총 동전 갯수: {min_coin(money)}")
except:
    print("다시 시도")

## [도전문제1] ######################
# <매개변수>
# 전체 학생수 n ( 2 <= n <= 30)
# 도난당한 학생들의 번호 배열 lost (1 <= n, 중복x)
# 여벌 체육복 가져온 학생들 번호 배열 reserve
# return 체육수업 들을 수 있는 학생 최대수

# n = int(input("전체 학생 수 : "))

## [도전문제1] ######################