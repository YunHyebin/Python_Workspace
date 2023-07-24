## [실습문제1] ##############################################################
# def sequential_search(target, nums):
#     for x in nums:
#         if x == target:
#             print(f"인덱스 {nums.index(x)}에서 32을(를) 찾았어요~")
#             break
#         else :
#             print(f"인덱스 {nums.index(x)}에서 {target}이(가) 없네요!!")
# num = [37, 53,23, 76, 14, 91, 89, 32,42, 10]
# sequential_search(32, num)
## [실습문제2] ##############################################################
def bubble_sort(nums):
  n = len(nums)
  for i in range(1, n):
    for j in range(i):
      
    # print(f"{i}단계: ")

nums = [90, 10, 23, 17, 56, 39]
print(bubble_sort(nums))
# bubble_sort(nums)
# print(f"오름차순 정렬전 : {nums}")
# print(f"오름차순 정렬후 : {bubble_sort(nums)}")
# ## [실습문제3] ##############################################################
# def bubble_sort(nums):
#   for cur in range(0, len(nums)):
#     if cur == len(nums) - 1:
#       break
#     else:
#       if nums[cur] > nums[cur+1]:
#         nums[cur], nums[cur+1] = nums[cur+1], nums[cur]
#         print(f"{cur+1}단계: {nums}")
#   return nums
# nums = [90, 10, 23, 17, 56, 39]
# print(f"오름차순 정렬전 : {nums}")
# print(f"\n정렬완료: {bubble_sort(nums)}")
## [실습문제 1 변형] ##############################################################
# def sequential_search(target, nums):
#     if target not in nums:
#         print("찾을 값이 리스트에 없습니다.")
#     else:
#         for x in nums:
#             if x == target:
#                 print(f"인덱스 {nums.index(x)}에서 {target}을(를) 찾았어요~")
#                 break
#             else :
#                 print(f"인덱스 {nums.index(x)}에서 {target}이(가) 없네요!!")
            
# count = int(input("자료 개수 입력: "))
# nums = []
# for i in range(count):
#     num = int(input("자료 값 입력: "))
#     nums.append(num)
# search = int(input("찾을 값 입력: "))
# sequential_search(search, nums)
# ## [실습문제 3 변형] ##############################################################
# def bubble_sort(nums):
#   for cur in range(0, len(nums)):
#     if cur == len(nums) - 1:
#       break
#     else:
#       if nums[cur] > nums[cur+1]:
#         nums[cur], nums[cur+1] = nums[cur+1], nums[cur]
#         print(f"{cur+1}단계: {nums}")
#   return nums

# numbers = []
# cnt = int(input("자료 갯수 입력: "))
# for x in range(cnt):
#     number = int(input("자료값 입력: "))
#     numbers.append(number)
# print(f"오름차순 정렬전 : {numbers}")
# print(f"\n정렬완료: {bubble_sort(numbers)}")

# ## [도전문제 1] ##############################################################
# def book_sort(books):
#     b_sorted = sorted(books.items(), key = lambda item : (item[1][1]))
#     print("책 제목".center(10), "분야".center(10))
#     print("{:-<30}".format("-"))
#     for x in b_sorted:
#       str = "%-13s%-10s" % (x[0], x[1][0])
#       print(str.replace(" ", "0"))
    
#       # print("%-15s" % x[0], "%-10s" % x[1][0])
#       # print("{0:<10}".format(x[0]), "{0:<10}".format(x[1][0]))
#       # print(x[0].ljust(10), x[1][0].ljust(10))

# fd_dict = {"철학" : 100, "사회과학" :200, "자연과학" : 300, "예술" : 400, "역사" : 500}
# books = {}
# print("분야: 철학 / 사회과학 / 자연과학 / 예술 / 역사")
# while True:
#   print("책 제목과 분야를 입력해주세요")
#   title = input("책 제목: ")
#   field = input("분야: ")
#   if title == "":
#     book_sort(books)
#     break
#   books.setdefault(title, (field, fd_dict[field]))

# ## [도전문제 2] ##############################################################
# numbers = set([])
# zeroTonine = set([x for x in range(0, 10)])
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# # set 자료형도 sum 함수가 적용가능함.

# # 없는 수 더하기 함수
# def plus1(N): #45에서 입력받은 수의 합계를 빼는 함수
#   global result1
#   result1 = 45-sum(N)
#   return result1

# def plus2(N): #set 자료형 특성을 이용한 함수
#   global result2
#   result2 = sum(zeroTonine - N)
#   return result2

# def plus3(N): # 순차탐색을 이용하여 없는 수를 더한 함수
#   global result3
#   result3 = 0
#   for i in zeroTonine:
#     if i not in N:
#       result3 += i
#   return result3

# # 원소 입력
# while True:
#   try:
#     cnt = int(input("원소 갯수 입력 (1~9개 입력 가능. 종료 0): "))
#     if cnt == 0:
#       print("종료")
#       break
#     elif cnt < 1 or cnt > 9:
#       print("갯수를 다시 입력해주세요")
#       continue
#   except:
#     continue
  
#   for i in range(0, cnt): 
#     try:
#       number = int(input("0부터 9사이의 숫자(원소) 입력: "))
#       numbers.add(number)
#     except:
#       continue
  
# # 부족한 원소 충족하기
# # 중복 삭제로 숫자가 부족하게 되면 cnt 갯수 충족하도록
# # for문으로 입력하기 때문에 초과입력은 x
#   while True:
#     if len(numbers) == cnt:
#       break
#     else:
#       for i in range(cnt - len(numbers)):
#         print(f"현재 원소: {numbers}")
#         numbers.update([int(input("추가할 숫자 다시 입력: "))])
  
# # 결과
#   print(f"입력받은 원소: {numbers}")
#   print(f"없는 원소 합계: {plus1(numbers)}")
#   print(f"없는 원소 합계: {plus2(numbers)}")
#   print(f"없는 원소 합계: {plus3(numbers)}")

# 버블 정렬로 똑같은 위치를 찾아 가장 작은 수 제거
# def bubble_arr(cnt, array): # 정렬함수
#   global arr2 #arr2는 정렬된 배열
#   arr2 = array
#   for cur in range(cnt): # 정렬
#     if cur == len(array) - 1:
#       break
#     else:
#       if arr2[cur] > arr2[cur+1]:
#         arr2[cur], arr2[cur+1] = arr2[cur+1], arr2[cur]
#   # for i in array:
#   #   if i == arr2[0]:
#   #     array.remove(i)
#   # if len(array) == 0:
#   #   array.append(-1)
#   return arr2

# while True:
#   arr1 = []
#   try: #원소 갯수 (몇번 넣을 건지)
#     cnt = int(input("원소 갯수 입력 (종료 0): "))
#     if cnt == 0:
#       print("종료")
#       break
#   except:
#     continue
#   for i in range(0, cnt): #원소 입력
#     try:
#       element = int(input("숫자(원소) 입력: "))
#       arr1.append(element)
#     except:
#       continue
  
#   print(f"기존 배열: {arr1}")
#   print(f"가장 작은 원소 제거 후 배열: {bubble_arr(cnt, arr1)}")

## 