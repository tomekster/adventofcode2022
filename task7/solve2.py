def is_command(line):
    return line[0] == '$'


def is_cd(line):
    return line[2:4] == 'cd'


def cd_get_dir(line):
    return line.split()[-1]


def is_ls(line):
    return line[2:4] == 'ls'


G = {'@/':[]}
parent = {}
size = {'@/': -1}
CUR_DIR = '@/'
listing = False
children = []

dir_sizes = {}


def dfs(cur='@/', depth=0):
    #print(depth)
    if cur not in G:
        return size[cur]

    s = 0
    for c in G[cur]:
        inc = dfs(c, depth+1)
        #print(cur, c, inc)
        s += inc
    dir_sizes[cur] = s
    return s



lines = []

with open('input.txt') as f:
    lines = [line.strip() for line in f]
      
for i, line in enumerate(lines):
    if is_command(line):
        if listing:
            #print('listing of ' + CUR_DIR)
            G[CUR_DIR] = children
            for c in children:
                parent[c] = CUR_DIR
            children = []
            listing = False

        if is_cd(line):
            directory = cd_get_dir(line)
            #print('cd into ' + directory)
            if directory == '..':
                CUR_DIR = '@'.join(CUR_DIR.split('@')[:-1])
            else:
                parent[directory] = CUR_DIR
                CUR_DIR = CUR_DIR + '@' + directory

        elif is_ls(line):
            listing = True
            children = []

    elif listing:
        x, y = line.split()
        path = CUR_DIR + '@' + y
        if x == 'dir':
            pass
            #size[path] = -1
        else:
            size[path] = int(x)
        #print("add to listing: " + y)
        children.append(path)

if listing and children:
    G[CUR_DIR] = children
    for c in children:
        parent[c] = CUR_DIR
print(G)

dfs()

res = 0
candidates_to_delete = []
for k in dir_sizes:
    if dir_sizes[k] >= 4376732:
        print(k, dir_sizes[k])
        candidates_to_delete.append((dir_sizes[k], k))
        res += dir_sizes[k]
candidates_to_delete.sort()
print(candidates_to_delete)
