
N=99
grid = []
see = [ [1 for x in range(N)] for y in range(N)]

def check_vis_left():
    for i in range(N):
        for j in range(N):
            print(i, j)
            cnt = 0
            while j - cnt - 1 >= 0 and grid[i][j - cnt - 1] < grid[i][j]:
                cnt += 1
            if j - cnt - 1 >= 0:
                cnt += 1
            see[i][j] *= cnt

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


for i in range(4):
    print(i)
    print('check vis')
    check_vis_left()
    print('rot')
    grid = rot(grid)
    see = rot(see)

print("SEE", len(see), len(see[0]))

#for i in range(N):
#    print(''.join(see[i]))

res = 0
for i in range(N):
    for j in range(N):
        if(see[i][j] > res):
            res = see[i][j]
print(res)
