data = []
antinodes = set()

with open("input.txt") as f:
    for line in f:
        data.append(line.strip())

d = {}

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == ".":
            continue
        elif data[i][j] not in d.keys():
            d[data[i][j]] = [(i, j)]
        else:
            d[data[i][j]].append((i, j))

for key in d.keys():
    for i in range(len(d[key])):
        for j in range(len(d[key])):
            if i == j:
                continue
            dist_x = d[key][i][0] - d[key][j][0]
            dist_y = d[key][i][1] - d[key][j][1]

            ant = (dist_x + d[key][i][0], dist_y + d[key][i][1])
            ant2 = (d[key][j][0] - dist_x, d[key][j][1] - dist_y)

            if not (
                ant[0] < 0
                or ant[0] >= len(data)
                or ant[1] < 0
                or ant[1] >= len(data[0])
            ):
                antinodes.add(ant)
            if not (
                ant2[0] < 0
                or ant2[0] >= len(data)
                or ant2[1] < 0
                or ant2[1] >= len(data[0])
            ):
                antinodes.add(ant2)

print(len(antinodes))

for key in d.keys():
    for i in range(len(d[key])):
        for j in range(len(d[key])):
            if i == j:
                continue
            dist_x = d[key][i][0] - d[key][j][0]
            dist_y = d[key][i][1] - d[key][j][1]

            count = 0

            while True:
                ant = ((count * dist_x) + d[key][i][0], (count * dist_y) + d[key][i][1])
                if not (
                    ant[0] < 0
                    or ant[0] >= len(data)
                    or ant[1] < 0
                    or ant[1] >= len(data[0])
                ):
                    antinodes.add(ant)
                    count += 1
                else:
                    break

            count = 0
            while True:
                ant2 = (
                    d[key][j][0] - (count * dist_x),
                    d[key][j][1] - (count * dist_y),
                )
                if not (
                    ant2[0] < 0
                    or ant2[0] >= len(data)
                    or ant2[1] < 0
                    or ant2[1] >= len(data[0])
                ):
                    antinodes.add(ant2)
                    count += 1
                else:
                    break

print(len(antinodes))
