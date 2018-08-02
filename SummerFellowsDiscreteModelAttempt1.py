#Catherine Castagna
#Summer Fellows
#Discrete Independent Model Attempt 1

from random import randint
import math

paths=[]
tInc=1



def runTrial(size,grid):
    collided=False
    never=False
    time=0
    step1x=0
    step1y=0
    step2x=0
    step2y=0
    p1x=[0]
    p1y=[0]
    p2x=[size-1]
    p2y=[size-1]
    while(collided==False):
        time+=tInc
        #move particle 1
        #calculate p1x stepDist
        #add step, append new location
        if(p1x[-1]==0):
            step1x=randint(0,1)
        elif(p1x[-1]==size-1):
            step1x=randint(-1,0)
        else:
            step1x=randint(-1,1)
        
        if(p1y[-1]==0):
            step1y=randint(0,1)
        elif(p1y[-1]==size-1):
            step1y=randint(-1,0)
        else:
            step1y=randint(-1,1)
        
        p1xBt=step1x+p1x[-1]
        p1x.append(p1xBt)
               
        p1yBt=step1y+p1y[-1]
        p1y.append(p1yBt)
        
        #move particle 2
        #add step, append new location
        if(p2x[-1]==0):
            step2x=randint(0,1)
        elif(p2x[-1]==size-1):
            step2x=randint(-1,0)
        else:
            step2x=randint(-1,1)
        
        if(p2y[-1]==0):
            step2y=randint(0,1)
        elif(p2y[-1]==size-1):
            step2y=randint(-1,0)
        else:
            step2y=randint(-1,1)  
        p2xBt=step2x+p2x[-1]
        p2x.append(p2xBt)
        p2yBt=step2y+p2y[-1]
        p2y.append(p2yBt)
        
        #update grid
        grid[p1x[-2]][p1y[-2]]=0
        grid[p2x[-2]][p2y[-2]]=0 
        grid[p1x[-1]][p1y[-1]]=1
        grid[p2x[-1]][p2y[-1]]=2
               
        #print('Time: ',end='',flush=True)
        #print(time)
        #print('P1(x,y)= ',end='',flush=True)
        #print(p1x[-1],end=' ',flush=True)
        #print(p1y[-1],end=' ',flush=True)
        #print('P2(x,y)= ',end='',flush=True)
        #print(p2x[-1],end=' ',flush=True)
        #print(p2y[-1])
        
        if(p1x[time]==p2x[time]):
            if(p1y[time]==p2y[time]):
                collided=True
                grid[p2x[-1]][p2y[-1]]='X'
        if(time>=size*size):
            never=True
        #printMat(grid,size)
        #print()        
    return time

def printMat(matrix,siz):
    for x in range(siz):
        for y in range(siz):
            print(matrix[x][y],end=' ',flush=True)
        print()
        

def runProgram(sideSize, numTrials):
    collTimes=[]
    size=sideSize
    grid = [[0 for y in range(sideSize)] for x in range(sideSize)]
    for i in range(numTrials):
        grid = [[0 for y in range(sideSize)] for x in range(sideSize)]
        collTimes.append(runTrial(sideSize,grid))
    print('Collision Times:',end=' ',flush=True)
    print(collTimes)
    
runProgram(3,1)
runProgram(100,100)