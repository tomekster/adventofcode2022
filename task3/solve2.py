import string

letters = string.ascii_lowercase + string.ascii_uppercase
s = 0
with open('input.txt') as f:
    c = 1
    lines = []
    for line in f:
        lines.append(line.strip())
        if c % 3 == 0:
            print(lines)
            for x in letters:
                if x in lines[0] and x in lines[1] and x in lines[2]:
                    if(ord(x) < 91):
                        s += ord(x) - ord('A') + 27
                    else:
                        s += ord(x) - ord('a') + 1
                    break
            c = 0
            lines = []
        c += 1
print(s) 
