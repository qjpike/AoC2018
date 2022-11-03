with open("input.txt") as f:
    inp = f.readlines()

field = dict()

for i in inp:
    claim = i.split()[0]
    coord = i.split()[2]
    size = i.split()[-1]

    start_x = int(coord.split(",")[0])
    start_y = int(coord.split(",")[1][:-1])

    size_x = int(size.split("x")[0])
    size_y = int(size.split("x")[1])

    for y in range(start_y, start_y + size_y):
        for x in range(start_x, start_x + size_x):
            if (x, y) not in field:
                field[(x,y)] = 1
                overlaps = 1
            else:
                field[(x,y)] += 1


count = 0
for i in field.values():
    if i >= 2:
        count += 1

print("1:", count)

for i in inp:
    claim = i.split()[0]
    coord = i.split()[2]
    size = i.split()[-1]

    start_x = int(coord.split(",")[0])
    start_y = int(coord.split(",")[1][:-1])

    size_x = int(size.split("x")[0])
    size_y = int(size.split("x")[1])

    m = 0
    for y in range(start_y, start_y + size_y):
        for x in range(start_x, start_x + size_x):
            m = max(m, field[(x,y)])

    if m == 1:
        print("2:", claim[1:])