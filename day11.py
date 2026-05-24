from collections import Counter


def take_input():
    return [int(x) for x in input().split()]


def blink(stones):
    next_stones = Counter()
    for stone, count in stones.items():
        if stone == 0:
            next_stones[1] += count
        else:
            s = str(stone)
            if len(s) % 2 == 0:
                half = len(s) // 2
                next_stones[int(s[:half])] += count
                next_stones[int(s[half:])] += count
            else:
                next_stones[stone * 2024] += count
    return next_stones


def count_after(stones, n):
    stones = Counter(stones)
    for _ in range(n):
        stones = blink(stones)
    return sum(stones.values())


def part1(stones):
    return count_after(stones, 25)


def part2(stones):
    return count_after(stones, 75)


stones = take_input()
print(part1(stones))
print(part2(stones))
