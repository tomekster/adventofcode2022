def contains(a,b,x,y):
    return a<=x and b>=y

def any_contains(a,b,x,y):
    return contains(a,b,x,y) or contains(x,y,a,b)

S=0
with open('input.txt') as f:
    for line in f:
        s1, s2 = line.split(',')
        x, y = s1.split('-')
        a, b = s2.split('-')
        x, y, a, b = [int(tmp) for tmp in [x, y, a, b]]  # cast all four variables to int
        if any_contains(x,y,a,b):
            S+=1
print(S)
