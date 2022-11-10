elves = 413
marble_max = 71082


class Marble:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def set_l(self, l):
        self.left = l

    def set_r(self, r):
        self.right = r

    def put_r(self, n):
        self.right.set_l(n)
        n.set_r(self.right)
        n.set_l(self)
        self.set_r(n)

    def remove_and_sum(self):
        self.right.set_l(self.left)
        self.left.set_r(self.right)
        return self.val

    def __str__(self):
        return str(self.val)

def move_cw(m, dist):
    for i in range(dist):
        m = m.right
    return m

def move_ccw(m, dist):
    for i in range(dist):
        m = m.left
    return m


scores = dict(default=0)
curr = Marble(0)
curr.set_l(curr)
curr.set_r(curr)
for i in range(1, marble_max):
    if i % 23 == 0:
        scores.setdefault((i-1) % elves + 1, 0)
        scores[(i-1) % elves + 1] += i
        temp = move_ccw(curr, 7)
        scores[(i-1) % elves + 1] += temp.remove_and_sum()
        curr = move_ccw(curr, 6)
    else:
        curr = move_cw(curr, 1)
        curr.put_r(Marble(i))
        curr = move_cw(curr, 1)

fin = list(scores.values())
fin.sort()
print("1:", fin[-1])


elves = 413
marble_max = 7108200

scores = dict(default=0)
curr = Marble(0)
curr.set_l(curr)
curr.set_r(curr)
for i in range(1, marble_max):
    if i % 23 == 0:
        scores.setdefault((i-1) % elves + 1, 0)
        scores[(i-1) % elves + 1] += i
        temp = move_ccw(curr, 7)
        scores[(i-1) % elves + 1] += temp.remove_and_sum()
        curr = move_ccw(curr, 6)
    else:
        curr = move_cw(curr, 1)
        curr.put_r(Marble(i))
        curr = move_cw(curr, 1)

fin = list(scores.values())
fin.sort()
print("2:", fin[-1])
