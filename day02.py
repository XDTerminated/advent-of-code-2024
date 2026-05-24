def take_input():
    reports = []
    while line := input():
        reports.append([int(x) for x in line.split()])
    return reports


def is_safe(levels):
    diffs = [b - a for a, b in zip(levels, levels[1:])]
    return all(1 <= abs(d) <= 3 for d in diffs) and (
        all(d > 0 for d in diffs) or all(d < 0 for d in diffs)
    )


def part1(reports):
    return sum(is_safe(r) for r in reports)


def part2(reports):
    return sum(
        is_safe(r) or any(is_safe(r[:i] + r[i + 1 :]) for i in range(len(r)))
        for r in reports
    )


reports = take_input()
print(part1(reports))
print(part2(reports))
