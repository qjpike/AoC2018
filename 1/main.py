with open("input.tt") as f:
    inp = f.readlines()

sum = 0
prev_sums = set()

for i in inp:
    sum += int(i.strip())

print("1: " + str(sum))

sum = 0

while True:
    for i in inp:
        sum += int(i.strip())
        if sum in prev_sums:
            print("2: " + str(sum))
            exit()
        prev_sums.add(sum)