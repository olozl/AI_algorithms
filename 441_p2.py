# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 20:15:12 2017

@author: Zoey Lee
"""
import random
import time

"""
name # weight # value
#####################
A    # 45     # 3
B    # 40     # 5
C    # 50     # 8
D    # 90     # 10

MaxWeight = 100 
genome = (tot (0/1 0/1 0/1 0/1))
"""

def genome(weights, values, MutationPct, MaxWeight):
    res = []
    cp = (MutationPct[1])[:]
    V=0
    W=0
    for i in range(len(cp)):
        cp[i] *= weights[i]
        
    for j in range(len(cp)):
        if cp[j]!=0:
            V += values[j]
            W += weights[j]
        if W > MaxWeight:
            V = 0
        res.append([V,MutationPct[1]])
    return res[len(MutationPct[1])-1]

def newPct(possible, PopulationSize, weights, values, MaxWeight):
    ret = []
    ret.append(possible)
    for i in range(PopulationSize):
        child = crossover(ret[random.randint(0,len(ret)-1)][1],ret[random.randint(0,len(ret)-1)][1])
        pick = random.randint(0,1)
        pick2 = random.randint(0,1)
        if pick==1:
          ret.append(genome(weights, values, [0,mutate(child[0])], MaxWeight))
        else:
          ret.append(genome(weights, values, [0,child[0]], MaxWeight))
           
        if pick2==1:
          ret.append(genome(weights, values, [0,mutate(child[1])], MaxWeight))
        else:
          ret.append(genome(weights, values, [0,child[1]], MaxWeight))
    return largest(ret)

def largest(gn):
    lar = [-10000,0]
    for i in range(len(gn)):
      if gn[i][0]>lar[0]:
          lar = gn[i]
    return lar

def delSmallHelper(gn):
    small = 0
    for i in range(len(gn)):
      if gn[i][0]<gn[small][0]:
        small = i 
    gn.pop(small)
    return gn

def delSmall(gn, maxSize):
    while len(gn)>=maxSize:
      gn = delSmallHelper(gn)
    return gn
      
def crossover(g1, g2):
    randpoint = random.randint(0,len(g1)-1)
    child1 = g1[:randpoint] + g2[randpoint:]
    child2 = g2[:randpoint] + g1[randpoint:]
    return [child1,child2]

def mutate(gn):
    randpoint = random.randint(0,len(gn)-1)
    gn[randpoint] = 0 if gn[randpoint]==1 else 1
    return gn


def knapsack():
    """
    PopulationSize = 3 
    NumIterations = 5
    MaxWeight = 100
    values = [3,5,8,10]
    weights = [45,40,50,90]
    """
    PopulationSize = 50
    NumIterations = 50
    MaxWeight = 6
    weights = [1,3,2,3,2,3,3]
    values = [2,100,5,3,50,16,60]
    print("\nGiven item: ", end="")
    for i in range(len(values)):
      print("[",values[i],end=", ")
      print(weights[i],end=" ]")
      if i!=len(values)-1:
        print(", ", end="")
    print("\nKnapsack maximum weight: ", MaxWeight)

    MutationPct = [0,[random.randint(0,1) for i in range(len(weights))]]
    gn = genome(weights, values, MutationPct, MaxWeight)
    MutationPct = gn[:]
    ret=[]
    i=0
    while i < NumIterations:
        i += 1
        MutationPct = newPct(gn, PopulationSize, weights, values, MaxWeight)
        ret.append(MutationPct)
        ret = delSmall(ret, PopulationSize)
        gn = genome(weights, values, MutationPct, MaxWeight)
     
    return largest(ret)

start = time.time()        
print("\nBest combination: ",knapsack())
end = time.time()        
print("Time spent: %.2fsec" %float(end-start), end='\n\n')
