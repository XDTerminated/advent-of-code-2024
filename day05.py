from functools import cmp_to_key
from itertools import combinations


def take_input():
    rules, updates, section = set(), [], 0
    while True:
        line = input()
        if not line:
            if section == 0:
                section = 1
                continue
            break
        if section == 0:
            a, b = map(int, line.split("|"))
            rules.add((a, b))
        else:
            updates.append([int(x) for x in line.split(",")])
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
