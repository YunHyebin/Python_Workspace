n = int(input('반복 횟수: '))
for dataset in range(n):
  result= ''
  line = input(f'{dataset + 1}번째 : ')
  contiguous_current_word = line[0]  #입력받은 글자의 첫번째 글자를 contiguous line word에 저장
  print(contiguous_current_word)
  contiguous_cnt = 0
  check_contiguous = [0 for x in range(200)]
  for char in line:
    if char == contiguous_current_word:
          contiguous_cnt += 1
    else: 
        result += contiguous_current_word
        result += str(contiguous_cnt)

        if check_contiguous[ord(contiguous_current_word)] < contiguous_cnt:
            check_contiguous[ord(contiguous_current_word)] = contiguous_cnt
            

# result = ""
# contiguous_current_word = line[0]  
# contiguous_cnt = 0
# check_contiguous = [0 for _ in range(200)]  # 각 문자의 연속된 길이를 저장하는 리스트
# for char in input:
# 	if char == contiguous_current_word:  #연속이 지속되는 경우라면
# 		contiguous_cnt += 1
# 	else:  # 연속이 깨지는 경우라면
# 		# 값을 확인하기 위한 테스트 변수
# 		result += contiguous_current_word
# 		result += str(contiguous_cnt)

# 		# 그 전까지 연속된 값을 업데이트
# 		if check_contiguous[ord(contiguous_current_word)] < contiguous_cnt:  #그 전까지 계산했던 해당 문자의 연속길이보다 긴 경우만 업데이트
# 			check_contiguous[ord(contiguous_current_word)] = contiguous_cnt
# 		# 연속되는 문자 현재 값으로 세팅
# 		contiguous_current_word = char
# 		contiguous_cnt = 1  # 문자 한개만 있어도 연속 값은 1임
# if check_contiguous[ord(contiguous_current_word)] < contiguous_cnt:  # 마지막 문자에서 연속이 깨지면 업데이트 해줘야함
# 	check_contiguous[ord(contiguous_current_word)] = contiguous_cnt
# # 값을 확인하기 위한 테스트 변수
# result += contiguous_current_word
# result += str(contiguous_cnt)

# print([(chr(i), value) for i, value in enumerate(check_contiguous) if value !=0])
# # 출력: [('a', 6), ('b', 2), ('d', 2), ('e', 1)]
# print(result)
# # 출력: a6b2a1d2e1d1b1