from collections import defaultdict
from itertools import combinations


def take_input():
    grid = []
    while line := input():
        grid.append(line)
    return grid


def antennas_by_freq(grid):
    by_freq = defaultdict(list)
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c != ".":
                by_freq[c].append((i, j))
    return by_freq


def in_bounds(grid, pos):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])


def part1(grid):
    antinodes = set()
    for positions in antennas_by_freq(grid).values():
        for a, b in combinations(positions, 2):
            di, dj = a[0] - b[0], a[1] - b[1]
            for p in [(a[0] + di, a[1] + dj), (b[0] - di, b[1] - dj)]:
                if in_bounds(grid, p):
                    antinodes.add(p)
    return len(antinodes)


def part2(grid):
    antinodes = set()
    for positions in antennas_by_freq(grid).values():
        for a, b in combinations(positions, 2):
            di, dj = a[0] - b[0], a[1] - b[1]
            i, j = a
            while in_bounds(grid, (i, j)):
                antinodes.add((i, j))
                i, j = i + di, j + dj
            i, j = b
            while in_bounds(grid, (i, j)):
                antinodes.add((i, j))
                i, j = i - di, j - dj
    return len(antinodes)


grid = take_input()
print(part1(grid))
print(part2(grid))
