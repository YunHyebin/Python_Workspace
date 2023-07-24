def GymSuit(n, lost, reverse) :
    count = n - len(lost) + len(reverse) + len(reverse)
    for i in lost :
        if i + 1 in reverse:
            reverse.remove(i + 1)
            count += 1
    return count

n = 3
lost = [3]
reverse = [1]
print(f"체육 수업에 참여한 학생 수: {GymSuit(n, lost, reverse)}")
