#Catherine Castagna
#Summer Fellows
#Discrete Independent Model Attempt 1

#! python
import sys, os
import time
import math
from numpy import random
from random import randint
import pyqtgraph as pg
import numpy as np


def configure_spark(spark_home=None, pyspark_python=None):
    spark_home = spark_home 
    os.environ['SPARK_HOME'] = spark_home

    # Add the PySpark directories to the Python path:
    sys.path.insert(1, os.path.join(spark_home, 'python'))
    sys.path.insert(1, os.path.join(spark_home, 'python', 'pyspark'))
    sys.path.insert(1, os.path.join(spark_home, 'python', 'build'))

    # If PySpark isn't specified, use currently running Python binary:
configure_spark('/Users/casta/AppData/Local/Programs/Python/Python36-32/Scripts')
pyspark_python = sys.executable

from pyspark import SparkContext, SparkConf



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
        #print(p2y[-1]
        
        if(math.sqrt((p1x[-1]-p2x[-1])**2+(p1y[-1]-p2y[-1])**2)<2):
            collided=True
            #grid[p2x[-1]][p2y[-1]]='X'
            #print("++++++++++++++++++++COLLIDED++++++++++++++++++++++++++")
        if(time>=size*size):
            never=True
        #printMat(grid,size)
        #print() 
    
    #plotWidget=pg.plot(title="Random Walk Paths of 2 Particles on "+str(len(grid))+" by "+str(len(grid))+" Grid")
    #pg.plot(p1x,p1y)#,connect='all',pen='r',symbol='o')
    #plotWidget.plot(p2x,p2y,connect='all',pen='b',symbol='x')        
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
    mean=np.mean(collTimes)   
    stand=np.std(collTimes)
    print('Collision Times:',end=' ',flush=True)
    print(collTimes)
    print('Average Collision Time:',end=' ',flush=True)
    print(mean)
    print('Std of Collision Times:',end=' ',flush=True)
    print(stand)    
    #hist=np.histogram(collTimes,bins=20)
    #print(hist)
    #pg.plot(hist[0],hist[1])
    #pg.ImageView(view=pg.PlotItem())
    #w.show()
    #w.setImage(hist)
    elapTim=time.clock()-elapTim
    print('Time Elapsed:', end=' ',flush=True)
    print(elapTim,flush=True)
    

runProgram(100,50)
#runProgram(3000,1)
#runProgram(4000,1)
