def search_best(answers):
  stu1, stu2, stu3,result = [1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5], [0,0,0]
# enumerate() -> 인덱스와 원소 동시 접근 (인덱스, 원소)
  for index, quiz in enumerate(answers):
    # print(index, quiz)
    if quiz == stu1[index % len(stu1)]:
      result[0] += 1
    if quiz == stu2[index % len(stu2)]:
      result[1] += 1
    if quiz == stu3[index % len(stu3)]:
      result[2] += 1
  answer = [i+1, for i in range(len(result)) if result[i] == max(result)]
  for i in range(len(result)):
    if result[i] == max(result):
      answer.append(i+1)
  for x in range(3):
    if result[x] == len(answers):
      print(f"수포자 {x+1}은 모든 문제 맞힘")
    if result[x] == 0:
      print(f"수포자 {x+1}은 모든 문제 틀림")
  if result[0] == result[1] == result[2]:
    print(f"모든 사람이 {result[0]}문제씩 맞힘")
  return answer

answers = list(map(int, (input("답지 입력: ").split())))
print(f"등수 결과: 수포자{search_best(answers)} ")