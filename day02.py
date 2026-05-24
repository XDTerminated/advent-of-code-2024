input_data = []
safe = 0

while True:
    line = input()
    if not line:
        break

    row = [int(x) for x in line.split()]
    input_data.append(row)


def is_safe(levels):
    if len(levels) <= 1:
        return False

    is_increasing = True
    is_decreasing = True

    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i]

        if not (1 <= abs(diff) <= 3):
            return False

        if diff > 0:
            is_decreasing = False
        if diff < 0:
            is_increasing = False

        if not (is_increasing or is_decreasing):
            return False

    return True


safe = 0
for row in input_data:
    if is_safe(row):
        safe += 1

print(safe)


def is_safe_2(levels):
    if is_safe(levels):
        return True

    for i in range(len(levels)):
        dampened = levels[:i] + levels[i + 1 :]

        if is_safe(dampened):
            return True

    return False


safe = 0
for row in input_data:
    if is_safe_2(row):
        safe += 1

print(safe)
