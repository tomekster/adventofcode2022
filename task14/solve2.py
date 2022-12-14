S = set()

BOTTOM = 0

def drop():
    x=500
    y=0
    
    while True:
        if y == BOTTOM -1:
            S.add((x,y))
            return True
        if (x, y+1) not in S:
            y = y+1
        elif (x-1, y+1) not in S:
            x = x-1
            y = y+1
        elif (x+1, y+1) not in S:
            x = x+1
            y = y+1
        else:
            S.add((x,y))
            if x == 500 and y == 0:
                return False
            return True


with open('example.txt') as f:
    for line in f:
        points = line.strip().split()
        print(points)
        for i in range(len(points) -1):
            x1,y1 = points[i].split(',')
            x2,y2 = points[i+1].split(',')

            x1, y1, x2, y2 = [int(x) for x in [x1, y1, x2, y2]]

            print(x1,y1,'->', x2,y2)

            x1, x2 = min(x1, x2), max(x1,x2)
            y1, y2 = min(y1, y2), max(y1,y2)
            
            BOTTOM = max(BOTTOM, y2)

            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    S.add((x,y))

BOTTOM = BOTTOM + 2

cnt = 0 
while drop():
    cnt += 1

print(cnt)
