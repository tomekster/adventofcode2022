items = []
ops = []
div = []
iftrue = []
iffalse = []
args = []

NUM_MONKEYS = 8

with open("input.txt") as f:

    for monkey in range(NUM_MONKEYS):
        items.append([int(x) for x in f.readline().strip().split()])
        op, arg = f.readline().strip().split()
        args.append(int(arg))
        #print(op, arg)
        if op == '+':
            ops.append(lambda x: x+args[monkey])
        elif op == '*':
            ops.append(lambda x: x*args[monkey])
        elif op == '^':
            ops.append(lambda x: x**args[monkey])
        
        #print(ops[-1](1))

        div.append(int(f.readline().strip()))
        
        iftrue.append(int(f.readline().strip()))
        iffalse.append(int(f.readline().strip()))

res = [0 for _ in range(NUM_MONKEYS)]

MOD = 1
for x in div:
    MOD *= x

for rnd in range(10000):
    #print(rnd)
    #print("#######")
    #for monkey in range(NUM_MONKEYS):
        #print(items[monkey])

    for monkey in range(NUM_MONKEYS):
        for item in items[monkey]:
            res[monkey] += 1 
            val_op = ops[monkey](item)
            #print(ops[monkey](1), ops[monkey](2))
            val = val_op % MOD
            if val % div[monkey] == 0:
                target = iftrue[monkey]
                items[target].append(val)
                #print("Item {} after operation: {}, divided by 3: {} is divisible by {} -> throw to monkey {}".format(item, val_op, val, div[monkey], target)) 
            else:
                target = iffalse[monkey]
                items[target].append(val)
                #print("Item {} after operation: {}, divided by 3: {} is NOT divisible by {} -> throw to monkey {}".format(item, val_op, val, div[monkey], target)) 
        items[monkey] = []

print(res)
