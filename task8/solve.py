grid = []
N=99

def check_vis_left():
    for i in range(N):
        M = -1
        for j in range(N):
            if grid[i][j] > M:
                see[i][j] = 'O'
                M = grid[i][j]

def rot(G):
    global N
    tmp = [ ['X' for x in range(N)] for y in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[j][N-1-i] = G[i][j]
    return tmp

with open('input.txt') as f:
    for line in f:
        grid.append( [int(c) for c in line.strip()] )

see = [ ['X' for x in range(N)] for y in range(N)]

for i in range(4):
    print(i)
    print('check vis')
    check_vis_left()
    print('rot')
    grid = rot(grid)
    see = rot(see)

for i in range(N):
    print(''.join(see[i]))

res = 0
for i in range(N):
    for j in range(N):
        if(see[i][j] == 'O'):
            res += 1
print(res)
