import sys
def possible(start, next, p):
    if start == n or len(next) == 0:
        return p
    else:
        s=set()
        for bob in next:
            temp =p
            temp.add((start, bob))
            billy =possible(bob, paths.get(bob),temp)
            for bill in billy:
                s.add(bill)

            return s
def time(tuple, j, overall1, overall2):
    set(tuple j [for x in range(0,10)])
line = input().split()
n,k,m = int(line[0]),int(line[1]), int(line[2])
times = {}
paths = {}
poss =[]
for x in range(m):
    line = input().split()
    a, b = int(line[0]),int(line[1])
    if a not in paths:
        paths[a] = {b}
    else:
        paths[a].add(b)
for x in range(1,k+1):
        temp = possible(x,paths.get(x),set())
        poss.append(temp)
print(poss)
