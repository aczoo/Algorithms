from collections import deque
class Board():
  def __init__(self,board):
    self.state =board
  def get_col(self,x, y):
    return self.state[:,y]
  def get_kids(self, x,y):
      possible = {1,2,3,4,5,6,7,8,9}
      possible = possible.difference(set(self.get_row(x,y)))
      possible = possible.difference(set(self.get_col(x,y)))
      possible = possible.difference(set(self.get_square(x,y)))
      temp = []
      for a in possible:
          y = Board(self.state)
          y.state[x][y] = a
          temp.append(y)
      return temp
    
  def get_row(self, x, y):
    return self.state[x]
  def get_square(self, x, y):
    x=(x//3)*3
    y=(y//3)*3
    result = []
    for a in range(3):
        for b in range(3):
            result.append(self.state[x+a][y+b])
    return result
  def goal_test(self):
      for a in range(3):
          for b in range(3):
              if not self.get_square(a*3, b*3).sort() == [1,2,3,4,5,6,7,8,9]:
                  return False
      for x in range(9):
          if not self.get_row(0,x).sort() ==[1,2,3,4,5,6,7,8,9]:
              return False 
          if not self.get_col(x,0).sort() ==[1,2,3,4,5,6,7,8,9]:
              return False
      return True
  def check_empty(self):
    toReturn = []
    for x in range(9):
       for y in range(9):
            if self.state[x][y] == 0:
                toReturn.append((x,y))

    return toReturn
  
 
def bfs(board):
 fringe = deque()
 fringe.append(board)
 while fringe:
   temp = fringe.popleft()
   if temp.goal_test():
    return temp
    
   l = board.check_empty()
                                     
   for x,y in l:
        for a in board.get_kids(x,y):
            fringe.append(a)
 return None

           
x= [[0, 7, 0, 0, 0, 0, 0, 6, 2],[0, 0, 6, 0, 7, 2, 8, 0, 4],[0,2, 3, 4, 6, 0, 5, 0, 7],[0, 0, 5, 9, 0, 0, 0, 0, 0],[0, 3, 4, 7, 1, 6, 2, 8, 0],[0, 0, 0, 0, 0, 8, 9, 0, 0],[6, 0, 8, 0, 2, 1, 7, 3, 0],[3, 0, 7, 6, 9, 0, 1, 0, 0],[1, 9, 0, 0, 0, 0, 0, 5, 6]]
bfs(Board(x))
              
