import ast
import functools


def cmp(a, b):
    return -compare(a, b)


def compare(a, b):
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


lines = []


with open('input2.txt') as f:
    for line in f:
        l = line.strip()
        if l == '':
            continue
        lines.append(l)

lines = [ast.literal_eval(x) for x in lines]

# lines.sort(cmp=compare)
lines = sorted(lines, key=functools.cmp_to_key(cmp))
for line in lines:
    print(line)

