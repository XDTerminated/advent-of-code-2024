def take_input():
    patterns = [p.strip() for p in input().split(",")]
    input()
    designs = []
    while line := input():
        designs.append(line)
    return patterns, designs


def count_ways(design, patterns):
    n = len(design)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for p in patterns:
            if i >= len(p) and design[i - len(p) : i] == p:
                dp[i] += dp[i - len(p)]
    return dp[n]


def part1(patterns, designs):
    return sum(count_ways(d, patterns) > 0 for d in designs)


def part2(patterns, designs):
    return sum(count_ways(d, patterns) for d in designs)


patterns, designs = take_input()
print(part1(patterns, designs))
print(part2(patterns, designs))
