from collections import defaultdict


def take_input():
    values = {}
    gates = []
    section = 0
    while True:
        line = input()
        if not line:
            if section == 0:
                section = 1
                continue
            break
        if section == 0:
            wire, val = line.split(": ")
            values[wire] = int(val)
        else:
            inp, out = line.split(" -> ")
            a, op, b = inp.split()
            gates.append((a, op, b, out))
    return values, gates


def evaluate(values, gates):
    gate_by_out = {out: (a, op, b) for a, op, b, out in gates}
    cache = dict(values)

    def get(wire):
        if wire in cache:
            return cache[wire]
        a, op, b = gate_by_out[wire]
        va, vb = get(a), get(b)
        cache[wire] = {"AND": va & vb, "OR": va | vb, "XOR": va ^ vb}[op]
        return cache[wire]

    for wire in gate_by_out:
        get(wire)
    return cache


def part1(values, gates):
    result = evaluate(values, gates)
    z_wires = sorted((w for w in result if w.startswith("z")), reverse=True)
    return int("".join(str(result[w]) for w in z_wires), 2)


def part2(values, gates):
    max_z = max(out for _, _, _, out in gates if out.startswith("z"))

    gates_using = defaultdict(list)
    for a, op, b, out in gates:
        gates_using[a].append(op)
        gates_using[b].append(op)

    wrong = set()
    for a, op, b, out in gates:
        if out.startswith("z") and out != max_z and op != "XOR":
            wrong.add(out)
        if out == max_z and op != "OR":
            wrong.add(out)
        if op == "XOR" and not out.startswith("z"):
            if not (a.startswith(("x", "y")) and b.startswith(("x", "y"))):
                wrong.add(out)
        if op == "AND" and {a, b} != {"x00", "y00"}:
            if any(next_op != "OR" for next_op in gates_using[out]):
                wrong.add(out)
        if op == "XOR" and a.startswith(("x", "y")) and b.startswith(("x", "y")):
            if {a, b} != {"x00", "y00"}:
                if any(next_op == "OR" for next_op in gates_using[out]):
                    wrong.add(out)

    return ",".join(sorted(wrong))


values, gates = take_input()
print(part1(values, gates))
print(part2(values, gates))
