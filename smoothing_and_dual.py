from pygel3d import hmesh, jupyter_display as jd
from numpy import zeros, unique
from numpy.linalg import det
from os import getcwd

#jd.set_export_mode(True) # useful in case of using jupyter

###################################
#        Defining funcitons       #
###################################

#helper function to display the number of faces and vertices in mesh
def mesh_stats(m):
    print("# faces : ", m.no_allocated_faces(), " # vertices : ", m.no_allocated_vertices())

# 1------> Smoothing function using laplacian
def smooth(m, max_iter=1):
    pos = m.positions()
    new_pos = zeros(pos.shape)
    for iter in range(0,max_iter):
        new_pos[:] = 0
        for v in m.vertices(): 
            for vn in m.circulate_vertex(v,'v'):
                new_pos[v] += pos[vn]
            new_pos[v] /= len(m.circulate_vertex(v,'v'))
        pos[:] = new_pos 

# 2------> volume of a triangle mesh (using signed volume of a triangle)
#helper function for the signed volume of a triangle
def triangle_volume(v1, v2, v3):
    v321 = v3[0] * v2[1] * v1[2]
    v231 = v2[0] * v3[1] * v1[2]
    v312 = v3[0] * v1[1] * v2[2] 
    v132 = v1[0] * v3[1] * v2[2]
    v213 = v2[0] * v1[1] * v3[2]
    v123 = v1[0] * v2[1] * v3[2]

    return (1.0/6.0) * (-v321 + v231 + v312 - v132 - v213 + v123)

def calculate_volume(m):
    pos = m.positions()
    vol = 0
    for f in m.faces():
        f_v = m.circulate_face(f,mode='v')
        vol += triangle_volume(pos[f_v[0]],pos[f_v[1]],pos[f_v[2]])

    return vol   

# 3------> dual of a triangle mesh
def dual(m):
    m2 = hmesh.Manifold()
        # Insert code ------>
    for v in m.vertices():
        new_vertices = zeros((len(m.circulate_vertex(v, 'f')), 3))
        for i, f in enumerate(m.circulate_vertex(v, 'f')):
            new_vertex = m.circulate_face(f, 'v')
            new_vertices[i] = (1/3) * (m.positions()[new_vertex[0]] + m.positions()[new_vertex[1]] + m.positions()[new_vertex[2]])
        m2.add_face(new_vertices)
        # <------------------
    return m2

###################################
#  loading and displaying results #
###################################

#original mesh
indir = "/data/"
m = hmesh.load(getcwd() + indir + "bunnytest.obj")
print("original mesh:")
mesh_stats(m)
#volume of the mesh
print(f"#Volume of the mesh: {calculate_volume(m)}")

#smoothed mesh
m_s = hmesh.Manifold(m)
smooth(m_s, 1)
print("smoothed mesh: ")
mesh_stats(m_s)

#dual of the original mesh

m_d = dual(m)
print("dual of the mesh: ")
mesh_stats(m_d)


 
