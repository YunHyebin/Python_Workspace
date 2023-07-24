wordsList = []
cnt = int(input("단어 개수: "))
for i in range(cnt):
    wordsList.append(input("단어: "))

print(wordsList)


for i in range(cnt):
        print(f"Case #{cnt} :" + wordsList.pop())