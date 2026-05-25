from collections import defaultdict


def take_input():
    edges = []
    while line := input():
        a, b = line.split("-")
        edges.append((a, b))
    return edges


def build_graph(edges):
    g = defaultdict(set)
    for a, b in edges:
        g[a].add(b)
        g[b].add(a)
    return g


def triangles(g):
    found = set()
    for a, neighbors in g.items():
        for b in neighbors:
            for c in g[b]:
                if c in neighbors and c != a:
                    found.add(tuple(sorted([a, b, c])))
    return found


def part1(edges):
    g = build_graph(edges)
    return sum(
        1 for t in triangles(g) if any(x.startswith("t") for x in t)
    )


def bron_kerbosch(R, P, X, g, cliques):
    if not P and not X:
        cliques.append(R)
        return
    pivot = max(P | X, key=lambda v: len(P & g[v]))
    for v in list(P - g[pivot]):
        bron_kerbosch(R | {v}, P & g[v], X & g[v], g, cliques)
        P = P - {v}
        X = X | {v}


def part2(edges):
    g = build_graph(edges)
    cliques = []
    bron_kerbosch(set(), set(g.keys()), set(), g, cliques)
    largest = max(cliques, key=len)
    return ",".join(sorted(largest))


edges = take_input()
print(part1(edges))
print(part2(edges))
