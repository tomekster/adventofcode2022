def overlaps(a,b,x,y):
    return (a >= x and a <= y) or (b >= x and b <= y) or (a<x and b >y)

S=0
with open('input.txt') as f:
    for line in f:
        s1, s2 = line.split(',')
        x, y = s1.split('-')
        a, b = s2.split('-')
        x, y, a, b = [int(tmp) for tmp in [x, y, a, b]]  # cast all four variables to int
        if overlaps(a,b,x,y):
            S+=1
print(S)
