

def cd(_dir):
    global current_dir
    global current_dir_contents

    if _dir == '/':
        pass
    elif _dir == '..':
        current_dir = current_path[-2]
        current_path.pop()

        curr_dict = files
        for path in current_path:
            curr_dict = curr_dict[path]
        current_dir_contents = curr_dict

    else:
        current_path.append(_dir)
        current_dir = _dir
        current_dir_contents = current_dir_contents[current_dir]


def ls(*args):
    global current_dir

    contents = {}
    line = None
    dir_files_size = 0
    while (next_line := next(lines, 0)) and (line := next_line.strip())[0] != '$':
        if line.startswith('dir'):
            contents[line.split(' ')[-1]] = dict()
        else:
            size, name = line.split(' ')
            contents[name] = size
            dir_files_size += int(size)

    global all_dir_sizes
    all_dir_sizes[current_dir] = dir_files_size

    contents['size'] = dir_files_size
    current_dir_contents.update(contents)

    # Also add size to parent folders
    curr_dict = files
    curr_dict['size'] += dir_files_size
    for path in current_path:
        curr_dict['size'] += dir_files_size
        all_dir_sizes[path] = curr_dict['size']
        curr_dict = curr_dict[path]

    if next_line == 0:
        line = None

    return line


def execute_line(line):
    line_lst = line.strip().split(' ')
    cmd = line_lst[1]
    arg = line_lst[2] if len(line_lst) > 2 else None

    line = globals()[cmd](arg)

    if line is not None and cmd == 'ls':
        execute_line(line)


files = {'/': dict(), 'size': 0}
current_dir = '/'
current_dir_contents = files[current_dir]
current_path = ['/']
all_dir_sizes = dict()

with open('input.txt') as fp:
    lines = iter(fp.readlines())

while line := next(lines, 0):
    execute_line(line)


def traverse_dict(dct):
    global _sum
    global min_dir
    global size_needed_to_delete

    if isinstance(dct, dict):
        for key, val in dct.items():
            if isinstance(val, dict):
                traverse_dict(val)
            elif key == 'size':
                if val < 100000:
                    _sum += val
                if size_needed_to_delete < val < min_dir:
                    min_dir = val


size_needed_to_delete = 30000000 - (70000000 - files['/']['size'])

_sum = 0 # For part 1
min_dir = 1E9 # For part 2
traverse_dict(files)
print(_sum)
print(min_dir)


exit()