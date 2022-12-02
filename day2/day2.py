
opponent_letters = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
me_letters = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
points = {'rock': 1, 'paper': 2, 'scissors': 3}

rules = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

pts = 0

# Part 1
with open('input.txt') as fp:
    for line in fp.readlines():
        letters = line.strip().split(' ')
        opponent = opponent_letters[letters[0]]
        me = me_letters[letters[1]]
        pts += points[me]
        if rules[me] == opponent:
            pts += 6
        elif rules[opponent] != me:
            pts += 3

print(pts)

# Part 2
pts = 0
with open('input.txt') as fp:
    for line in fp.readlines():
        letters = line.strip().split(' ')
        opponent = opponent_letters[letters[0]]
        outcome = letters[1]

        if outcome == 'X':
            me = rules[opponent]
        elif outcome == 'Y':
            me = opponent
            pts += 3
        else:
            me = [key for key, val in rules.items() if val == opponent][0]
            pts += 6

        pts += points[me]
        me = me_letters[letters[1]]

print(pts)