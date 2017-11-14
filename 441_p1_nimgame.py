# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 11:28:56 2017

@author: Zoey Lee
"""
infinity = 100000

def terminalTest(pile):
    if pile[1] > 1:
        return False
    for i in range(2,len(pile)):
        if pile[i]:
            return False
    return True
 
def Actions(pile):
    action = []
    change = 0
    for i in range(1,len(pile)):
        if pile[i] > 0:
            change += pile[i]
            for r in range(i-1, -1, -1):
                action.append([i,r+1])
    if change == 1:
        for act in action:
            if act[0] != 1:
                if act[0] == act[1]:
                    action.remove(act)
    return action
 
def maxValue(depth, alpha, beta, pile):
    if terminalTest(pile):
        return -infinity+depth
    action = Actions(pile)
    for move in action:
        pile = Move(pile, move,1)
        alpha = max(alpha, minValue(depth+1, alpha, beta, pile))
        if alpha >= beta:
            pile = Move(pile, move,0)
            return alpha
        pile = Move(pile, move,0)
    return alpha
 
def minValue(depth, alpha, beta, pile):
    if terminalTest(pile):
        return infinity-depth
    action = Actions(pile)
    for move in action:
        pile = Move(pile, move,1)
        beta = min(beta, maxValue(depth+1, alpha, beta, pile))
        if beta <= alpha:
            pile = Move(pile, move,0)
            return beta
        pile = Move(pile, move,0)
    return beta

def Move(pile, move, n):
    nxt = move[0] - move[1]
    if n==1:
        pile[move[0]] -= 1
        pile[nxt] += 1
    else:
        pile[move[0]] += 1
        pile[nxt] -= 1
        
    return pile

def display(piles, user, nextMove):
    print("current pile : ", piles)
    print(">> ", user,"'s next choice: ", nextMove,"\n")
        
        
def AlphaBetaSearch(num, piles, player):    
    print("initial pile : ", piles)
    while not terminalTest(piles):
        maxV = -infinity
        minV = infinity
        depth = 0
        nextMove = [0,0]
        action = Actions(piles)
        for act in action:
            user = 'computer' if player==1 else 'opponent'
            piles = Move(piles, act,1)
            if player:
                strength = minValue(depth+1, maxV, minV, piles)
                if strength > maxV:
                    nextMove = act
                    maxV = strength
            else:
                strength = maxValue(depth+1, maxV, minV, piles)
                if strength < minV:
                    nextMove = act
                    minV = strength
            piles = Move(piles, act,0)
        player *= -1
        display(piles, user, nextMove)  
        piles = Move(piles, nextMove,1)
    print("\n>> ",user, "LOST!")            
    user = 'computer' if user=='opponent' else 'opponent'
    print("\n>> ",user, "LOST!")

 
def main():
    num = 0
    while num<=0 or num>5:
        print("\nEnter the number of piles less than 5 : ", end='')
        num = int(input())
    piles = [0,0,0,0,num] #configuration   
    print(piles)
    player = 0
    while(player!=1 and player!=-1):
        print("\nChoose a player that goes first (1: computer, 2: opponent): ",end='')
        player = int(input())
        if(player==2):
            player=-1
    AlphaBetaSearch(num, piles, player)

main()