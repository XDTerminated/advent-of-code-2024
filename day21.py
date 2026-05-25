import functools

NUMERIC = {
    "7": (0, 0), "8": (0, 1), "9": (0, 2),
    "4": (1, 0), "5": (1, 1), "6": (1, 2),
    "1": (2, 0), "2": (2, 1), "3": (2, 2),
    "0": (3, 1), "A": (3, 2),
}
NUMERIC_GAP = (3, 0)

DIRECTIONAL = {
    "^": (0, 1), "A": (0, 2),
    "<": (1, 0), "v": (1, 1), ">": (1, 2),
}
DIRECTIONAL_GAP = (0, 0)


def shortest_paths(c1, c2, keypad, gap):
    r1, col1 = keypad[c1]
    r2, col2 = keypad[c2]
    dr, dc = r2 - r1, col2 - col1
    vert = "v" * dr if dr > 0 else "^" * (-dr)
    horiz = ">" * dc if dc > 0 else "<" * (-dc)
    paths = []
    if (r2, col1) != gap:
        paths.append(vert + horiz)
    if (r1, col2) != gap and horiz + vert != vert + horiz:
        paths.append(horiz + vert)
    return paths


@functools.lru_cache(maxsize=None)
def move_cost(c1, c2, depth, is_numeric):
    keypad = NUMERIC if is_numeric else DIRECTIONAL
    gap = NUMERIC_GAP if is_numeric else DIRECTIONAL_GAP
    paths = shortest_paths(c1, c2, keypad, gap)
    if depth == 0:
        return len(paths[0]) + 1
    best = float("inf")
    for path in paths:
        total = 0
        prev = "A"
        for ch in path + "A":
            total += move_cost(prev, ch, depth - 1, False)
            prev = ch
        if total < best:
            best = total
    return best


def code_cost(code, dir_layers):
    total = 0
    prev = "A"
    for ch in code:
        total += move_cost(prev, ch, dir_layers, True)
        prev = ch
    return total


def take_input():
    codes = []
    while line := input():
        codes.append(line)
    return codes


def numeric_part(code):
    return int("".join(c for c in code if c.isdigit()))


def part1(codes):
    return sum(code_cost(c, 2) * numeric_part(c) for c in codes)


def part2(codes):
    return sum(code_cost(c, 25) * numeric_part(c) for c in codes)


codes = take_input()
print(part1(codes))
print(part2(codes))
