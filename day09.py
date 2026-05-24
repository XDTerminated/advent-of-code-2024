data = ""
with open("input.txt", "r") as file:
    data = file.read().strip()


disk = []
id = 0
for i in range(len(data)):
    if i % 2 == 0:
        tmp = [id] * int(data[i])
        disk.append(tmp)
        id += 1
    else:
        tmp = ["."] * int(data[i])
        disk.append(tmp)


disk = [j for i in disk for j in i]
ptr_start = 0
ptr_end = len(disk) - 1

while ptr_start < ptr_end:
    if disk[ptr_start] == ".":
        if disk[ptr_end] == ".":
            ptr_end -= 1
        else:
            disk[ptr_start] = disk[ptr_end]
            disk[ptr_end] = "."
    else:
        ptr_start += 1

checksum = 0
for i in range(len(disk)):
    if disk[i] == ".":
        break
    checksum += disk[i] * i

print(checksum)

disk = []
id = 0
for i in range(len(data)):
    if i % 2 == 0:
        tmp = [id] * int(data[i])
        disk.append(tmp)
        id += 1
    else:
        tmp = ["."] * int(data[i])
        disk.append(tmp)

l_files = []
for i in range(len(disk)):
    if "." in disk[i] or len(disk[i]) == 0:
        continue
    l_files.append(disk[i])

l_files = l_files[::-1]

for i in range(len(l_files)):
    length = len(l_files[i])
    cur_index = disk.index(l_files[i])
    for j in range(0, cur_index):
        if disk[j] and disk[j][0] == "." and len(disk[j]) >= length:
            leftover = disk[j][length:]
            disk = (
                disk[:j]
                + [l_files[i]]
                + ([leftover] if leftover else [])
                + disk[j + 1 :]
            )
            for k in range(len(disk) - 1, j, -1):
                if disk[k] == l_files[i]:
                    disk[k] = ["." for _ in range(length)]
                    break
            break

flatten = [j for i in disk for j in i]
checksum = 0
for i in range(len(flatten)):
    if flatten[i] == ".":
        continue
    checksum += flatten[i] * i

print(checksum)
