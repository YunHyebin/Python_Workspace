# ### 4주차 도전문제 4############################################################
while True:
    play = int(input("냥이가 상자를 가지고 노는 일수 (종료 0): "))
    gohome = int(input("귀가일수: "))
    delay, cnt = 0, 0

for x in range(gohome):
  box = input("빈손 or 상자: ")
  if box == "상자":
    if cnt != play:
      delay += 1
      cnt +=1
    else:
      cnt = 1
      delay += 1
  else: # box == '빈손'
    if cnt > 0 and cnt != play:
      delay += 1
      cnt += 1
  print(f"지연일수: {delay}")
except:
print("잘못 입력하셨습니다.")
continue
### 4주차 도전문제 5############################################################
# # 마을 위치 입력 받아 마을 리스트에 넣고 오름차순 정렬
# import math 
# VilNum = input("마을 개수 : ")
# village = []
# for x in range(1, int(VilNum)+ 1) :
#     village.append(int(input(f"마을{x} 위치: "))) 
#     village.sort()

# # 마을과 마을 사이의 길이 구하기
# count = 0
# vill_total = [] #총 마을 사이즈 리스트
# for current in range(0, len(village)):
#     if current == (len(village) - 1):
#         break
#     else:
#         vill_total.append(math.sqrt(pow((village[current] - village[current + 1]), 2)) / 2)

# # 마을 사이 길이 구하여 마을 크기 구하기
# vill_size = []
# for cur in range(0, len(vill_total)) :
#     if cur == (len(vill_total) - 1):
#         break
#     else: 
#         vill_size.append(vill_total[cur] + vill_total[cur + 1])

# # 가장 작은 마을의 크기 구하기
# smallest = vill_size[0]
# for i in vill_size:
#     if i < smallest:
#         smallest = i

# smallest = min(vill_size)

# print(f"가장 작은 마을 크기: {smallest}")

### 4주차 도전문제 6############################################################
# participant = []
# num = int(input("참가자 수: "))
# for i in range(num*2-1):
#     participant.append(input("참가자 이름 입력: "))

# p_set = set(participant)

# for x in p_set:
#     if (participant.count(x) % 2) != 0:
#         print(f"완주하지 못한 참가자: {x}")