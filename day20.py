from collections import deque

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def take_input():
    grid = []
    while line := input():
        grid.append(line)
    return grid


def find_char(grid, ch):
    for r, row in enumerate(grid):
        for c, x in enumerate(row):
            if x == ch:
                return r, c


def distances_from(grid, start):
    dist = {start: 0}
    queue = deque([start])
    while queue:
        r, c = queue.popleft()
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if grid[nr][nc] != "#" and (nr, nc) not in dist:
                dist[(nr, nc)] = dist[(r, c)] + 1
                queue.append((nr, nc))
    return dist


def count_cheats(grid, max_cheat, min_save):
    dist = distances_from(grid, find_char(grid, "S"))
    count = 0
    for (r, c), d_a in dist.items():
        for dr in range(-max_cheat, max_cheat + 1):
            for dc in range(-max_cheat, max_cheat + 1):
                m = abs(dr) + abs(dc)
                if m == 0 or m > max_cheat:
                    continue
                b = (r + dr, c + dc)
                if b in dist and dist[b] - d_a - m >= min_save:
                    count += 1
    return count


def part1(grid):
    return count_cheats(grid, 2, 100)


def part2(grid):
    return count_cheats(grid, 20, 100)


grid = take_input()
print(part1(grid))
print(part2(grid))
