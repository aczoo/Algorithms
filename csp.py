import time
import math
from random import shuffle
import matplotlib.pyplot as plt
class Board:
    def __init__(self,l):
        self.queens = [ [-1,{x for x in range(0,l)},y] for y in range(0,l)]
        self.l=l
    def get_next(self):
        temp = [self.queens[x] for x in range(0,self.l) if self.queens[x][0]==-1]
        temp.sort(key=lambda x:len(x[1]))
        return temp[0]
    def goalTest(self):
        if  [self.queens[x][0] for x in range(0,self.l) if self.queens[x][0]==-1]:
            return False
        return True
    def alter(self, queen, val):
        d = queen[2] - val+self.l-1
        dr=math.fabs(val+queen[2]-2*(self.l-1))
        self.queens[queen[2]][0] = val
        for x in self.queens:
            if x[2] != queen[2] and x[0] ==-1:
                x[1].discard(val)
                if x[2]<=d:
                    x[1].discard(self.l-d+x[2]-1)
                if math.fabs(x[2]-self.l)<=dr:
                    x[1].discard(math.fabs(dr - 2*(self.l-1))-x[2])
def csp(board):
    global count
    count+=1
    if (count>2000 and board.l<200) or (count>3000 and board.l>=200):
        count = 0
        return csp(Board(board.l))
    elif (count<2000 and board.l<200) or (count<3000 and board.l>=200):
        if board.goalTest():
            return board
        else:
            temp2 = board.get_next()
            if temp2:
                if temp2[1]:
                    l = list(temp2[1])
                    shuffle(l)
                    for x in l:
                        temp= Board(board.l)
                        temp.queens = [[int(x[0]),set(x[1]),int(x[2])]for x in board.queens]
                        temp.alter(temp2,x)
                        result= csp(temp)
                        if result!=False:
                            return result
    return False

g= []
value= []
t = []
for x in range(4,300,2):
    print(x)
    count=0
    board = Board(x)
    tic = time.time()
    temp = csp(board)
    toc = time.time()
    if temp:
        value.append(count)
        g.append(x)
        t.append(toc-tic)
f, ax = plt.subplots(2, sharex = True)
ax[0].plot(g, value)
ax[0].set_title('Size vs Nodes Created')
plt.xlabel('Size of Board')
plt.ylabel('Nodes Created')
#ax[1].plot(g, [math.log10(x) for x in value])
#ax[1].set_title('Size vs log(Nodes Created)')
ax[1].plot(g,t)
ax[1].set_title('Size vs Time')
plt.xlabel('Size of Board')
plt.ylabel('Time')
plt.show()
