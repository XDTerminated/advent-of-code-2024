from collections import deque

SIZE = 71
PREFIX = 1024


def take_input():
    positions = []
    while line := input():
        x, y = map(int, line.split(","))
        positions.append((x, y))
    return positions


def shortest_path(corrupted):
    queue = deque([((0, 0), 0)])
    visited = {(0, 0)}
    target = (SIZE - 1, SIZE - 1)
    while queue:
        (x, y), d = queue.popleft()
        if (x, y) == target:
            return d
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < SIZE
                and 0 <= ny < SIZE
                and (nx, ny) not in corrupted
                and (nx, ny) not in visited
            ):
                visited.add((nx, ny))
                queue.append(((nx, ny), d + 1))
    return -1


def part1(positions):
    return shortest_path(set(positions[:PREFIX]))


def part2(positions):
    lo, hi = PREFIX, len(positions) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if shortest_path(set(positions[: mid + 1])) == -1:
            hi = mid
        else:
            lo = mid + 1
    x, y = positions[lo]
    return f"{x},{y}"


positions = take_input()
print(part1(positions))
print(part2(positions))
