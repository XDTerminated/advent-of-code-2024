with open("input.txt") as f:
    data = f.readlines()

data = [x.strip() for x in data]


def get_xmas(data):

    rows, cols = len(data), len(data[0])
    count = 0

    def check_direction(x, y, dx, dy):
        if not (0 <= x + 3 * dx < rows and 0 <= y + 3 * dy < cols):
            return False
        return "".join(data[x + i * dx][y + i * dy] for i in range(4)) == "XMAS"

    directions_to_check = [
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
    ]

    for i in range(rows):
        for j in range(cols):
            if data[i][j] == "X":
                for dx, dy in directions_to_check:
                    if check_direction(i, j, dx, dy):
                        count += 1

    return count


print(get_xmas(data))


def get_x_mas(data):
    rows, cols = len(data), len(data[0])
    count = 0

    valid_mas = ["MAS", "SAM"]

    def get_diagonal(x, y, dx, dy):
        if not (
            0 <= x - dx < rows
            and 0 <= x + dx < rows
            and 0 <= y - dy < cols
            and 0 <= y + dy < cols
        ):
            return None

        return data[x - dx][y - dy] + data[x][y] + data[x + dx][y + dy]

    for i in range(rows):
        for j in range(cols):
            if data[i][j] != "A":
                continue

            diag1 = get_diagonal(i, j, 1, 1)
            diag2 = get_diagonal(i, j, 1, -1)

            if not diag1 and not diag2:
                continue

            if diag1 in valid_mas and diag2 in valid_mas:
                count += 1

    return count


print(get_x_mas(data))
