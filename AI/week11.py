# # 퀵 정렬 & 병합 정렬
# # 실습문제 2 : 퀵 정렬 단계마다 결과 확인
# def quick_sorted(arr):
#   # print(f'퀵정렬 전: {arr}')
#   if len(arr) > 1:
#     pivot = arr[0]
#     left, mid, right = [], [], []
#     for i in range(len(arr)):
#       if arr[i] < pivot:
#         left.append(arr[i])
#       elif arr[i] > pivot:
#         right.append(arr[i])
#       else:
#         mid.append(arr[i])
#     # print(f"피봇: {pivot}, 정렬: {arr}")
#     process = left + mid + right
#     print(f"피봇: {pivot}, 정렬: {process}")
#     # print(f"피봇: {pivot}, 정렬: {left,mid, right}")
#     return quick_sorted(left) + mid + quick_sorted(right)
#   else:
#     return arr
# arr = [30, 49, 66, 58, 10, 99, 78, 17, 41, 23]
# print(f'퀵정렬 후: {quick_sorted(arr)}')


### 병합 정렬################
# def merge_sort(list): # partitioning
#     list_length = len(list)
#     if list_length == 1:
#         return list
#     mid_point = list_length // 2
#     left_partition = merge_sort(list[:mid_point])
#     right_partition = merge_sort(list[mid_point:])
#     return merge(left_partition, right_partition)

# def merge(left, right): # actual sorting
#     output = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             output.append(left[i])
#             i += 1
#         else:
#             output.append(right[j])
#             j += 1
#     output.extend(left[i:])
#     output.extend(right[j:])
#     return output

# def run_merge_sort():
#     unsorted_list = [4, 1, 5, 7, 2, 6, 1, 1, 6, 4, 10, 33, 5, 7, 23]
#     print(unsorted_list)
#     sorted_list = merge_sort(unsorted_list)
#     print(sorted_list)

# run_merge_sort()

# 도전문제2
# best solution
def sort_max(sequence):
    for i in sequence:
        for j in i:
            pass


# n = len(sequence)
#   for i in range(n-1, 0, -1):
#     for j in range(i):
#         for x, y in sequence[j], sequence[j+1]:
            
#         # print(sequence[j], sequence[j+1])

# #   for i in sequence:
# #         for j in i:
# #             print(j)
try:
  sequence = list(filter(lambda x : int(x) >= 0, list(input("자료 값 입력: ").split())))
  output = []
  
except:
    print("다시 입력")  

from functools import reduce
try:
  sequence = list(filter(lambda x : int(x) >= 0, list(input("자료 값 입력: ").split())))
  output = reduce(lambda x, y : max(x+y, y+x), sorted(sequence))
  print(output)
  
except:
    print("다시 입력")  

# try:
#   sequence = list(filter(lambda x : int(x) >= 0, list(input("자료 값 입력: ").split())))
#   a = sorted(sequence)
#   for x, y in a:
#     a = max(x+y, y+x)
#     print(a)
#     # print(max(x + y, y+x))
#   # print(sorted(sequence)) ['3', '30', '34', '5', '9']


# except:
#   print("다시 입력")