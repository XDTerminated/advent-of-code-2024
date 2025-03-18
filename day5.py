import sys

first = []
second = []
a = 0
sum_middle_valid = 0
sum_middle_invalid = 0

sys.setrecursionlimit(100000)


def check_order(first, second, l):
    valid = True
    for i in range(len(l)):
        for j in range(len(first)):
            if l[i] == first[j]:
                if second[j] in l:
                    if l.index(second[j]) < i:
                        valid = False
                        break

    return valid


# This is a really bad solution btw
def correct_order(first, second, l):
    if check_order(first, second, l):
        return l
    else:
        found = False
        for i in range(len(l)):
            for j in range(len(first)):
                if l[i] == first[j]:
                    if second[j] in l:
                        if l.index(second[j]) < i:
                            l.remove(second[j])
                            l.insert(i, second[j])
                            found = True
                            break
            if found:
                break
        return correct_order(first, second, l)


with open("input.txt") as file:
    for line in file:
        if line == "\n":
            a = 1
            continue

        if a == 0:
            first.append(int(line.strip().split("|")[0]))
            second.append(int(line.strip().split("|")[1]))
        else:
            update = list(map(int, line.strip().split(",")))
            if check_order(first, second, update):
                sum_middle_valid += update[len(update) // 2]
            else:
                a = correct_order(first, second, update)
                sum_middle_invalid += a[len(a) // 2]

print(sum_middle_valid)
print(sum_middle_invalid)
