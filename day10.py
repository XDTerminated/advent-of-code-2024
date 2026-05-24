DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def take_input():
    grid = []
    while line := input():
        grid.append([int(c) for c in line])
    return grid


def trails_from(grid, i, j):
    if grid[i][j] == 9:
        yield (i, j)
        return
    rows, cols = len(grid), len(grid[0])
    for di, dj in DIRECTIONS:
        ni, nj = i + di, j + dj
        if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == grid[i][j] + 1:
            yield from trails_from(grid, ni, nj)


def trailheads(grid):
    return [(i, j) for i, row in enumerate(grid) for j, v in enumerate(row) if v == 0]


def part1(grid):
    return sum(len(set(trails_from(grid, i, j))) for i, j in trailheads(grid))


def part2(grid):
    return sum(len(list(trails_from(grid, i, j))) for i, j in trailheads(grid))


grid = take_input()
print(part1(grid))
print(part2(grid))
