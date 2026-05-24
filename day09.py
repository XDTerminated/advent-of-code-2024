def take_input():
    return input()


def expand(disk_map):
    disk = []
    for i, n in enumerate(disk_map):
        disk.extend([i // 2 if i % 2 == 0 else None] * int(n))
    return disk


def checksum(disk):
    return sum(i * x for i, x in enumerate(disk) if x is not None)


def part1(disk_map):
    disk = expand(disk_map)
    left, right = 0, len(disk) - 1
    while left < right:
        if disk[left] is not None:
            left += 1
        elif disk[right] is None:
            right -= 1
        else:
            disk[left], disk[right] = disk[right], disk[left]
            left += 1
            right -= 1
    return checksum(disk)


def part2(disk_map):
    segments = [
        [i // 2 if i % 2 == 0 else None, int(n)] for i, n in enumerate(disk_map)
    ]
    file_ids = sorted({s[0] for s in segments if s[0] is not None}, reverse=True)

    for fid in file_ids:
        fpos = next(i for i, s in enumerate(segments) if s[0] == fid)
        flen = segments[fpos][1]
        for gpos in range(fpos):
            if segments[gpos][0] is None and segments[gpos][1] >= flen:
                gap_len = segments[gpos][1]
                segments[fpos] = [None, flen]
                segments[gpos] = [fid, flen]
                if gap_len > flen:
                    segments.insert(gpos + 1, [None, gap_len - flen])
                break

    pos, total = 0, 0
    for seg_id, length in segments:
        if seg_id is not None:
            total += seg_id * sum(range(pos, pos + length))
        pos += length
    return total


disk_map = take_input()
print(part1(disk_map))
print(part2(disk_map))
