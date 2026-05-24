def take_input():
    equations = []
    while line := input():
        target, rest = line.split(":")
        equations.append((int(target), [int(x) for x in rest.split()]))
    return equations


def can_make(target, numbers, ops):
    *rest, last = numbers
    if not rest:
        return target == last
    for op in ops:
        if op == "+" and target > last and can_make(target - last, rest, ops):
            return True
        if op == "*" and target % last == 0 and can_make(target // last, rest, ops):
            return True
        if op == "||":
            t, s = str(target), str(last)
            if len(t) > len(s) and t.endswith(s) and can_make(int(t[: -len(s)]), rest, ops):
                return True
    return False


def solve(equations, ops):
    return sum(t for t, nums in equations if can_make(t, nums, ops))


def part1(equations):
    return solve(equations, ("+", "*"))


def part2(equations):
    return solve(equations, ("+", "*", "||"))


equations = take_input()
print(part1(equations))
print(part2(equations))
