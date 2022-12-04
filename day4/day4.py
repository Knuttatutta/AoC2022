
# Parts 1 and 2
with open('input.txt') as fp:
    lines = fp.readlines()

redundant_elves = 0
overlap = 0
for line in lines:
    elves = line.strip().split(',')
    elf1 = elves[0].split('-')
    elf2 = elves[1].split('-')

    ids1 = list(range(int(elf1[0]), int(elf1[1])+1))
    ids2 = list(range(int(elf2[0]), int(elf2[1])+1))

    if all(_id in ids2 for _id in ids1) or all(_id in ids1 for _id in ids2):
        redundant_elves += 1

    if any(_id in ids2 for _id in ids1) or any(_id in ids1 for _id in ids2):
        overlap += 1

print(redundant_elves)
print(overlap)
