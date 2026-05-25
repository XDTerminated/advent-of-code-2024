def take_input():
    schematics = []
    current = []
    while True:
        line = input()
        if not line:
            if not current:
                break
            schematics.append(current)
            current = []
        else:
            current.append(line)
    return schematics


def parse(schematic):
    is_lock = schematic[0] == "#" * len(schematic[0])
    heights = [
        sum(1 for r in range(len(schematic)) if schematic[r][c] == "#") - 1
        for c in range(len(schematic[0]))
    ]
    return is_lock, heights


def part1(schematics):
    locks, keys = [], []
    for s in schematics:
        is_lock, h = parse(s)
        (locks if is_lock else keys).append(h)
    return sum(
        all(li + ki <= 5 for li, ki in zip(lock, key))
        for lock in locks
        for key in keys
    )


schematics = take_input()
print(part1(schematics))
