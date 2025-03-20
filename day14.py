current_position = []
velocity = []

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        parts = line.split()
        p = list(map(int, parts[0][2:].split(",")))
        v = list(map(int, parts[1][2:].split(",")))
        current_position.append(p)
        velocity.append(v)


count = 1
while count < 10000:  # experiment with the number of iterations
    tmp = [["0" for i in range(101)] for j in range(103)]
    for j in range(len(current_position)):
        current_position[j] = [
            (current_position[j][0] + velocity[j][0]) % 101,
            (current_position[j][1] + velocity[j][1]) % 103,
        ]

    for j in range(len(current_position)):
        tmp[current_position[j][1]][current_position[j][0]] = "1"

    for j in range(len(tmp)):
        if "111111" in "".join(tmp[j]):  # experiment with the numbers of 1s in a row.
            print(count)  # answer is the one that has the most number of occurences

    count += 1


quad_1 = 0
quad_2 = 0
quad_3 = 0
quad_4 = 0
for i in range(len(current_position)):

    if current_position[i][0] < 50 and current_position[i][1] < 51:
        quad_1 += 1
    if current_position[i][0] > 50 and current_position[i][1] < 51:
        quad_2 += 1
    if current_position[i][0] < 50 and current_position[i][1] > 51:
        quad_3 += 1
    if current_position[i][0] > 50 and current_position[i][1] > 51:
        quad_4 += 1

print(quad_1 * quad_2 * quad_3 * quad_4)
