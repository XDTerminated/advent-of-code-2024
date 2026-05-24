def part1():
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

    sum_of_differences = 0

    for i in range(len(left_list)):
        sum_of_differences += abs(left_list[i] - right_list[i])

    return sum_of_differences


def part2():
    left_list = []
    right_list = []

    while True:
        line = input()
        if not line:
            break

        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

    similarity_score = 0

    for i in range(len(set(left_list))):
        similarity_score += left_list[i] * right_list.count(left_list[i])

    return similarity_score


print(part1())
print(part2())
