data = []
current_position = ()
current_direction = (-1, 0)

with open("input.txt") as f:
    for line in f:
        if line == "\n":
            continue
        data.append(line.strip())

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "^":
            current_position = (i, j)


def simulate_path(data, current_position, current_direction):
    count = 1
    while True:
        if (
            current_position[0] < 0
            or current_position[0] >= len(data)
            or current_position[1] < 0
            or current_position[1] >= len(data[0])
        ):
            break

        if data[current_position[0]][current_position[1]] == "#":
            current_position = (
                current_position[0] - current_direction[0],
                current_position[1] - current_direction[1],
            )
            current_direction = (current_direction[1], -current_direction[0])

        if data[current_position[0]][current_position[1]] == ".":
            data[current_position[0]] = (
                data[current_position[0]][: current_position[1]]
                + ","
                + data[current_position[0]][current_position[1] + 1 :]
            )
            count += 1

        current_position = (
            current_position[0] + current_direction[0],
            current_position[1] + current_direction[1],
        )

    print(count)


# simulate_path(data, current_position, current_direction)


def simulate_guard_loop(data, current_position, current_direction):
    visited_states = set()
    while True:
        if (
            current_position[0] < 0
            or current_position[0] >= len(data)
            or current_position[1] < 0
            or current_position[1] >= len(data[0])
        ):
            return False

        if (current_position, current_direction) in visited_states:
            return True

        visited_states.add((current_position, current_direction))

        if data[current_position[0]][current_position[1]] == "#":
            current_position = (
                current_position[0] - current_direction[0],
                current_position[1] - current_direction[1],
            )
            current_direction = (current_direction[1], -current_direction[0])

        current_position = (
            current_position[0] + current_direction[0],
            current_position[1] + current_direction[1],
        )


count = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "^":
            continue
        if data[i][j] == "#":
            continue
        if data[i][j] == ".":
            data[i] = data[i][:j] + "#" + data[i][j + 1 :]
            is_loop = simulate_guard_loop(data, current_position, current_direction)
            if is_loop:
                count += 1
            data[i] = data[i][:j] + "." + data[i][j + 1 :]

print(count)
