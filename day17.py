import re


def take_input():
    text_lines = []
    prev_blank = False
    while True:
        line = input()
        if not line:
            if prev_blank:
                break
            prev_blank = True
            continue
        prev_blank = False
        text_lines.append(line)
    nums = [int(x) for x in re.findall(r"\d+", "\n".join(text_lines))]
    a, b, c, *program = nums
    return a, b, c, program


def run(a, b, c, program):
    output = []
    ip = 0

    def combo(x):
        return x if x < 4 else [a, b, c][x - 4]

    while ip < len(program):
        op, operand = program[ip], program[ip + 1]
        if op == 0:
            a = a >> combo(operand)
        elif op == 1:
            b = b ^ operand
        elif op == 2:
            b = combo(operand) % 8
        elif op == 3:
            if a != 0:
                ip = operand
                continue
        elif op == 4:
            b = b ^ c
        elif op == 5:
            output.append(combo(operand) % 8)
        elif op == 6:
            b = a >> combo(operand)
        elif op == 7:
            c = a >> combo(operand)
        ip += 2
    return output


def part1(a, b, c, program):
    return ",".join(str(x) for x in run(a, b, c, program))


def part2(a, b, c, program):
    candidates = [0]
    for i in range(len(program)):
        new_candidates = []
        for prefix in candidates:
            for digit in range(8):
                candidate = (prefix << 3) | digit
                if run(candidate, b, c, program) == program[-(i + 1) :]:
                    new_candidates.append(candidate)
        candidates = new_candidates
    return min(candidates) if candidates else None


a, b, c, program = take_input()
print(part1(a, b, c, program))
print(part2(a, b, c, program))
