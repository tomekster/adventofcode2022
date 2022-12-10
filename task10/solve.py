L = [1]
with open('input.txt') as f:
    for line in f:
        L.append(L[-1])
        if line.strip() == 'noop':
            pass
        else:
            _, val = line.strip().split()
            L.append(L[-1] + int(val))

for i, val in enumerate(L):
    print(i, val)


idx = [20,60,100,140,180,220]

s=0
for i in idx:
    print(i, L[i-1])
    s += i * L[i-1]
print(s)
