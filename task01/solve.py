with open('input.txt') as f:
    elves = []
    s = 0
    for line in f:
        if line == '\n':
            elves.append(s)
            s = 0
        else:
            s = s + int(line)
    elves.append(s)
    print(max(elves))
    print(elves[2])


