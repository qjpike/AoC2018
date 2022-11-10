with open("input.txt") as f:
    dat = []
    for i in f.read().split():
        dat.append(int(i))


class Node:
    def __init__(self, children, metadata):
        self.children = children
        self.metadata = metadata

    def task1(self):
        sum = 0
        for i in self.children:
            sum += i.task1()
        for i in self.metadata:
            sum += i
        return sum

    def task2(self):
        sums = 0

        if len(self.children) == 0:
            return sum(self.metadata)


        for i in self.metadata:
            if len(self.children) > i-1:
                sums += self.children[i-1].task2()

        return sums

def recursive_tree_builder(inp, idx):

    ch_count = inp[idx]
    idx += 1
    metadata_count = inp[idx]
    idx += 1

    children = []
    metadata = []

    for i in range(ch_count):
        child, idx = recursive_tree_builder(inp, idx)
        children.append(child)

    for i in range(metadata_count):
        metadata.append(inp[idx])
        idx += 1

    return Node(children, metadata), idx

tree, idx = recursive_tree_builder(dat, 0)

print("1:", tree.task1())

print("2:", tree.task2())

