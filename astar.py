from tkinter import *
import random
from math import pi , acos , sin , cos
from heapq import heappush, heappop
class Node:
   def __init__(self,state,parent, graph):
      self.state =state
      self.parent = parent
      self.past =[state]
      self.pathLength = 0
      if parent is not None:
        self.past = list(parent.past)
        self.past.append(state)
        self.pathLength = parent.pathLength + graph.get_edge_length(parent.state, state)
class Graph():
  def __init__(self,graph):
    self.state =graph
  def get_neighbors(self,v):
    return self.state[v].keys()
  def get_edge_length(self, v1,v2):
    return self.state[v1][v2]
def goal_test(a, b):
  return a==b
def gcd(start, finish):
   if start== finish:
      return 0
   y1  = nodes[start][0]
   x1  = nodes[start][1]
   y2  = nodes[finish][0]
   x2  = nodes[finish][1]
   R   = 3958.76 # miles
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0
   
   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R
def astar(graph, start, finish):
   fringe = []
   heappush(fringe,(0,Node(start, None, graph)))
   x= set()
   count=0
   while fringe:
      temp = heappop(fringe)
      if temp[1].state not in x:
        x.add(temp[1].state)
        if temp[1].state== finish:
          return (temp[1],x)
        for a in graph.get_neighbors(temp[1].state):
          n =  Node(a, temp[1],graph)
          count+=1
          heappush(fringe, (n.pathLength + gcd(a,finish),n))
   return None  
   
#MAIN   
file = open("rrNodes.txt", "r")
nodes = {}
diction ={}
for line in file.readlines():
  temp = line.split(" ")
  nodes[temp[0]] = (float(temp[1]), float(temp[2]))
  diction[temp[0]] = {}
file2 = open("rrEdges.txt", "r")
vertex = {}

for line in file2.readlines():
  temp = line.strip("\n").split(" ")
  vertex[(temp[0],temp[1])]= gcd(temp[0],temp[1])
  
for x in vertex.keys():
  for y in range(2):
    diction[x[y]][x[(y+1)%2]]= vertex[x]
    
file = open("rrNodeCity.txt", "r")
names = {}

for line in file.readlines():
  line = line.strip("\n").split(" ",1)
  names[line[1]] = line[0]
graph = Graph(diction)




start = input("starting station : ")
end = input("ending station : ")
x = astar(graph, names[start], names[end])
y = x[1]
x=x[0]
print("path length : ", x.pathLength)
#for y in x.past:
   #print (y)
master = Tk()
w = Canvas(master, width=750, height=750)
for a in vertex:
    if (a[0] in x.past) or (a[1] in x.past) :
       w.create_line(float(nodes[a[0]][1]*10) +1325, float(nodes[a[0]][0]*-10) + 700, float(nodes[a[1]][1] *10)+1325, float(nodes[a[1]][0]*-10) + 700, fill = "red")
    if (a[0] in y) or (a[1] in y) :
       w.create_line(float(nodes[a[0]][1]*10) +1325, float(nodes[a[0]][0]*-10) + 700, float(nodes[a[1]][1] *10)+1325, float(nodes[a[1]][0]*-10) + 700, fill = "yellow")
    else:
       w.create_line(float(nodes[a[0]][1]*10) +1325, float(nodes[a[0]][0]*-10) + 700, float(nodes[a[1]][1] *10)+1325, float(nodes[a[1]][0]*-10) + 700)
w.pack()
master.mainloop()
