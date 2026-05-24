import re


def take_input():
    nums = []
    prev_blank = False
    while True:
        line = input()
        if not line:
            if prev_blank:
                break
            prev_blank = True
            continue
        prev_blank = False
        nums.extend(int(x) for x in re.findall(r"\d+", line))
    machines = []
    for i in range(0, len(nums), 6):
        ax, ay, bx, by, px, py = nums[i : i + 6]
        machines.append(((ax, ay), (bx, by), (px, py)))
    return machines


def solve(machines, offset=0):
    total = 0
    for (ax, ay), (bx, by), (px, py) in machines:
        px += offset
        py += offset
        det = ax * by - ay * bx
        if det == 0:
            continue
        a_num = px * by - py * bx
        b_num = ax * py - ay * px
        if a_num % det or b_num % det:
            continue
        a, b = a_num // det, b_num // det
        if a >= 0 and b >= 0:
            total += 3 * a + b
    return total


def part1(machines):
    return solve(machines)


def part2(machines):
    return solve(machines, offset=10**13)


machines = take_input()
print(part1(machines))
print(part2(machines))
