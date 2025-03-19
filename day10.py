data = []
with open("input.txt") as f:
    for line in f:
        data.append(list(str(line.strip())))


def get_trailhead_score(data, pos_x, pos_y, visited):
    if data[pos_x][pos_y] == "9":
        visited.append((pos_x, pos_y))
        return visited

    if pos_x - 1 >= 0:
        if data[pos_x - 1][pos_y] == str(int(data[pos_x][pos_y]) + 1):
            visited = get_trailhead_score(data, pos_x - 1, pos_y, visited)

    if pos_x + 1 < len(data):
        if data[pos_x + 1][pos_y] == str(int(data[pos_x][pos_y]) + 1):
            visited = get_trailhead_score(data, pos_x + 1, pos_y, visited)

    if pos_y - 1 >= 0:
        if data[pos_x][pos_y - 1] == str(int(data[pos_x][pos_y]) + 1):
            visited = get_trailhead_score(data, pos_x, pos_y - 1, visited)

    if pos_y + 1 < len(data[pos_x]):
        if data[pos_x][pos_y + 1] == str(int(data[pos_x][pos_y]) + 1):
            visited = get_trailhead_score(data, pos_x, pos_y + 1, visited)
    return visited


trailhead_score = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "0":
            trailhead_score += len(set(get_trailhead_score(data, i, j, [])))

print(trailhead_score)

rating = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "0":
            rating += len(get_trailhead_score(data, i, j, []))

print(rating)
