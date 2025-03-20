button_a = []
button_b = []
prizes = []

with open("input.txt") as file:
    for line in file:
        line = line.strip()
        if line.startswith("Button A:"):
            x, y = map(int, line.split("X+")[1].split(", Y+"))
            button_a.append((x, y))
        elif line.startswith("Button B:"):
            x, y = map(int, line.split("X+")[1].split(", Y+"))
            button_b.append((x, y))
        elif line.startswith("Prize:"):
            x, y = map(int, line.split("X=")[1].split(", Y="))
            prizes.append((x, y))

tokens = 0

for i in range(len(button_a)):
    matrix = [
        [button_a[i][0], button_a[i][1]],
        [button_b[i][0], button_b[i][1]],
        [prizes[i][0] + 10000000000000, prizes[i][1] + 10000000000000],
    ]

    det_matrix = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det_x = matrix[2][0] * matrix[1][1] - matrix[2][1] * matrix[1][0]
    det_y = matrix[0][0] * matrix[2][1] - matrix[0][1] * matrix[2][0]

    x = det_x / det_matrix
    y = det_y / det_matrix

    if int(x) == x and int(y) == y and x >= 0 and y >= 0:
        tokens += int(x) * 3 + int(y)


print(tokens)
