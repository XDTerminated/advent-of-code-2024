import re

MUL = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
INSTRUCTION = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)")


def take_input():
    lines = []
    while line := input():
        lines.append(line)
    return "".join(lines)


def part1(memory):
    return sum(int(a) * int(b) for a, b in MUL.findall(memory))


def part2(memory):
    total, enabled = 0, True
    for m in INSTRUCTION.finditer(memory):
        token = m.group(0)
        if token == "do()":
            enabled = True
        elif token == "don't()":
            enabled = False
        elif enabled:
            total += int(m.group(1)) * int(m.group(2))
    return total


memory = take_input()
print(part1(memory))
print(part2(memory))
