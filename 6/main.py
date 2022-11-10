points = dict()
with open("input.txt") as f:
    for i, pt in enumerate(f.readlines()):
        points[i] = (int(pt.split(",")[0]), int(pt.split(",")[1]))

x_min = 0
y_min = 0
x_max = 400
y_max = 400

field = dict() # keys = (x,y) values = (point, distance) if 2 points are the same distance, point = -1
for y in range(y_min, y_max):
    for x in range(x_min, x_max):
        if (x,y) not in field:
            field[(x,y)] = (-2, 1000000)

        for i in points.keys():
            dist = abs(x - points[i][0]) + abs(y - points[i][1])
            if dist < field[(x,y)][1]:
                field[(x,y)] = (i, dist)
            elif dist == field[(x,y)][1]:
                field[(x,y)] = (-1, dist)

edges = set() # set of all ranges that touch an edge assuming that means it goes on for infinity
for y in range(y_min, y_max):
    edges.add(field[(x_min, y)][0])
    edges.add(field[(x_max-1, y)][0])

for x in range(x_min, x_max):
    edges.add(field[(x, y_min)][0])
    edges.add(field[(x, y_max-1)][0])



counts = dict()
for pt, dist in field.values():
    if pt not in edges:
        if pt not in counts:
            counts[pt] = 1
        else:
            counts[pt] += 1

print("1:", max(counts.values()))

count = 0

for y in range(y_min, y_max):
    for x in range(x_min, x_max):
        sum = 0
        for dx, dy in points.values():
            sum += abs(x-dx) + abs(y - dy)
        if sum < 10000:
            count += 1

print("2:", count)