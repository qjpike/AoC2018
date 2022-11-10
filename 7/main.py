import copy
from collections import deque

dependencies = dict()
dependents = set()
starters = set()

with open("input.txt") as f:
    for l in f.readlines():
        starter = l.split()[1]
        dependent = l.split()[7]

        if dependent not in dependencies:
            dependencies[dependent] = []
        dependencies[dependent].append(starter)

        dependents.add(dependent)
        starters.add(starter)

todo = list(starters - dependents)
todo.sort()
result = ''
while len(todo) > 0:
    result += todo[0]
    todo.remove(todo[0])
    new_deps = copy.deepcopy(dependencies)
    for dep, starters in new_deps.items():
        if result[-1] in starters:
            dependencies[dep].remove(result[-1])
            if len(dependencies[dep]) == 0:
                todo.append(dep)
                del dependencies[dep]
    todo.sort()

print("1:", result)




def calc_time(in_ch):
    return ord(in_ch) - ord("A") + 61

dependencies = dict()
dependents = set()
starters = set()

with open("input.txt") as f:
    for l in f.readlines():
        starter = l.split()[1]
        dependent = l.split()[7]

        if dependent not in dependencies:
            dependencies[dependent] = []
        dependencies[dependent].append(starter)

        dependents.add(dependent)
        starters.add(starter)

todo = list(starters - dependents)
todo.sort()
result = ''
workers = dict()
workers[todo[0]] = calc_time(todo[0])
todo.remove(todo[0])
count = 0
while len(todo) > 0 or len(workers) > 0:
    count += 1
    while len(workers) < 5 and len(todo) > 0:
        workers[todo[0]] = calc_time(todo[0])
        todo.remove(todo[0])
    temp = list(workers.keys())
    for i in temp:
        workers[i] -= 1
        if workers[i] == 0:
            del workers[i]
            temp2 = copy.deepcopy(dependencies)
            for t in temp2.keys():
                if i in dependencies[t]:
                    dependencies[t].remove(i)
                    if len(dependencies[t]) == 0:
                        todo.append(t)
                        todo.sort()
                        del dependencies[t]


print(count)