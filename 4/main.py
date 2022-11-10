with open("input.txt") as f:
    inp = f.readlines()

inp.sort()

sched = dict()
guard = -1
fell = 0
for i in inp:
    info = i.split()
    if info[2] == "Guard":
        guard = int(info[3][1:])
    elif info[2] == "falls":
        fell = int(info[1].split(":")[1][:-1])
    elif info[2] == "wakes":
        if guard not in sched:
            sched[guard] = dict()
        for j in range(fell, int(info[1].split(":")[1][:-1])):
            if j not in sched[guard]:
                sched[guard][j] = 0

            sched[guard][j] += 1

max = 0
verdict = 0
biggest_min = -1
for g in sched.keys():
    mins_asleep = sum(sched[g].values())
    if mins_asleep > max:
        verdict = g
        max = mins_asleep
        max_min = 0
        for j in sched[g].keys():
            if sched[g][j] > max_min:
                max_min = sched[g][j]
                biggest_min = j


print("1:", verdict * biggest_min)

biggest_min = -1
guard = -1
max_min
for g in sched.keys():
    mins = list(sched[g].values())
    mins.sort()
    if mins[-1] > max_min:
        max_min = mins[-1]
        guard = g
        biggest_min = list(sched[g].keys())[list(sched[g].values()).index(mins[-1])]

print("2:", guard * biggest_min)