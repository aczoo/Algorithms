from collections import deque
import heapq
import time
import random
n = 4
class Node:
   def __init__(self,state,parent):
      self.state =state
      self.parent = parent
      self.children=[]
      self.past =[state]
      self.moves=[]
def make_move(state,direction):
   index = state.state.index('Z')
   x= list(state.state)
   if direction =="U" and index >n-1:
      temp = x[index - n]
      x[index - n] = x[index]
      x[index] = temp
      return Node("".join(x), state)
   elif direction == "D" and index <n*(n-1):
      temp = x[index + n]
      x[index + n] = x[index]
      x[index] = temp
      return Node("".join(x), state)
   elif direction =="L" and not index==n and not index ==0 and not index ==n*2 and not index==n*3:
      temp = x[index - 1]
      x[index - 1] = x[index]
      x[index] = temp
      return Node("".join(x), state)
   elif direction =="R" and not index ==n-1 and not index==n*2-1 and not index ==n*3-1 and not index==n*n-1:
      temp = x[index +1]
      x[index +1] = x[index]
      x[index] = temp
      return Node("".join(x), state)
   return Node(None, None)
def goal_test(state):
   return (state.state =="ABCDEFGHIJKLMNOZ")
def make_children(state):
   global totalnodes
   for char in (list("UDLR")):
      x = make_move(state, char)
      if not x.state ==None:
         totalnodes+=1
         x.past=state.past+x.past
         x.moves.append(char)
         state.children.append(x)
def geti(o, state):
   return state.index(o)%(n)
def getj(o, state):
   return state.index(o)/(n)
def man(state):
   returnval = 0
   goal = "ABCDEFGHIJKLMNOZ"
   for char in list(goal):
     returnval=returnval +abs(geti(char, state)-geti(char,goal)) + abs(getj(char, state)-getj(char,goal))
   return returnval
def frac(state):
   returnval = 0
   goal = "ABCDEFGHIJKLMNOZ"
   for char in list(goal):
     if(geti(char,state)==geti(char,goal) and getj(char,state)==getj(char,goal)):
      returnval =returnval+1
   return returnval/16.00
   
def kdfs(depth, state):
   fringe = []
   fringe.append(state)
   while fringe:
      temp = fringe.pop()
      if len(temp.past)<depth:
        if goal_test(temp):
          return temp
        make_children(temp)
        for a in temp.children:
          if not a.state in temp.past:
            fringe.append(a)
   return None
def bfs(state):
 fringe = deque()
 fringe.append(state)
 while fringe:
   temp = fringe.popleft()
   if goal_test(temp):
    return temp
   make_children(temp)
   for a in temp.children:
       if a.state not in temp.past:
        fringe.append(a)
 return None
def greedy(state):
   fringe = []
   heapq.heappush(fringe,(man(state.state)+len(state.past)+random.random(),state))
   x=set()
   while fringe:
      temp = heapq.heappop(fringe)
      if goal_test(temp[1]):
         return temp[1]
      make_children(temp[1])
      for a in temp[1].children:
         if not a.state in x:
            x.add(a.state)
            heapq.heappush(fringe, (man(a.state)+len(a.past)+random.random(),a))
   return None
def i_DFS(state, max):
  for x in range(max):
    solution = iterative(state,[], x)
    if solution is not None:
      return solution

def iterative(a,past, depth):
  if goal_test(a):
    return a
  if depth==0:
    return
  make_children(a)
  for c in a.children:
    if c.state not in past:
      past.append(c.state)
      solution = iterative(c, past,depth-1)
      if solution is not None:
        return solution
  return None

def bi_BFS(state):
  goal = Node("ABCDEFGHIJKLMNOZ", None)
  dictionary1= {}
  dictionary2= {}
  fringe1 = deque()
  fringe1.append(state)
  fringe2 = deque()
  fringe2.append(goal)
  while fringe1 or fringe2:
   temp1 = fringe1.popleft()
   temp2 = fringe2.popleft()
   make_children(temp1)
   make_children(temp2)
   for a in temp1.children:
     if a.state not in dictionary1:
       dictionary1[a.state] = a
       fringe1.append(a)
     elif a.state in dictionary2:
       temp = Node(goal, None)
       temp.past = a.past[0:-1]+dictionary2[a.state].past[::-1]
       return temp
   for b in temp2.children:
     if b.state not in dictionary2:
       dictionary2[b.state] = b
       fringe2.append(b)
     elif b.state in dictionary1:
       temp =Node(goal,None)
       temp.past = dictionary1[b.state].past[0:-1] + b.past[::-1]
       return temp

  
  
def test_method(f, args, verbose = 1):
    global totalnodes
    totalnodes=0 
    tic = time.time()
    sol = f(*args)
    toc = time.time()
    if verbose == 1:
        print ("\n------Testing %s ------- \n" % f.__name__)
        if sol is not None:
            print("Solution Found")
            print("Node count: %i" % totalnodes)
            print("Length: %i steps, Time: %5.4f" % (len(sol.past), toc-tic))
            print_steps(sol)
        else:
            print("Unsolvable")

    elif verbose == 0:
        if sol is not None:
            print("Solved. %10s %8i Nodes\t %4i Steps\t %5.5f secs\t %6.0f N/s" % (f.__name__, totalnodes, len(sol.past)-1, toc-tic, \
                                                                                  totalnodes / (toc-tic)))
        else:
            print("Unsolv. %10s %8i Nodes\t %4i Steps\t %5.5f secs\t %6.0f N/s" % (f.__name__, totalnodes, 0, toc-tic, \
                                                                                  totalnodes / (toc-tic)))

def multi_solver(start_state = None):
    state = start_state
    print("\n---->Solving ", state.state)
    #test_method(bfs,(state,), 0)
    #test_method(kdfs,(30, state), 0)
    test_method(i_DFS, (state,25), 0)
    #test_method(bi_BFS, (state,), 0)
    #test_method(greedy, (state,), 0)
    
def print_steps(sol):
  states = sol.past
  moves = sol.moves
  for x in range (len(moves)):
    print(moves[x],"\t")
  right=4
  left = 0
  for a in range(3):
    for y in range(len(states)):
        print((states[y])[left:right],"\t")
    left+=4
    right+=4
    
x = ["ABCDEFGZIJKHMNOL",
"ABCZEFGDIJKHMNOL",
"ABZCEFHDIJGKMNOL",
"AZBCEFGDIJKHMNOL",
"ABGCEFKDZIJHMNOL",
"BCDZAFGHEIJLMNKO",
"EACDIBGHMFJLNZKO",
"ABCDFGKHEJNLZIMO",
"ZEBDIACHFGKLMJNO",
"ABCDEFGHIOJNMKZL",
"ZCGDBAJHFEKLIMNO",
"ABCZEFHDMJIGNKOL",
"BCGDAFHLEKZOIMNJ"]
multi_solver(Node(x[10],None))
#for f in x:
	#multi_solver(Node(f,None))