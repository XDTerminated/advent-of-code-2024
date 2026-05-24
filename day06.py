DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def take_input():
    grid = []
    while line := input():
        grid.append(line)
    return grid


def find_start(grid):
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == "^":
                return i, j


def walk(grid, start, extra=None):
    rows, cols = len(grid), len(grid[0])
    pos, d = start, 0
    visited, seen = set(), set()
    while 0 <= pos[0] < rows and 0 <= pos[1] < cols:
        if (pos, d) in seen:
            return visited, True
        seen.add((pos, d))
        visited.add(pos)
        ni, nj = pos[0] + DIRECTIONS[d][0], pos[1] + DIRECTIONS[d][1]
        if (
            0 <= ni < rows
            and 0 <= nj < cols
            and (grid[ni][nj] == "#" or (ni, nj) == extra)
        ):
            d = (d + 1) % 4
        else:
            pos = (ni, nj)
    return visited, False


def part1(grid):
    visited, _ = walk(grid, find_start(grid))
    return len(visited)


def part2(grid):
    start = find_start(grid)
    visited, _ = walk(grid, start)
    visited.discard(start)
    return sum(walk(grid, start, extra=cell)[1] for cell in visited)


grid = take_input()
print(part1(grid))
print(part2(grid))
