import ast


def compare(a, b):
    print(a,b)
    #print(a,b)
    if type(a) == int and type(b) == int:
        if a < b:
            return 1
        elif a == b:
            return 0
        elif a > b:
            return -1

    if type(a) == list and type(b) == int:
        #b = [b for x in a]
        b = [b]

    if type(a) == int and type(b) == list:
        #a = [a for x in b]
        a = [a]
 
    if type(a) == list and type(b) == list:
        for i, x in enumerate(a):
            if i >= len(b):
                return -1
            res = compare(x, b[i])
            if res == 1:
                return 1
            elif res == 0:
                continue
            elif res == -1:
                return -1
        if len(a) < len(b):
            return 1


cnt = 0
correct = []

lines = []

with open('input.txt') as f:
    for line in f:
        l = line.strip()
        if l == '':
            continue
        lines.append(l)

def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return zip(a, a)

res = 0

for l1, l2 in pairwise(lines):
    cnt += 1
    l1 = ast.literal_eval(l1)
    l2 = ast.literal_eval(l2)

    print(cnt, l1, l2)

    if compare(l1, l2) == 1:
        correct.append(cnt)
        res += cnt

print(correct)
print(res)
    

