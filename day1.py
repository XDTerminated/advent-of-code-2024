left_list = []
right_list = []


while True:
    line = input()
    if not line:
        break

    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)


left_list.sort()
right_list.sort()

sum_difference = 0
similarity_score = 0

for i in range(len(left_list)):
    sum_difference += abs(left_list[i] - right_list[i])

for i in range(len(set(left_list))):
    similarity_score += left_list[i] * right_list.count(left_list[i])


print(sum_difference)
print(similarity_score)
