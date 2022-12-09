
moves = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

positions = [(0,0) for x in range(10)]

base_moves = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
}

def add_pos(pos, v):
    return (pos[0] + v[0], pos[1] + v[1])

def manhatan_dist(pos1, pos2):
    return abs(pos1[0]-pos2[0]) + abs(pos1[1] - pos2[1])

def get_new_pos(pos1, pos2):
    x1,y1 = pos1
    x2,y2 = pos2

    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) < 2 and abs(dy) < 2:
        return pos1

    min_dist = 1000
    final_pos = pos1
    for move in moves:
        new_pos = add_pos(pos1, move)
        dist = manhatan_dist(new_pos, pos2)
        if  dist < min_dist:
            min_dist = dist
            final_pos = new_pos
    return final_pos
                

S = set()
S.add((0,0))

with open('input.txt') as f:
    for line in f:
        direction, n = line.split()
        n = int(n)
        for i in range(n):
            positions[0] = add_pos(positions[0], base_moves[direction])
            
            for tail in range(1,10): 
                positions[tail] = get_new_pos(positions[tail], positions[tail-1])
            S.add(positions[9])
print(len(S))
