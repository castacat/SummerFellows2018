#Catherine Castagna
#Summer Fellows
#Discrete Independent Model Attempt 1

import math
import time
from pyqtgraph.Qt import QtGui, QtCore
from numpy import random
from random import randint
import pyqtgraph as pg
import numpy as np
import sys

distArr=[]

def plot_hist(x,b):
    pg.setConfigOption('background', 'w')
    pg.setConfigOption('foreground', 'k')

    app = QtGui.QApplication([])

    win = pg.GraphicsWindow(title="Histogram")
    win.resize(800,600)

    current_plot = win.addPlot(title="Collision Times Histogram")
    y,x = np.histogram(x, bins=b)
    curve = pg.PlotCurveItem(x, y, stepMode=True, fillLevel=0, brush=(0, 0, 255, 80))
    current_plot.addItem(curve)
    
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            app.exec_()    

def plot_path(x1,y1,x2,y2,size):
    pg.setConfigOption('background', 'w')
    pg.setConfigOption('foreground', 'k')

    app = QtGui.QApplication([])

    win = pg.GraphicsWindow(title="Paths of Two Particles")
    win.resize(800,600)

    current_plot = win.addPlot(title="Random Walk Paths of 2 Particles on "+str(size)+" by "+str(size)+" Grid")
    #pg.plot(p1x,p1y)#,connect='all',pen='r',symbol='o')
    #plotWidget.plot(p2x,p2y,connect='all',pen='b',symbol='x')     
    #y,x = np.histogram(x, y)
    data1 = pg.PlotDataItem(x1, y1,pen='r',symbol='o',brush=(0, 0, 255, 100))
    data2 = pg.PlotDataItem(x2, y2,pen='b',symbol='t')
    current_plot.addItem(data1)
    current_plot.addItem(data2)
    current_plot.setXRange(0,size,padding=0)
    current_plot.setYRange(0,size,padding=0)
    
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            app.exec_()   

def plot_dist(yd,size):
    pg.setConfigOption('background', 'w')
    pg.setConfigOption('foreground', 'k')
    app = QtGui.QApplication([])
    x=0

    win = pg.GraphicsWindow(title="Distances")
    win.resize(800,600)

    current_plot = win.addPlot(title="Distance Between Correlated Particles Over Time on "+str(size)+" by "+str(size)+" Grid",labels={'left': "Distance",'bottom':"Time"})
    #pg.plot(p1x,p1y)#,connect='all',pen='r',symbol='o')
    #plotWidget.plot(p2x,p2y,connect='all',pen='b',symbol='x')     
    #y,x = np.histogram(x, y)
    step=1
    for i in range(len(yd)):
        data1 = pg.PlotDataItem(list(range(len(yd[i]))[::step]), yd[i][::step],pen=(0+x,0,255-x,100),symbol=None)
        current_plot.addItem(data1)
        x=x+20
    current_plot.setXRange(0,2*math.pow(size,2),padding=0)
    current_plot.setYRange(2,size*2,padding=0)
    
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            app.exec_()  

           
            
def runTrial(size,rad,F0):
    collided=False
    never=False
    time=0
    s1x=''
    s1y=''
    s2x=''
    s2y=''
    step1x=0
    step1y=0
    step2x=0
    step2y=0
    p1x=[0]
    p1y=[0]
    p2x=[size-1]
    p2y=[size-1]
    distOverTime=[math.sqrt(math.pow(size,2)+math.pow(size,2))]
       
    
    while(collided==False):
        time+=1
        a=0
        b=0
        F=0
        optionsFourD=[]
        probabsFourD=[]          
        #calculate F
        dist=math.sqrt((p1x[-1]-p2x[-1])**2+(p1y[-1]-p2y[-1])**2)

        #print("Distance:",end=' ',flush=True)
        #print(dist,end=' ',flush=True)
        #print("Radius:",end=' ',flush=True)
        #print(rad,end=' ',flush=True)
        if(dist>=2*rad):
            F=0
        else:
            q=2*math.acos(dist/(2*rad))
            F=rad**2*(q-math.sin(q))/F0           
        
        x1=''
        y1=''
        x2=''
        y2=''
        #calculate a and b
        a=(1+F)/4
        b=(1-F)/4
        #list of 4-dimensional options and probabilities
        for z1 in ['n','1']:
            for z2 in ['n','1']:
                for z3 in ['n','1']:
                    for z4 in ['n','1']:
                        optionsFourD.append(z1+z2+z3+z4)
                        #translate
                        if(z1=='n'):
                            x1=-1
                        else:
                            x1=1
                        if(z2=='n'):
                            y1=-1
                        else:
                            y1=1 
                        if(z3=='n'):
                            x2=-1
                        else:
                            x2=1
                        if(z4=='n'):
                            y2=-1
                        else:
                            y2=1 
                        
                        if(x1*y1*x2*y2==-1):
                            probabsFourD.append(a*b)
                        elif(x1*x2==1):
                            probabsFourD.append(a**2)
                        elif(x1*x2==-1):
                            probabsFourD.append(b**2)
                        
        #choose 4D movement option
        #print(optionsFourD)
        #print(probabsFourD)
        
        step=random.choice(optionsFourD,1,probabsFourD)[0]
        #print('4D Move Chosen: ',end='',flush=True)
        #print(step)
        #define each step
        s1x=step[0]
        s1y=step[1]
        s2x=step[2]
        s2y=step[3]
        
        #translate
        if(s1x=='n'):
            step1x=-1
        else:
            step1x=1
        if(s1y=='n'):
            step1y=-1
        else:
            step1y=1 
        if(s2x=='n'):
            step2x=-1
        else:
            step2x=1
        if(s2y=='n'):
            step2y=-1
        else:
            step2y=1 
            
        #reflect particle if out of bounds
        if(p1x[-1]==0 and step1x==-1):
            step1x=1
        elif(p1x[-1]==size-1 and step1x==1):
            step1x=-1
        
        if(p1y[-1]==0 and step1y==-1):
            step1y=1
        elif(p1y[-1]==size-1 and step1y==1):
            step1y=-1
        
        if(p2x[-1]==0 and step2x==-1):
            step2x=1
        elif(p2x[-1]==size-1 and step2x==1):
            step2x=-1
            
        if(p2y[-1]==0 and step2y==-1):
            step2y=1
        elif(p2y[-1]==size-1 and step2y==1):
            step2y=-1        
        
        #move particles
        p1xBt=step1x+p1x[-1]
        p1yBt=step1y+p1y[-1]
        #grid[p1x[-1]][p1y[-1]]=0
        p1x[0]=(p1xBt)   
        p1y[0]=(p1yBt)
        
        p2xBt=step2x+p2x[-1]
        p2yBt=step2y+p2y[-1]
        #grid[p2x[-1]][p2y[-1]]=0        
        p2x[0]=(p2xBt)
        p2y[0]=(p2yBt)
        
        
        #update grid 
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
        dist=math.sqrt((p1x[-1]-p2x[-1])**2+(p1y[-1]-p2y[-1])**2)
        #distOverTime.append(dist)
        if(dist<2):
            collided=True
            #grid[p2x[-1]][p2y[-1]]='X'
            #print("++++++++++++++++++++COLLIDED++++++++++++++++++++++++++")
        if(time>=size*size*size*size):
            never=True
        #printMat(grid,size)
        #print()  
    
    #distArr.append(distOverTime)
    return time

def printMat(matrix,siz):
    for x in range(siz):
        for y in range(siz):
            print(matrix[x][y],end=' ',flush=True)
        print()
        

def runProgram(sideSize, numTrials):
    elapTim=time.clock()
    collTimes=[]
    radi=sideSize/4
    q_0=2*math.acos(0/(2*radi))
    F_0=radi**2*(q_0-math.sin(q_0))       
    for i in range(numTrials):
        collTimes.append(runTrial(sideSize,radi,F_0))
        if(i==math.floor(numTrials*75/100)):
            print("75% of Trials Completed")
        elif(i==math.floor(numTrials*50/100)):
            print("50% of Trials Completed")
        elif(i==math.floor(numTrials*25/100)):
            print("25% of Trials Completed")   
    #plot_dist(distArr,sideSize)
    mean=np.mean(collTimes)   
    stand=np.std(collTimes)
    print('Collision Times:',end=' ',flush=True)
    print(collTimes)
    print('Average Collision Time:',end=' ',flush=True)
    print(mean)
    print('Std of Collision Times:',end=' ',flush=True)
    print(stand,flush=True)    
    #hist=np.histogram(collTimes,bins=10)
    #print(hist,flush=True)
    #plot_hist(collTimes,20)
    #pg.plot(hist[0],hist[1])
    #pg.ImageView(view=pg.PlotItem())
    #w.show()
   
    #w.setImage(hist)
    elapTim=time.clock()-elapTim
    print('Time Elapsed:', end=' ',flush=True)
    print(elapTim,flush=True)
    return mean
    

#hits100_10_100=[]
#for i in range(100):
    #hits100_10_100.append(runProgram(100,75))
    

runProgram(1000,100)
runProgram(1000,100)