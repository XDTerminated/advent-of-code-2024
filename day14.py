import re
from math import prod

W, H = 101, 103


def take_input():
    robots = []
    while line := input():
        px, py, vx, vy = (int(x) for x in re.findall(r"-?\d+", line))
        robots.append(((px, py), (vx, vy)))
    return robots


def part1(robots):
    mx, my = W // 2, H // 2
    quads = [0, 0, 0, 0]
    for (px, py), (vx, vy) in robots:
        x = (px + vx * 100) % W
        y = (py + vy * 100) % H
        if x == mx or y == my:
            continue
        quads[(x < mx) * 2 + (y < my)] += 1
    return prod(quads)


def variance(values):
    mean = sum(values) / len(values)
    return sum((v - mean) ** 2 for v in values)


def part2(robots):
    best_tx = min(
        range(W),
        key=lambda t: variance([(px + vx * t) % W for (px, _), (vx, _) in robots]),
    )
    best_ty = min(
        range(H),
        key=lambda t: variance([(py + vy * t) % H for (_, py), (_, vy) in robots]),
    )
    k = ((best_ty - best_tx) * pow(W, -1, H)) % H
    return best_tx + W * k


robots = take_input()
print(part1(robots))
print(part2(robots))
