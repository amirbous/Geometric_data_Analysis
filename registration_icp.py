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

import sys


'''
ICP implementation
	- compute_tranform: computes optimal transformation between 2 sets of points P0 and P1
	- tranform_mesh: applies a tranformation to a mesh m0
		tranformation is described by the 2 center of masses P0m and P1m and rotation R
'''
# function that computes optimal transformation from one set to the other
# takes set of points p0, and set of points p1

def compute_transform(P0, P1):
    P0m = np.mean(P0, axis=0)
    P1m = np.mean(P1, axis=0)
    
    # Center the data
    P0_centered = P0 - P0m
    P1_centered = P1 - P1m
    
    # Compute covariance matrix
    H = np.dot(P0_centered.T, P1_centered)
    
    # Perform singular value decomposition
    U, S, Vt = np.linalg.svd(H)
    
    # Compute optimal rotation matrix
    R = np.dot(U, Vt.T)
    
    return P0m, P1m, R


# applies tranformation to a matrix 

def transform_mesh(m, P0m, P1m, R):

    # Translate the mesh back
    translation_vector = P1m - np.dot(P0m, R)
    
    # Update mesh vertices
    m.positions()[:] = np.dot(P0m, R) + translation_vector

'''
	Main routine
'''

mesh_file0 = sys.argv[1]
mesh_file1 = sys.argv[2]


# reading original mesh
print("reading first mesh")
m0 = hmesh.load(getcwd() + "/" + mesh_file0)
m1 = hmesh.load(getcwd() + "/" + mesh_file1)



print("starting the ICP algorithm")
pos0 = m0.positions()
pos1 = m1.positions()
tree = KDTree(pos1)


max_iter = 50

max_convergence_itern = 5

# preallocating error vector
E = np.zeros(max_iter)

for i in range(max_iter):
    
    # finding closest points
    _, idx = tree.query(pos0)
    
    # computing optimal tranformation
    P0_matched = pos0
    P1_matched = pos1[idx]
    P0m, P1m, R = compute_transform(P0_matched, P1_matched)
    
    # applying tranformation
    transform_mesh(m0, P0m, P1m, R)
    
    # evaluationg error
    E[i] = np.mean(np.linalg.norm(P0_matched - P1_matched, axis=0))







