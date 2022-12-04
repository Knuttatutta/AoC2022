
# Part 1
_max = 0
_sum = 0
with open('input.txt') as fp:
    for line in fp.readlines():
        line = line.strip()
        if not line:
            _sum = 0
            continue
        _sum += int(line)
        _max = max(_sum, _max)


print(_max)

# Part 2
elves = []

_sum = 0
with open('input.txt') as fp:
    for line in fp.readlines():
        line = line.strip()
        if not line:
            elves.append(_sum)
            _sum = 0
            continue
        _sum += int(line)

elves = sorted(elves)

print(sum(elves[-3:]))
