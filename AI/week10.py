# # # # ## 실습문제 4,5 문제 변형 #########################################
# # # # def insertion_sort(arr):
# # # #   for x in range(1, len(arr)):  
# # # #     key = arr[x] # 기준 키 arr의 두번째부터 5, 3, 1, 2
# # # #     y = x - 1 # 비교할 값 (기준 키의 앞의 요소 idx) 0, 1, 2, 3
# # # #     while arr[y] > key and y >= 0: # 정렬이 될 때까지 반복
# # # #       arr[y+1] = arr[y] # 기준 키의 원래 위치에 앞의 요소 복사
# # # #       y = y-1 # 비교할 값의 인덱스를 더 앞으로 바꿔 기준 키 앞에 있는 모든 요소와 비교
# # # #       arr[y+1] = key # 교환 후 기준 키를 다음 요소로 바꿈
# # # #     print(f"{x}단계: {arr}, key = {key}")
# # # #   return arr

# # # # while True:
# # # #   array = []
# # # #   try:
# # # #     num = int(input("자료 갯수 입력 (종료0)"))
# # # #     if num == 0:
# # # #       print("종료")
# # # #       break
# # # #     for i in range(num):
# # # #       element = int(input("자료 요소 입력: "))

# # # #   except ValueError:
# # # #     print('다시 입력해주세요')
# # # #     continue


# # # # print(f"삽입정렬 후 : {insertion_sort(array)}")

# # # ## [도전문제2] ##############################################################
# # # Info = []
# # # # 국가 무역 정보 입력 함수
# # # def create_info(nation, ip, xp): 
# # #   net = xp - ip
# # #   Info.append({nation: (ip, xp, net)})
# # # # 국가 무역 정보 보기 함수
# # # def read_info():
# # #   Info_list = []
# # #   for a in Info:
# # #     Info_list.append(list(a) + list(a.values()))
# # #   while True:
# # #     try:
# # #       choice = int(input("1. 국가별 정렬 2. 순이익별 정렬 3. 전체 메뉴로 가기: "))
# # #       if choice == 1: # 국가별 정렬 (삽입 정렬 이용)
# # #         for x in range(1, len(Info_list)):
# # #           key = Info_list[x]
# # #           y = x -1
# # #           while Info_list[y][0] > key[0] and y >=0:
# # #             Info_list[y+1] = Info_list[y]
# # #             y = y - 1
# # #             Info_list[y+1] = key
# # #         print("국가".center(10), "수입액".center(10), "수출액".center(10))
# # #         print("{:-<30}".format("-"))
# # #         for a in Info_list:
# # #           print("%-13s%-13d%-13d" %(a[0], a[1][0], a[1][1]))

# # #       elif choice == 2: #순이익별 정렬 (선택 정렬 이용)  
# # #         for i in range(len(Info_list) - 1):
# # #           for j in range(i + 1, len(Info_list)):
# # #             # print(Info_list[i][1][2], Info_list[j][1][2])
# # #              if Info_list[i][1][2] < Info_list[j][1][2]:
# # #               Info_list[i], Info_list[j] = Info_list[j], Info_list[i]
# # #         print("국가".center(13), "순수익".center(13))
# # #         print("{:-<30}".format("-"))
# # #         for a in Info_list:
# # #           print("%-13s%-13d" %(a[0], a[1][2]))
# # #       elif choice == 3: # 반복문 탈출 -> 
# # #         print("전체 메뉴로 나갑니다\n")
# # #         break
# # #     except:
# # #       print("다시 입력해주세요")
# # #       continue
# # # #국가 무역 정보 수정 함수
# # # def update_info(): 
# # #   global ip
# # #   global xp
# # #   global net
# # #   global nation
# # #   while True:
# # #     try:
# # #       nation = input("수정할 국가명 입력: ")
# # #       for a in Info:
# # #         if nation == a[0]:
# # #           ip = int(input("수입 재입력: "))
# # #           xp = int(input("수출 재입력: "))
# # #           net = xp-ip
# # #           Info[nation] = (ip, xp, net)
# # #           print(f"{nation}의 정보 수정이 완료되었습니다\n")          
# # #         else:
# # #           print(f"{nation}은(는) 무역 정보에 없습니다.\n다시 입력해주시기 바랍니다\n")
# # #           continue
# # #     except ValueError:
# # #       print("다시 입력해주세요\n")
# # # # 국가 무역 정보 삭제 함수
# # # def delete_info(): 
# # #   nation = input("삭제할 국가명 입력: ")
# # #   for x in Info:
# # #     if nation not in x.keys():
# # #       print(f"{nation}은(는) 무역 정보에 없습니다.\n 다시 입력해주시기 바랍니다\n")
# # #     else:
# # #       del x[nation]
# # #       print(f"{nation}의 무역 정보 삭제가 완료되었습니다\n")

# # # # 무역 시스템 
# # # while True:
# # #   try:
# # #     menu = int(input("\n1. 국가 수입수출 정보 입력\n2. 정렬 보기\n3. 국가 무역 정보 수정\n4. 국가 무역 정보 삭제\n0. 종료\n: "))
# # #     if menu == 0:
# # #       print("종료합니다\n")
# # #       break
# # #     elif menu == 1: # 정보입력
# # #       nation = input("\n국가명: ")
# # #       ip = int(input("수입: "))
# # #       xp = int(input("수출: "))
# # #       create_info(nation, ip, xp)
# # #     elif menu == 2: # 정렬 보기
# # #       read_info()
# # #     elif menu == 3: # 정보 수정
# # #       update_info()
# # #     elif menu == 4: #정보 삭제
# # #       delete_info()
# # #   except:
# # #     continue
  
# # ## 도전문제3 ########################################
# # def selection_sort(arr): # 선택정렬
# #   for i in range(len(arr)-1): 
# #     for j in range(i, len(arr)): 
# #       if arr[i] > arr[j]:
# #         arr[i], arr[j] = arr[j], arr[i]
# #   return arr

# # def insertion_sort(arr): # 삽입정렬
# #   for end in range(1, len(arr)):
# #     # print(end) # end = 1, 2, 3, 4
# #     for i in range(end, 0, -1):
# #       # print(end, i)
# #       if arr[i-1] > arr[i]:
# #         arr[i-1] , arr[i] = arr[i], arr[i-1]
# #   return arr

# # def bubble_sort(arr): # 버블정렬
# #   n = len(arr)
# #   for i in range(n - 1):
# #     for j in range(n-1, i, -1):
# #       if arr[j-1] > arr[j]:
# #         arr[j-1],  arr[j] = arr[j], arr[j-1]
# #   return arr 

# # while True:
# #   try:
# #     cnt = int(input("요소 갯수 입력 (종료 0): "))
# #     if cnt == 0:
# #       break
# #     array = []
# #     for i in range(cnt):
# #       array.append(int(input("요소 입력: ")))
# #     divisor = int(input("나눌 몫 입력: "))
# #     result = list(filter(lambda x: (x % divisor == 0), array))
# #     if len(result) == 0:
# #       result.append(-1)
# #     print(f"버블정렬 return: {bubble_sort(result)}")
# #     print(f"선택정렬 return: {selection_sort(result)}")
# #     print(f"삽입정렬 return: {insertion_sort(result)}")
# #   except ValueError:
# #     print("다시 입력해주세요.")  
# #     continue

# ## 도전문제4 ###################################################
# def selection_sort(arr):
#   for i in range(len(arr)-1): 
#     for j in range(i, len(arr)):
#       if arr[i] > arr[j]:
#         arr[i], arr[j] = arr[j], arr[i]
#   return arr
  
# def check_budget(d, budget):
#   global result 
#   global ok_d
#   global need_budget
#   need_budget = 0
#   ok_d = []
#   d_sort = selection_sort(d)
#   for i in d_sort:
#     if budget >= i:
#       budget -= i
#       need_budget += i
#       ok_d.append(i)
#   result = len(ok_d) # 최대 부서 갯수
#   return ok_d, need_budget, result

# while True:
#   try:  
#     cnt = int(input("\n부서 갯수 입력 (종료 0): "))
#     if cnt == 0:
#       break
#     d = []
#     for i in range(cnt):
#       d.append(int(input("신청 금액 입력: ")))
#     budget = int(input("예산 입력: "))
#     ok_d, need_budget, cnt_d = check_budget(d, budget)
#     print(f"{ok_d}원을 신청한 부서의 물품 구매에는 {need_budget}원 필요")
#     print(f"지원 가능한 최대 부서 갯수: {cnt_d}")
#   except ValueError:
#     print("다시 입력해주세요")
#     continue

### 도전문제5 ##########################################

def number_k(array, commands):
  pass

while True:
  try:
    arr = input("요소입력 (띄어쓰기, 갯수 100개 초과 입력 x) (종료 0) : ")
    if arr == "0":
      print("종료")
      break
    array = list(map(int, arr.split(" ")))
    if len(array) > 100:
      print("원소를 초과 입력하였습니다.\n 다시 입력해주세요.")
      continue
    print(f"원소: {array}")

    print("알고싶은 k번째 수 갯수는 1이상 50 이하로 입력하셔야 합니다.")
    command_cnt = int(input("알고싶은 k번째 수 갯수 입력: "))
    if (0 > command_cnt) or (command_cnt > 50):
      print('알고싶은 k번째 수 입력이 범위 안에 있지 못합니다.\n 다시 입력해주세요.')
      continue

    command_list = []
    for a in range(command_cnt):
      first_last_which = input("어디부터 어디까지 잘라 정렬하여 몇번째(k)의 수를 원하십니까?: ")
      command_list.append(list(map(int, first_last_which.split(" "))))
    while True:
      for b in command_list:
        if (b[1] > max(array)) or (len(b) > 3):
          command_list.remove(b)
          print("정렬할 숫자가 초과되어 다시 입력합니다.")
          first_last_which = input("어디부터 어디까지 잘라 정렬하여 몇번째(k)의 수를 원하십니까?: ")
          command_list.append(list(map(int, first_last_which.split(" "))))
        else:
          break
    print(command_list)
  except ValueError:
    print("다시 입력")
    continue
