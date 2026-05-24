def take_input():
    left, right = [], []
    while line := input():
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)
    return sorted(left), sorted(right)


def part1(left, right):
    return sum(abs(l - r) for l, r in zip(left, right))


def part2(left, right):
    return sum(n * right.count(n) for n in left)


left, right = take_input()
print(part1(left, right))
print(part2(left, right))
