from pygel3d import hmesh, jupyter_display as jd
import numpy as np
from scipy.spatial import KDTree
from numpy.linalg import norm,det
from scipy.linalg import eigh,solve,lstsq,svd
from itertools import permutations,combinations
from math import tan,acos,cos,sqrt,exp
from random import random
from time import sleep
import plotly.offline as py
import plotly.graph_objs as go

jd.set_export_mode(True)


#py.init_notebook_mode(connected=False) #useful when using jupyter notebook

#  A set of points
#  points are in a 10x2 numpy array where, rows are x's and columns are y's
ORIG_PTS = array([[1.21,2.21],[0.91,2.84],[1.81,1.21],[2.102,-.908],[2.741,-2.53],
                  [3.19,-2.31],[3.938,-1.519],[4.183,-1.1092],[5.11,1.44],[5.92,2.31]])


