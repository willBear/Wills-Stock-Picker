import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from datetime import datetime


class TimeAxisItem(pg.AxisItem):
    def tickStrings(self, values, scale, spacing):
        return [datetime.fromtimestamp(value) for value in values]

list_x = [datetime(2018, 3, 1, 9, 36, 50, 136415), 
        datetime(2018, 3, 1, 9, 36, 51, 330912),
        datetime(2018, 3, 1, 9, 36, 51, 382815),
        datetime(2018, 3, 1, 9, 36, 52, 928818)]

for e in list:
    print('The type of element is '+ str(type(e))+ ' and its value is' + str(e))

list_y = [10, 9, 12, 11]

app = QtGui.QApplication([])

date_axis = TimeAxisItem(orientation='bottom')
graph = pg.PlotWidget(axisItems = {'bottom': date_axis})

graph.plot(x=[x.timestamp() for x in list_x], y=list_y, pen=None, symbol='o')
graph.show()

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()