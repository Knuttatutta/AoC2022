
with open('input.txt') as fp:
    lines = fp.readlines()

stack_index = None
crate_indices = []

for i, line in enumerate(lines):
    if line.strip(' ')[0].isnumeric():
        stack_index = i
        for j, index in enumerate(line):
            if index.isnumeric():
                crate_indices.append(j)
        break

crates_list = lines[:stack_index]
crates_num = lines[stack_index]
moves = lines[stack_index+2:]

crates = {i: [] for i in crates_num if i.isnumeric()}
for i, line in enumerate(reversed(crates_list)):
    for j in crate_indices:
        if len(line) > j and line[j] != ' ':
            crates[crates_num[j]].append(line[j])

for move in moves:
    move_split = move.split(' ')
    num = int(move_split[1])
    old_stack = move_split[3]
    new_stack = move_split[-1].strip()

    start_ind = len(crates[old_stack]) - num
    crates_to_move = crates[old_stack][start_ind:]
    del crates[old_stack][start_ind:]
    # crates[new_stack].extend(reversed(crates_to_move)) # Part 1
    crates[new_stack].extend(crates_to_move) # Part 2

message = ''
for val in crates.values():
    message += val[-1]

print(message)
