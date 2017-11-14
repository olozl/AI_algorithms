# -*- coding: utf-8 -*-
"""
Created on Tue Oct  31 03:18:34 2017

@author: Zoey Lee
"""

rand=[]
goal = [[1, 2, 3, 12], [8, 'b', 4, 13], [7, 6, 5, 14],[9, 10, 11, 15]]
init = [[2, 3, 3,8], [1, 6, 4, 13], [7, 'b', 5, 14],[9, 10, 11, 15]]
rand.append(init)
init = [[2, 8, 3,12], [1, 6, 4, 13], ['b', 7, 5, 14],[9, 10, 11, 15]]
rand.append(init)
init = [[1, 2, 3,12], [7, 8, 4, 13], ['b', 6, 5, 14],[9, 10, 11, 15]]
rand.append(init)
init = [[1, 'b', 3,12], [8, 2, 4, 13], [7, 6, 5, 14],[9, 10, 11, 15]]
rand.append(init)
init = [[1, 2, 3,12], [8, 6, 4, 13], [7, 'b', 5, 14],[9, 10, 11, 15]]
rand.append(init)


def misplace(a,b):
  c=0
  for i in range(4):
    for j in range(4):
      if a[i][j] != b[i][j]:
          c+=1
  return c

def manhattan(a,b):
  i=1
  gx=location(a)[0]-location(b)[0]
  gx = gx*-1 if gx<0 else gx
  gy=location(a)[1]-location(b)[1]
  gy = gy*-1 if gy<0 else gy
  result= gx+gy
  result= gx+gy
  while i<9:
    gx=location2(a,i)[0]-location2(b,i)[0]
    gy=location2(a,i)[1]-location2(b,i)[1]
    gx = gx*-1 if gx<0 else gx
    gy = gy*-1 if gy<0 else gy
    result= gx+gy
    i+=1
  return result

def myheuristic(a,b):
  sum1=0
  sum2=0
  for i in range(4):
    for j in range(4):
      if a[i][j] != 'b':
          loc = 4*i + j
          loc*=a[i][j]
          sum1+=loc
      if b[i][j] != 'b':
          loc2 = 4*i + j
          loc2*=b[i][j]
          sum2+=loc2
  return sum1-sum2 if sum1>sum2 else sum2-sum1

def isSame(a,b):
  for i in range(4):
    for j in range(4):
      if a[i][j] != b[i][j]:
        return False
  return True

def copy(p, p2):
  p2 = [[0 for x in range(4)] for y in range(4)]
  for i in range(4):
    for j in range(4):
      p2[i][j] = p[i][j]
  return p2
  
def location(p):
  for i in range(4):
    for j in range(4):
      if p[i][j] == 'b':
        return (i,j)
    
def location2(p,val):
  for i in range(4):
    for j in range(4):
      if p[i][j] == val:
        return (i,j)    
  
def MoveL(p):
  locX = location(p)[0]
  locY = location(p)[1]
  if locY>0:
    p[locX][locY] = p[locX][locY-1] 
    p[locX][locY-1] = 'b'
    return p
  return False

def MoveR(p):
  locX = location(p)[0]
  locY = location(p)[1]
  if locY<3:
    p[locX][locY] = p[locX][locY+1] 
    p[locX][locY+1] = 'b'
    return p
  return False
  
def MoveD(p):
  locX = location(p)[0]
  locY = location(p)[1]
  if locX<3:
    p[locX][locY] = p[locX+1][locY] 
    p[locX+1][locY] = 'b'
    return p
  return False  
  
def MoveU(p):
  locX = location(p)[0]
  locY = location(p)[1]
  if locX>0:
    p[locX][locY] = p[locX-1][locY] 
    p[locX-1][locY] = 'b'
    return p
  return False

def addintfrontier(frontier, p):
    for i in range(len(frontier)-1):
        if frontier[i][3]> p[3]:
            frontier.insert(i, p)
            return frontier
    frontier.append(p)    
    return frontier
    
def addintfrontier2(frontier, p):
    for i in range(len(frontier)-1):
        if (frontier[i][3]+frontier[i][2]) > (p[2]+p[3]):
            frontier.insert(i, p)
            return frontier
    frontier.append(p)    
    return frontier

def BFS(point, num):
  curr = point[0]
  parent = point[1]
  MAX = 50
  depth=0
  frontier=[]
  visited=[]
  cnt=0
  if num==1:
      print("\n>> Best-first Search - number of misplaced tiles")
  if num==2:
      print("\n>> Best-first Search - Manhattan")
  if num==3:
      print("\n>> Best-first Search - My heuristic")
      
  while MAX>0:
    cnt+=1
    depth+=1
    flag = 0
    print(curr,end=" ")
    if isSame(goal, curr):
        print("Goal!")
        return cnt
    for ele in visited:
      if isSame(ele[0], curr):
        flag = 1
    if flag==0:
      if num==1:
        h_misplace(curr, parent, depth, visited, frontier,1 )
      if num==2:
        h_manhattan(curr, parent, depth, visited, frontier,1)
      if num==3:
        h_myheuristic(curr, parent, depth, visited, frontier,1)
         
        
    if len(frontier)==0:
        print("-> FAILED", end=" ")
        return "FAILED"
    print("->",end=" ")
    curr = copy(frontier[0][0], [])
    parent = copy(frontier[0][1], [])
    frontier.pop(0)
    MAX-=1
  return cnt

def h_misplace(curr, parent, depth, visited, frontier, num):
    if num==1:
      visited.append([copy(curr,[]), parent, depth])
      par = copy(curr, [])
      if MoveL(curr)!=False:
        addintfrontier(frontier,[curr, par,depth, misplace(goal, curr)])
      curr = copy(par, [])
      if MoveR(curr)!=False:
        addintfrontier(frontier,[curr, par,depth, misplace(goal, curr)])
      curr = copy(par, [])
      if MoveU(curr)!=False:
        addintfrontier(frontier,[curr, par,depth, misplace(goal, curr)])
      curr = copy(par, [])
      if MoveD(curr)!=False:
        addintfrontier(frontier,[curr, par,depth, misplace(goal, curr)])
    else:
      visited.append([copy(curr,[]), parent, depth])
      par = copy(curr, [])
      if MoveL(curr)!=False:
        addintfrontier2(frontier,[curr, par,depth, misplace(goal, curr)])
      curr = copy(par, [])
      if MoveR(curr)!=False:
        addintfrontier2(frontier,[curr, par,depth, misplace(goal, curr)])
      curr = copy(par, [])
      if MoveU(curr)!=False:
        addintfrontier2(frontier,[curr, par,depth, misplace(goal, curr)])
      curr = copy(par, [])
      if MoveD(curr)!=False:
        addintfrontier2(frontier,[curr, par,depth, misplace(goal, curr)])
        
def h_manhattan(curr, parent, depth, visited, frontier, num):            
    if num==1:
      visited.append([copy(curr,[]), parent, depth])
      par = copy(curr, [])
      if MoveL(curr)!=False:
        addintfrontier(frontier,[curr, par,depth, manhattan(goal, curr)])
      curr = copy(par, [])
      if MoveR(curr)!=False:
        addintfrontier(frontier,[curr, par,depth, manhattan(goal, curr)])
      curr = copy(par, [])
      if MoveU(curr)!=False:
        addintfrontier(frontier,[curr, par,depth, manhattan(goal, curr)])
      curr = copy(par, [])
      if MoveD(curr)!=False:
        addintfrontier(frontier,[curr, par,depth, manhattan(goal, curr)])
    else:
      visited.append([copy(curr,[]), parent, depth])
      par = copy(curr, [])
      if MoveL(curr)!=False:
        addintfrontier2(frontier,[curr, par,depth, manhattan(goal, curr)])
      curr = copy(par, [])
      if MoveR(curr)!=False:
        addintfrontier2(frontier,[curr, par,depth, manhattan(goal, curr)])
      curr = copy(par, [])
      if MoveU(curr)!=False:
        addintfrontier2(frontier,[curr, par,depth, manhattan(goal, curr)])
      curr = copy(par, [])
      if MoveD(curr)!=False:
        addintfrontier2(frontier,[curr, par,depth, manhattan(goal, curr)])
 
def h_myheuristic(curr, parent, depth, visited, frontier, num):            
    if num==1:
      visited.append([copy(curr,[]), parent, depth])
      par = copy(curr, [])
      if MoveL(curr)!=False:
        addintfrontier(frontier,[curr, par,depth, myheuristic(goal, curr)])
      curr = copy(par, [])
      if MoveR(curr)!=False:
        addintfrontier(frontier,[curr, par,depth, myheuristic(goal, curr)])
      curr = copy(par, [])
      if MoveU(curr)!=False:
        addintfrontier(frontier,[curr, par,depth, myheuristic(goal, curr)])
      curr = copy(par, [])
      if MoveD(curr)!=False:
        addintfrontier(frontier,[curr, par,depth, myheuristic(goal, curr)])
    else:
      visited.append([copy(curr,[]), parent, depth])
      par = copy(curr, [])
      if MoveL(curr)!=False:
        addintfrontier2(frontier,[curr, par,depth, myheuristic(goal, curr)])
      curr = copy(par, [])
      if MoveR(curr)!=False:
        addintfrontier2(frontier,[curr, par,depth, myheuristic(goal, curr)])
      curr = copy(par, [])
      if MoveU(curr)!=False:
        addintfrontier2(frontier,[curr, par,depth, myheuristic(goal, curr)])
      curr = copy(par, [])
      if MoveD(curr)!=False:
        addintfrontier2(frontier,[curr, par,depth, myheuristic(goal, curr)])

       
def Astar(point, num):    
  curr = point[0]
  parent = point[1]
  MAX = 50
  depth=0
  frontier=[]
  visited=[]
  cnt=0
  if num==1:
      print("\n>> A* Search - number of misplaced tiles")
  if num==2:
      print("\n>> A* Search - Manhattan")
  if num==3:
      print("\n>> A* Search - My heuristic")
  while MAX>0:
    flag = 0
    depth+=1
    cnt+=1
    print(curr, end=" ")
    if isSame(goal, curr):
        print("Goal!")
        return cnt
    for ele in visited:
      if isSame(ele[0], curr):
        flag = 1
    if flag==0:
      if num==1:
        h_misplace(curr, parent, depth, visited, frontier,2)
      if num==2:
        h_manhattan(curr, parent, depth, visited, frontier,2)
      if num==3:
        h_myheuristic(curr, parent, depth, visited, frontier,2)    
    if len(frontier)==0:
        print("-> FAILED", end=" ")
        return "FAILED"
    print("->", end=" ")
    curr = copy(frontier[0][0], [])
    parent = copy(frontier[0][1], [])
    frontier.pop(0)
    MAX-=1
  return cnt
result=0
for i in range(5):
    result+=BFS([rand[i],None],1)
print("\n\n>>>>Average steps : ",result//5)
result=0
for i in range(5):
    result+=BFS([rand[i],None],2)
print("\n\n>>>>Average steps : ",result//5)
result=0
for i in range(5):
    result+=BFS([rand[i],None],3)
print("\n\n>>>>Average steps : ",result//5)
result=0
for i in range(5):
        result+=Astar([rand[i],None],1)
print("\n\n>>>>Average steps : ",result//5)
result=0
for i in range(5):
        result+=Astar([rand[i],None],2)
print("\n\n>>>>Average steps : ",result//5)
result=0
for i in range(5):
        result+=Astar([rand[i],None],3)
print("\n\n>>>>Average steps : ",result//5)
 