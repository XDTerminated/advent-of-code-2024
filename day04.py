DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def take_input():
    grid = []
    while line := input():
        grid.append(line)
    return grid


def part1(grid):
    rows, cols = len(grid), len(grid[0])

    def is_xmas(i, j, dx, dy):
        if not (0 <= i + 3 * dx < rows and 0 <= j + 3 * dy < cols):
            return False
        return "".join(grid[i + k * dx][j + k * dy] for k in range(4)) == "XMAS"

    return sum(
        is_xmas(i, j, dx, dy)
        for i in range(rows)
        for j in range(cols)
        for dx, dy in DIRECTIONS
    )


def part2(grid):
    rows, cols = len(grid), len(grid[0])
    valid = {"MAS", "SAM"}
    return sum(
        grid[i][j] == "A"
        and grid[i - 1][j - 1] + "A" + grid[i + 1][j + 1] in valid
        and grid[i - 1][j + 1] + "A" + grid[i + 1][j - 1] in valid
        for i in range(1, rows - 1)
        for j in range(1, cols - 1)
    )


grid = take_input()
print(part1(grid))
print(part2(grid))
