import heapq

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def take_input():
    maze = []
    while row := input():
        maze.append(list(row))
    return maze


def find_char(maze, ch):
    for r, row in enumerate(maze):
        for c, x in enumerate(row):
            if x == ch:
                return r, c


def part1(maze):
    sr, sc = find_char(maze, "S")
    er, ec = find_char(maze, "E")
    pq = [(0, sr, sc, 1)]
    seen = set()
    while pq:
        cost, r, c, d = heapq.heappop(pq)
        if (r, c) == (er, ec):
            return cost
        if (r, c, d) in seen:
            continue
        seen.add((r, c, d))
        dr, dc = DIRECTIONS[d]
        if maze[r + dr][c + dc] != "#":
            heapq.heappush(pq, (cost + 1, r + dr, c + dc, d))
        heapq.heappush(pq, (cost + 1000, r, c, (d + 1) % 4))
        heapq.heappush(pq, (cost + 1000, r, c, (d - 1) % 4))


def part2(maze):
    sr, sc = find_char(maze, "S")
    er, ec = find_char(maze, "E")
    start = (sr, sc, 1)
    dist = {start: 0}
    parents = {start: set()}
    pq = [(0, start)]
    while pq:
        cost, state = heapq.heappop(pq)
        if cost > dist[state]:
            continue
        r, c, d = state
        dr, dc = DIRECTIONS[d]
        neighbors = [
            ((r, c, (d + 1) % 4), 1000),
            ((r, c, (d - 1) % 4), 1000),
        ]
        if maze[r + dr][c + dc] != "#":
            neighbors.append(((r + dr, c + dc, d), 1))
        for ns, edge_cost in neighbors:
            nc = cost + edge_cost
            existing = dist.get(ns, float("inf"))
            if nc < existing:
                dist[ns] = nc
                parents[ns] = {state}
                heapq.heappush(pq, (nc, ns))
            elif nc == existing:
                parents[ns].add(state)

    best = min(dist.get((er, ec, d), float("inf")) for d in range(4))
    on_path = set()
    queue = [
        (er, ec, d) for d in range(4) if dist.get((er, ec, d), float("inf")) == best
    ]
    visited = set(queue)
    while queue:
        state = queue.pop()
        on_path.add(state[:2])
        for p in parents[state]:
            if p not in visited:
                visited.add(p)
                queue.append(p)
    return len(on_path)


maze = take_input()
print(part1(maze))
print(part2(maze))
