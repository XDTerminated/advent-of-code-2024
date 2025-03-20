data = list(map(str.strip, open("input.txt").readlines()))
hm_pos = {}

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] not in hm_pos:
            hm_pos[data[i][j]] = [(i, j)]
        else:
            hm_pos[data[i][j]].append((i, j))


def get_all_one_away(coords, pos):
    a = [pos]
    for i in coords:
        if abs(i[0] - pos[0]) + abs(i[1] - pos[1]) == 1:
            a.append(i)

    return a


def get_regions(coords):
    regions = []
    for i in coords:
        regions.append(get_all_one_away(coords, i))

    idx = 0
    while idx < len(regions):
        merged = False
        for i in range(idx + 1, len(regions)):
            if len(set(regions[idx]) & set(regions[i])) > 0:
                regions[idx] = list(set(regions[idx]) | set(regions[i]))
                regions[i] = []
                merged = True

        if not merged:
            idx += 1

    regions = [i for i in regions if len(i) > 0]
    return regions


cost = 0
for i in hm_pos.keys():
    regions = get_regions(hm_pos[i])
    for j in range(len(regions)):
        perimeter = 0
        for k in regions[j]:
            rows, cols = len(data), len(data[0])
            current_value = data[k[0]][k[1]]
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dx, dy in directions:
                nx, ny = k[0] + dx, k[1] + dy

                if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                    perimeter += 1

                elif data[nx][ny] != current_value:
                    perimeter += 1

        cost += len(regions[j]) * perimeter

print(cost)


cost = 0
for letter in hm_pos.keys():
    regions = get_regions(hm_pos[letter])
    for region in regions:
        region_set = set(region)
        corners = 0
        for r, c in region_set:
            in_region = lambda pt: pt in region_set
            if not in_region((r - 1, c)) and not in_region((r, c - 1)):
                corners += 1
            if (
                in_region((r - 1, c))
                and in_region((r, c - 1))
                and not in_region((r - 1, c - 1))
            ):
                corners += 1
            if not in_region((r - 1, c)) and not in_region((r, c + 1)):
                corners += 1
            if (
                in_region((r - 1, c))
                and in_region((r, c + 1))
                and not in_region((r - 1, c + 1))
            ):
                corners += 1
            if not in_region((r + 1, c)) and not in_region((r, c - 1)):
                corners += 1
            if (
                in_region((r + 1, c))
                and in_region((r, c - 1))
                and not in_region((r + 1, c - 1))
            ):
                corners += 1
            if not in_region((r + 1, c)) and not in_region((r, c + 1)):
                corners += 1
            if (
                in_region((r + 1, c))
                and in_region((r, c + 1))
                and not in_region((r + 1, c + 1))
            ):
                corners += 1
        cost += len(region_set) * corners
print(cost)
