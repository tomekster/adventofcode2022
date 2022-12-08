def unique(s):
    S = set(s)
    return len(S) == len(s)


with open('input.txt') as f:
    for line in f:
        for i in range(3, len(line)):
            if(unique(line[i-3:i+1])):
                print(i+1)
                break
