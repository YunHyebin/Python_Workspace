# from functools import reduce
# try:
#   sequence = list(filter(lambda x : int(x) >= 0, list(input("자료 값 입력: ").split())))
#   output = reduce(lambda x, y : max(x+y, y+x), sorted(sequence))
#   print(output)
  
# except:
#     print("다시 입력")  

# # try:
# #   sequence = list(filter(lambda x : int(x) >= 0, list(input("자료 값 입력: ").split())))
# #   a = sorted(sequence)
# #   for x, y in a:
# #     a = max(x+y, y+x)
# #     print(a)
# #     # print(max(x + y, y+x))
# #   # print(sorted(sequence)) ['3', '30', '34', '5', '9']


# # except:
# #   print("다시 입력")

arr = list(map(int, (input("자료 값 띄어서 입력: ").split()))).sort()
print(arr)