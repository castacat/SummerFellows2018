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

def plot_hist(x,b):
    pg.setConfigOption('background', 'w')
    pg.setConfigOption('foreground', 'k')

    app = QtGui.QApplication([])

    win = pg.GraphicsWindow(title="Collision Times Histogram")
    win.resize(800,600)

    current_plot = win.addPlot(title="Histogram")
    y,x = np.histogram(x, bins=b)
    curve = pg.PlotCurveItem(x, y, stepMode=True, fillLevel=0, brush=(0, 0, 255, 80))
    current_plot.addItem(curve)
    
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            app.exec_()    


collTime50=10
plot_hist(collTime2000,10)