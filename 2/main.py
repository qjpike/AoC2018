inp = []
with open("input.txt") as f:
    for i in f.readlines():
        inp.append(i.strip())

twos = 0
threes = 0


for i in inp:
    dat = dict()
    for ch in i:
        if ch not in dat:
            dat[ch] = 1
        else:
            dat[ch] += 1

    if 2 in dat.values():
        twos += 1
    if 3 in dat.values():
        threes += 1



print("1: " + str(twos*threes))

for z, i in enumerate(inp):

    for j in inp[z+1:]:
        count = 0
        idx = -1
        for k, ch in enumerate(j):
            if i[k] != ch:
                count += 1
                idx = k
                if count > 1:
                    break

        if count == 1:
            print("2: " + i[:idx] + i[idx+1:])
            exit()