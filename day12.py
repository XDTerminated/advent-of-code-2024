DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def take_input():
    grid = []
    while line := input():
        grid.append(line)
    return grid


def regions(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    for i in range(rows):
        for j in range(cols):
            if (i, j) in visited:
                continue
            label = grid[i][j]
            region = set()
            stack = [(i, j)]
            while stack:
                p = stack.pop()
                if p in region:
                    continue
                region.add(p)
                visited.add(p)
                for di, dj in DIRECTIONS:
                    ni, nj = p[0] + di, p[1] + dj
                    if (
                        0 <= ni < rows
                        and 0 <= nj < cols
                        and grid[ni][nj] == label
                        and (ni, nj) not in region
                    ):
                        stack.append((ni, nj))
            yield region


def perimeter(region):
    return sum(
        (r + di, c + dj) not in region for r, c in region for di, dj in DIRECTIONS
    )


def sides(region):
    total = 0
    for r, c in region:
        for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            v = (r + dr, c) in region
            h = (r, c + dc) in region
            d = (r + dr, c + dc) in region
            if not v and not h:
                total += 1
            elif v and h and not d:
                total += 1
    return total


def part1(grid):
    return sum(len(r) * perimeter(r) for r in regions(grid))


def part2(grid):
    return sum(len(r) * sides(r) for r in regions(grid))


grid = take_input()
print(part1(grid))
print(part2(grid))
