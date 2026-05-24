test_value = []
numbers = []
total = 0

with open("input.txt") as f:
    for line in f:
        line = line.strip().split(":")
        test_value.append(int(line[0]))
        numbers.append(list(map(int, line[1].split())))


def helper(test_value, numbers):
    for i in range(2 ** (len(numbers) - 1)):
        operations = bin(i)[2:].zfill(len(numbers) - 1)
        total = numbers[0]
        for j in range(len(operations)):
            if operations[j] == "0":
                total += numbers[j + 1]
            elif operations[j] == "1":
                total *= numbers[j + 1]
        if total == test_value:
            return True

    return False


def ter(num):
    if num == 0:
        return "0"
    res = ""
    while num:
        res += str(num % 3)
        num //= 3
    return res[::-1]


def helper2(test_value, numbers):
    for i in range(3 ** (len(numbers) - 1)):
        operations = ter(i).zfill(len(numbers) - 1)
        total = numbers[0]
        for j in range(len(operations)):
            if operations[j] == "0":
                total += numbers[j + 1]
            elif operations[j] == "1":
                total *= numbers[j + 1]
            else:
                total = int(str(total) + str(numbers[j + 1]))
        if total == test_value:
            return True

    return False


for i in range(len(test_value)):
    if helper2(test_value[i], numbers[i]):
        total += test_value[i]

print(total)
