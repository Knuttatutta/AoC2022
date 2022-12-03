
# Part 1
_sum = 0
with open('input.txt') as fp:
    for line in fp:
        line = line.strip()
        half = int(len(line) / 2)
        _1 = line[:half]
        _2 = line[half:]

        item = [val for val in _1 if val in _2][0]

        if not item:
            continue

        pts = ord(item.lower()) - 96
        if item.isupper():
            pts += 26

        _sum += pts

print(_sum)

# Part 2
_sum = 0
with open('input.txt') as fp:
    lines = fp.readlines()
    for i in range(int(len(lines)/3)):
        group = [line.strip() for line in lines[i*3:i*3+3]]

        item = [val for val in group[0] if val in group[1] and val in group[2]][0]

        pts = ord(item.lower()) - 96
        if item.isupper():
            pts += 26

        _sum += pts

print(_sum)

