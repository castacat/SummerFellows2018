#Catherine Castagna
#Summer Fellows
#Discrete Independent Model Attempt 2
import math
import time
from pyqtgraph.Qt import QtGui, QtCore
from numpy import random
from random import randint
import pyqtgraph as pg
import numpy as np
import sys


paths=[]
tInc=1

def plot_path(x1,y1,x2,y2,size):
    pg.setConfigOption('background', 'w')
    pg.setConfigOption('foreground', 'k')

    app = QtGui.QApplication([])

    win = pg.GraphicsWindow(title="Collision Times Histogram")
    win.resize(800,600)

    current_plot = win.addPlot(title="Random Walk Paths of 2 Particles on "+str(size)+" by "+str(size)+" Grid")
    #pg.plot(p1x,p1y)#,connect='all',pen='r',symbol='o')
    #plotWidget.plot(p2x,p2y,connect='all',pen='b',symbol='x')     
    #y,x = np.histogram(x, y)
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            app.exec_()      
    for i in range(x1.len()):
        data1 = pg.PlotDataItem(x1[i:i+1], y1[i:i+1], connect='all',pen='r')
        data2 = pg.PlotDataItem(x2[i:i+1], y2[i:i+1], connect='all',pen='b')
        current_plot.addItem(data1)
        current_plot.addItem(data2)        
        time.sleep(0.5)
    data3 = pg.PlotDataItem(x2[-1:], y2[-1:],symbol='x', symbolBrush=(255,0,0), symbolSize=50)
    
    current_plot.addItem(data3)
    current_plot.setXRange(0,size-1,padding=0)
    current_plot.setYRange(0,size-1,padding=0)

def plot_dist(yd,size):
    pg.setConfigOption('background', 'w')
    pg.setConfigOption('foreground', 'k')
    app = QtGui.QApplication([])
    x=0

    win = pg.GraphicsWindow(title="Distances")
    win.resize(800,600)

    current_plot = win.addPlot(title="Distance Between Particles Over Time on "+str(size)+" by "+str(size)+" Grid",labels={'left': "Distance",'bottom':"Time"})
    #pg.plot(p1x,p1y)#,connect='all',pen='r',symbol='o')
    #plotWidget.plot(p2x,p2y,connect='all',pen='b',symbol='x')     
    #y,x = np.histogram(x, y)
    step=1
    for i in range(len(yd)):
        data1 = pg.PlotDataItem(list(range(len(yd[i]))[::step]), yd[i][::step],pen=(0+x,0,255-x,100),symbol=None)
        current_plot.addItem(data1)
        x=x+20
    current_plot.setXRange(0,3*math.pow(size,2),padding=0)
    current_plot.setYRange(2,size*2,padding=0)
    
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            app.exec_()
    

def runTrial(size):
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
            step1x=random.choice([1])
        elif(p1x[-1]==size-1):
            step1x=random.choice([-1])
        else:
            step1x=random.choice([-1,1])
        
        if(p1y[-1]==0):
            step1y=random.choice([1])
        elif(p1y[-1]==size-1):
            step1y=random.choice([-1])
        else:
            step1y=random.choice([-1,1])
        
        p1xBt=step1x+p1x[-1]
        p1x.append(p1xBt)
               
        p1yBt=step1y+p1y[-1]
        p1y.append(p1yBt)
        
        #move particle 2
        #add step, append new location
        if(p2x[-1]==0):
            step2x=random.choice([1])
        elif(p2x[-1]==size-1):
            step2x=random.choice([-1])
        else:
            step2x=random.choice([-1,1])
        
        if(p2y[-1]==0):
            step2y=random.choice([1])
        elif(p2y[-1]==size-1):
            step2y=random.choice([-1])
        else:
            step2y=random.choice([-1,1])  
        p2xBt=step2x+p2x[-1]
        p2x.append(p2xBt)
        p2yBt=step2y+p2y[-1]
        p2y.append(p2yBt)
        
        #update grid
        #grid[p1x[-2]][p1y[-2]]=0
        #grid[p2x[-2]][p2y[-2]]=0 
        #grid[p1x[-1]][p1y[-1]]=1
        #grid[p2x[-1]][p2y[-1]]=2
               
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
                #print("COLLIDED",flush=True)
                #grid[p2x[-1]][p2y[-1]]='X'
        if(time>=size*size):
            never=True
        #printMat(grid,size)
        #print()
    #plot_path(p1x,p1y,p2x,p2y,size)
    return time

def printMat(matrix,siz):
    for x in range(siz):
        for y in range(siz):
            print(matrix[x][y],end=' ',flush=True)
        print()
        

def runProgram(sideSize, numTrials):
    elapTim=time.clock()
    collTimes=[]
    size=sideSize
    #grid = [[0 for y in range(sideSize)] for x in range(sideSize)]
    for i in range(numTrials):
        #grid = [[0 for y in range(sideSize)] for x in range(sideSize)]
        collTimes.append(runTrial(size))
        if(i==math.floor(numTrials*75/100)):
            print("75% of Trials Completed")
        elif(i==math.floor(numTrials*50/100)):
            print("50% of Trials Completed")
        elif(i==math.floor(numTrials*25/100)):
            print("25% of Trials Completed")         
    mean=np.mean(collTimes)   
    stand=np.std(collTimes)
    print('Collision Times:',end=' ',flush=True)
    print(collTimes)
    print('Average Collision Time:',end=' ',flush=True)
    print(mean)
    print('Std of Collision Times:',end=' ',flush=True)
    print(stand,flush=True)
    elapTim=time.clock()-elapTim
    print('Time Elapsed:', end=' ',flush=True)
    print(elapTim,flush=True)    
    


runProgram(801,500)
runProgram(1001,500)
