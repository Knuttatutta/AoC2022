
with open('input.txt') as fp:
    buffer = fp.readlines()[0]

# n_chars = 4   # Part 1
n_chars = 14  # Part 2

for i in range(n_chars - 1, len(buffer)):
    if len(set(buffer[i - n_chars + 1:i + 1])) == n_chars:
        print(i+1)
        break
