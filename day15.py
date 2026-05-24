MOVEMENTS = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}
WIDEN = {"#": "##", "O": "[]", ".": "..", "@": "@."}


def take_input():
    warehouse, directions, section = [], [], 0
    while True:
        line = input()
        if not line:
            if section == 0:
                section = 1
                continue
            break
        if section == 0:
            warehouse.append(list(line))
        else:
            directions.append(line)
    return warehouse, "".join(directions)


def find_robot(warehouse):
    for y, row in enumerate(warehouse):
        for x, c in enumerate(row):
            if c == "@":
                return x, y


def part1(warehouse, directions):
    warehouse = [row[:] for row in warehouse]
    rx, ry = find_robot(warehouse)
    for d in directions:
        dx, dy = MOVEMENTS[d]
        nx, ny = rx + dx, ry + dy
        ex, ey = nx, ny
        while warehouse[ey][ex] == "O":
            ex += dx
            ey += dy
        if warehouse[ey][ex] == "#":
            continue
        if (ex, ey) != (nx, ny):
            warehouse[ey][ex] = "O"
        warehouse[ny][nx] = "@"
        warehouse[ry][rx] = "."
        rx, ry = nx, ny
    return sum(
        100 * y + x
        for y, row in enumerate(warehouse)
        for x, c in enumerate(row)
        if c == "O"
    )


def widen(warehouse):
    return [list("".join(WIDEN[c] for c in row)) for row in warehouse]


def part2(warehouse, directions):
    warehouse = widen(warehouse)
    rx, ry = find_robot(warehouse)

    def box_at(x, y):
        if warehouse[y][x] == "[":
            return (x, y)
        if warehouse[y][x] == "]":
            return (x - 1, y)
        return None

    for d in directions:
        dx, dy = MOVEMENTS[d]
        if dy == 0:
            ex = rx + dx
            while warehouse[ry][ex] in "[]":
                ex += dx
            if warehouse[ry][ex] == "#":
                continue
            x = ex
            while x != rx + dx:
                warehouse[ry][x] = warehouse[ry][x - dx]
                x -= dx
            warehouse[ry][rx + dx] = "@"
            warehouse[ry][rx] = "."
            rx += dx
        else:
            if warehouse[ry + dy][rx] == "#":
                continue
            to_move, seen = [], set()
            frontier = [(rx, ry + dy)]
            blocked = False
            while frontier:
                x, y = frontier.pop()
                b = box_at(x, y)
                if b is None or b in seen:
                    continue
                seen.add(b)
                to_move.append(b)
                bx, by = b
                ny = by + dy
                for cx in (bx, bx + 1):
                    if warehouse[ny][cx] == "#":
                        blocked = True
                        break
                    frontier.append((cx, ny))
                if blocked:
                    break
            if blocked:
                continue
            for bx, by in to_move:
                warehouse[by][bx] = "."
                warehouse[by][bx + 1] = "."
            for bx, by in to_move:
                warehouse[by + dy][bx] = "["
                warehouse[by + dy][bx + 1] = "]"
            warehouse[ry + dy][rx] = "@"
            warehouse[ry][rx] = "."
            ry += dy

    return sum(
        100 * y + x
        for y, row in enumerate(warehouse)
        for x, c in enumerate(row)
        if c == "["
    )


warehouse, directions = take_input()
print(part1(warehouse, directions))
print(part2(warehouse, directions))
