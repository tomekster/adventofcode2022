grid = []
moves = [(1,0), (0,1), (-1,0), (0,-1)] 
#with open('example.txt') as f:
with open('input.txt') as f:
    for line in f:
        grid.append(line.strip())

X = len(grid)
Y = len(grid[0])

dist = []
for i in range(X):
    dist.append([-1 for j in range(Y)])

tx, ty = -1, -1

for i in range(X):
    for j in range(Y):
        if(grid[i][j] == 'S' or grid[i][j] == 'a'):
            dist[i][j] = 0
            grid[i] = grid[i].replace('S', 'a')
            print("S:", i, j)
        elif(grid[i][j] == 'E'):
            tx, ty = i, j
            grid[i] = grid[i].replace('E', 'z')
            print("E:", i, j)

print(grid[tx][ty])

print(X * Y)
cnt = 0


def print_dist():
    for l in dist:
        string = [str(x) if x < 0 or x > 9 else ' ' + str(x) for x in l]
        print(' '.join(string))


update = True

while update and cnt < 6000:
    update = False
    cnt += 1
    print(cnt)
    #print_dist()
    for i in range(X):
        for j in range(Y):
            if dist[i][j] != -1:
                for move in moves:
                    dx, dy = move
                    x = i + dx
                    y = j + dy
                    if x >= 0 and y >= 0 and x < X and y < Y and ord(grid[x][y]) <= ord(grid[i][j]) + 1:
                        if dist[x][y] == -1:
                            dist[x][y] = dist[i][j] + 1
                            update = True
                        else:
                            if dist[x][y] > dist[i][j] + 1:
                                update = True
                            dist[x][y] = min(dist[x][y], dist[i][j] + 1)

print(dist[tx][ty])

