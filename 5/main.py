# this is slow but it works.
with open("input.txt") as f:
    dat = f.readline()

def reduce(inp):
    prev_len = len(inp)
    cur_len = 0
    while prev_len > cur_len:
        prev_len = len(inp)
        i = 0
        while i < len(inp)-1:
            if inp[i].isupper() and inp[i].lower() == inp[i+1]\
                    or inp[i].islower() and inp[i].upper() == inp[i+1]:
                inp = inp[:i] + inp[i+2:]
            else:
                i += 1
        cur_len = len(inp)

    return len(inp)


print("1:", reduce(dat))


alphabet = 'abcdefghijklmnopqrstuvwxyz'

from copy import deepcopy
min = 9999999999
for i in alphabet:
    inp = deepcopy(dat)
    inp = inp.replace(i,'',50000)
    inp = inp.replace(i.upper(), '', 50000)
    res = reduce(inp)
    if res < min:
        min = res
    # print(i)

print("2:", min)
