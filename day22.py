from collections import defaultdict

MASK = (1 << 24) - 1


def next_secret(n):
    n = (n ^ (n << 6)) & MASK
    n = (n ^ (n >> 5)) & MASK
    n = (n ^ (n << 11)) & MASK
    return n


def take_input():
    nums = []
    while line := input():
        nums.append(int(line))
    return nums


def part1(nums):
    total = 0
    for n in nums:
        for _ in range(2000):
            n = next_secret(n)
        total += n
    return total


def part2(nums):
    totals = defaultdict(int)
    for n in nums:
        prices = [n % 10]
        for _ in range(2000):
            n = next_secret(n)
            prices.append(n % 10)
        changes = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]
        seen = set()
        for i in range(len(changes) - 3):
            seq = tuple(changes[i : i + 4])
            if seq in seen:
                continue
            seen.add(seq)
            totals[seq] += prices[i + 4]
    return max(totals.values())


nums = take_input()
print(part1(nums))
print(part2(nums))
