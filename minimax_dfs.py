class Node:
   def __init__(self,state,parent,move):
      self.state =state
      self.move = move
      self.children=[]
      self.parent =parent
      self.isLeaf = False
def minmax(node, player):
   if node.isLeaf:
      return node
   elif player == "max":
      return max(node.children, key=lambda x: minmax(x,"min").state)
   else:       
      return min(node.children, key=lambda x: minmax(x,"max").state)
def dfs(board, player, pointer):
    global finalboard
    players=["x","o"]
    score = ["o",None, "x"]
    test=goal_test(board)
    if test!= False:
        pointer.isLeaf= True
        pointer.state= score.index(test[1])-1
    else:
        for a in make_children(board,player):
            pointer.children.append(Node(None,tree,a[1]))
            dfs(a[0],players[(players.index(player)+1)%2],pointer.children[-1])
def make_children(board,player):
    return [(board[:x]+player+board[x+1:], x) for x in range(9) if board[x] =="."]
def goal_test(board): # returns tuple of if it is done, who won
    x= [[0,1,2],[3,4,5],[6,7,8], [0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for y in x:
        temp = set([board[z] for z in y])
        if len(temp)==1 and "." not in temp:
            if "." in board:
                return (1,board[y[0]])
            else:
                return (1,board[y[0]])
    if'.' in board:
        return False
    else:
        return(1,None)
players=["x","o"]
board='.........'
tree = Node(None, None, None)
dfs(board,'x', tree)
for x in range(3):
   print( board[3*x:3*x+3])
while goal_test(board)== False:
   tree = minmax(tree, "min")
   board=board[:tree.move]+"x"+board[tree.move+1:]
   print "Opponent's move:", tree.move
   for x in range(3):
      print (board[3*x:3*x+3])
   if goal_test(board)==False:
      human = input('Your move: ')
      board=board[:human]+"o"+board[human+1:]
      for a in tree.children:
         if a.move ==human:
            tree = a
      for x in range(3):
         print (board[3*x:3*x+3])

