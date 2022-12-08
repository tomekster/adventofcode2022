def unique(s):
    S = set(s)
    return len(S) == len(s)


with open('input.txt') as f:
    for line in f:
        for i in range(13, len(line)):
            if(unique(line[i-13:i+1])):
                print(i+1)
                break
