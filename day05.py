import sys
from functools import cmp_to_key
from itertools import combinations


def take_input():
    rules_block, updates_block = sys.stdin.read().split("\n\n", 1)
    rules = {tuple(map(int, line.split("|"))) for line in rules_block.splitlines()}
    updates = [list(map(int, line.split(","))) for line in updates_block.splitlines()]
    return rules, updates


def is_ordered(rules, update):
    return all((b, a) not in rules for a, b in combinations(update, 2))


def reorder(rules, update):
    def cmp(a, b):
        return -1 if (a, b) in rules else 1 if (b, a) in rules else 0

    return sorted(update, key=cmp_to_key(cmp))


def middle(seq):
    return seq[len(seq) // 2]


def part1(rules, updates):
    return sum(middle(u) for u in updates if is_ordered(rules, u))


def part2(rules, updates):
    return sum(middle(reorder(rules, u)) for u in updates if not is_ordered(rules, u))


rules, updates = take_input()
print(part1(rules, updates))
print(part2(rules, updates))
