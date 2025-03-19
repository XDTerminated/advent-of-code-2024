data = map(int, input().split())
turn = 0
hm = {}

for num in data:
    if num not in hm:
        hm[num] = 1
    else:
        hm[num] += 1

while turn < 75:
    tmp_dict = {}
    for i in list(hm.keys()):
        if hm[i] > 0:
            if i == 0:
                if 1 not in tmp_dict:
                    tmp_dict[1] = hm[i]
                else:
                    tmp_dict[1] += hm[i]
            elif len(str(i)) % 2 == 0:
                left = int(str(i)[: len(str(i)) // 2])
                right = int(str(i)[len(str(i)) // 2 :])

                if left not in tmp_dict:
                    tmp_dict[left] = hm[i]
                else:
                    tmp_dict[left] += hm[i]

                if right not in tmp_dict:
                    tmp_dict[right] = hm[i]
                else:
                    tmp_dict[right] += hm[i]
            else:
                if i * 2024 not in tmp_dict:
                    tmp_dict[i * 2024] = hm[i]
                else:
                    tmp_dict[i * 2024] += hm[i]
        hm[i] = 0

    for i in tmp_dict.keys():
        hm[i] = tmp_dict[i]

    turn += 1

print(sum(hm.values()))
