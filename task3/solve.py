s = 0
with open('input.txt') as f:
    for line in f:
        l = int(len(line.strip())/2)
        print(l)
        p1 = set(line[0:l])
        p2 = line[l:]
        for c in p2:
            if c in p1:
                if(ord(c) < 91):
                    s += ord(c) - ord('A') + 27
                else:
                    s += ord(c) - ord('a') + 1
                break
    print(s)
