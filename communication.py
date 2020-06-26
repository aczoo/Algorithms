#import math
def distance(fx,fy, sx,sy):
    return ((sx- fx)**2 + (sy- fy)**2)**.5


def intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])
    if xdiff[0]*ydiff[1]-xdiff[1]*ydiff[0] == 0:
        return False
    return True
# def generatecircumference(x,y,r,p):
#     l = list()
#     for c in range(0,p+1):
#         l.append((x+r* math.cos(c), y+r* math.sin(c)))
#     return l


i = int(input())
disks = dict()
for a in range(i):
    line = input().split(" ")
    #disks[a] = generatecircumference(int(line[0]),int(line[1]), int(line[2]),100)
    disks[a] = (int(line[0]),int(line[1]), int(line[2],0))
fdistance = 50000000000000
for i in disks.keys():
    possiblen,tempd, current = list(disks.keys()), 0,i
    possiblen.remove(i)
    lines= set()
    while possiblen:
        d,pair= 10000,0
        for j in possiblen:
            line =((disks[current][0],disks[current][1]),(disks[j][0],disks[j][1]))
            if True in [intersection(line, h) for h in lines] or lines.isEmpty():
                e = min(d , distance(disks[current][0],disks[current][1],disks[j][0],disks[j][1])- disks[current][2]-disks[j][2])
                if not e == d:
                    pair, d = j, e
                    # checked each line, needs to grab the line of the min distance and then add it to the set lines
        tempd += d
        current = pair
        possiblen.remove(pair)
    if tempd < fdistance:
        fdistance = tempd
print(fdistance)