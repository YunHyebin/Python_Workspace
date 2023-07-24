# # # list 의 성질

# # a = [10, 20, 30]
# # a.append(500)
# # #  a = [10, 20, 30, 500]

# # # append(리스트)
# # a.append([1, 2, 3])
# # # [1, 20, 30, 500, (1, 2, 3)]

# # a.extend([4,5,6])
# # # [10, 20, 30, 500, [1, 2, 3], 4, 5, 6]

# # print(a[1])

# # # a = (1, 2, 3, 4, 5)
# # # print(a.index(21))

# # class BusinessCard:
# #     def __init__(self, name, email, addr):
# #         self.name = name
# #         self.email = email
# #         self.addr = addr
# #     def print_info(self):
# #         print("------------------")
# #         print("Name: ", self.name)
# #         print("E-mail: ", self.email)
# #         print("Address: ", self.addr)
# #         print("------------------")

# # # gangcheol = BusinessCard()
# # # gangcheol.print_info()
# # hyebin = BusinessCard("윤혜빈", "123@gmail.com", "USA")
# # hyebin.__init__("윤강철", "345@gmail.com", "korea")
# # hyebin.print_info()

# # hyebin.addr = "japan" #.addr 하니까 hyebin객체의 addr 속성에 접근함
# # hyebin.print_info()


# # phone_book = [('A', '010-9656-2122', '123@gmail.com'), ('B', '010-1111-2222', '456@gmail.com'), ('C', '010-9656-2122', '123@gmail.com')]

# # search_name= input("이름으로 검색: ")
# # result = ""
# # for x in phone_book:
# #     # print(x[0] == search_name)
# #     if x[0] == search_name:
# #         result = x
# #         break

# # if result == x:
# #     print(x)
# # else:
# #     print("없는 정보")


# # 연락처 종합 검색 하기
# from distutils.log import info


# phone_book = [{"A": ("010", "A의 메일")}, {"B" : ("011", "B의 메일")}]
# phonebook_data = []

# for x in phone_book:
#     phonebook_data.append(list(x) + list(x.values()))
# # [['A', ('010', 'A의 메일')], ['B', ('011', 'B의 메일')]]

# for y in phonebook_data:
#     print(f"이름: {y[0]} / 번호 : {y[1][0]} / 메일 : {y[1][1]}")
    



# # for y in phonebook_data:
# #     # ['A', ('010', 'A의 메일')]
# #     # ['B', ('011', 'B의 메일')]
# #     for z in y: #이름 출력    
# #         print(z[0][0])

# #         pass
# #         # A #str
# #         # ('010', 'A의 메일') #tuple
# #         # B #str
# #         # ('011', 'B의 메일') #tuple
# #         # if type(z) == str :   
# #         #     name.append(z)
# #         # else:
# #         #     information.append(z)


# # name = ['A', 'B']
# # information = [('010', 'A의 메일'), ('011', 'B의 메일')]

# # 출력하는 방법 못해결
# # for N in name:
# #     print(N)
# #     for I in information:
# #         print(I)

# # print(name, information)

# # dictionary a.get(key)
# # a = {"A": 1, "B": 2, "C": 3}
# # key = input("찾을 키: ")
# # print(f"값: {a.get(key)}")

# # ex_list = []
# # example = [{"subject1" : ("G1", "avg1", "cre1")}, {"subject2" : ("G2", "avg2", "cre2")}]
# # for x in example:
# #     ex_list.append(list(x) + list(x.values()))

# # for x in ex_list:
# #     print(f"{x[0]}\t\t\t{x[1][0]}\t{x[1][1]}")

# my_list = [10, 20, 30, 40, 50, 60]
# mean = sum(my_list) / len(my_list)
# print(mean)

# while True:
#     x = input("제목: ")
#     y = input("분야: ")
#     print("%-15s" % x +"%-10s" % y)

# list = [x for x in range(0, 10)]
# # print(sum(list))
# zeroTonine = set([x for x in range(0, 10)])
# # print(zeroTonine) #집합 컬렉션자료도 sum 가능

# N = {1,2,3,4,6,7,8,0}
# result = 0
# for i in zeroTonine:
#     if i not in N:
#         print(i)
#         result += i
# print(result)

# numbers = set([])

# while True:
#   cnt = int(input("원소 갯수 입력 (1~9개 입력 가능. 종료 0): "))
#   if cnt == 0:
#     print("종료")
#     break
# #   elif cnt < 1 or cnt > 9:
# #     print("갯수를 다시 입력해주세요")
# #     continue
#   for i in range(0, cnt): 
#     number = int(input("0부터 9사이의 숫자(원소) 입력: "))
#     print(number)
#     numbers.add(number)

# arr= [1,2,3,4]
# arr2 = [1]
# arr3 = arr - arr2[0]
# print(arr3)

def bubble_sort(arr):
    for i in range(len(arr) -1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(nums)
    return nums

nums = [90, 10, 23, 17, 56, 39]
print(f"수정전: {nums}")
print(f"최종: {bubble_sort(nums)}")