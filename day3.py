import re

multsum = 0

with open("input.txt", "r") as file:
    data = file.readlines()

for i in range(len(data)):
    data[i] = data[i].strip()
    a = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", data[i])

    for j in a:
        b = j.split("(")[1].split(")")[0].split(",")
        multsum += int(b[0]) * int(b[1])

print(multsum)

multsum = 0

mult = True

for i in range(len(data)):
    data[i] = data[i].strip()
    a = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)", data[i])

    for j in a:
        if j == "do()":
            mult = True

        elif j == "don't()":
            mult = False

        elif mult:
            b = j.split("(")[1].split(")")[0].split(",")
            multsum += int(b[0]) * int(b[1])

print(multsum)
