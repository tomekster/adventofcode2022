score = [
    [3, 6, 0],
    [0, 3, 6],
    [6, 0, 3]
]

score2 = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
]

my_move = [
    ['C', 'A', 'B'],
    ['A', 'B', 'C'],
    ['B', 'C', 'A']
]


def replace(s):
    if s == 'X' or s == 'A':
        return 0
    elif s == 'Y' or s == 'B':
        return 1
    elif s == 'Z' or s == 'C':
        return 2


total = 0
with open("input.txt") as f:
    for line in f:
        him, me = line.split()
        x, y = replace(him), replace(me)
        y = my_move[x][y]
        y = replace(y)
        total += score[x][y]
        total += score2[x][y]


print(total)
