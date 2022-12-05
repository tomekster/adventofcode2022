#                [B] [L]     [J]    
#            [B] [Q] [R]     [D] [T]
#            [G] [H] [H] [M] [N] [F]
#        [J] [N] [D] [F] [J] [H] [B]
#    [Q] [F] [W] [S] [V] [N] [F] [N]
#[W] [N] [H] [M] [L] [B] [R] [T] [Q]
#[L] [T] [C] [R] [R] [J] [W] [Z] [L]
#[S] [J] [S] [T] [T] [M] [D] [B] [H]
# 1   2   3   4   5   6   7   8   9 


stacks = [
    [],
    ['S','L','W'],
    ['J','T','N','Q'],
    ['S','C','H','F','J'],
    ['T','R','M','W','N','G','B'],
    ['T','R','L','S','D','H','Q','B'],
    ['M','J','B','V','F','H','R','L'],
    ['D','W','R','N','J','M'],
    ['B','Z','T','F','H','N','D','J'],
    ['H','L','Q','N','B','F','T']
]

with open('input.txt') as f:
    for line in f:
        n, src, dest = [int(x) for x in line.split()]
        for x in range(n):
            a = stacks[src].pop()
            stacks[dest].append(a)
    for stack in stacks:
        print(stack)

