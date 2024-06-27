from pygel3d import hmesh, jupyter_display as jd
from numpy import zeros, unique
from numpy.linalg import det
from os import getcwd
import sys

#jd.set_export_mode(True) # useful in case of using jupyter



#helper function to display the number of faces and vertices in mesh
def mesh_stats(m):
	print("# faces : ", m.no_allocated_faces(), " # vertices : ", m.no_allocated_vertices())

#helper function to calculate the volumen of a triangle mesh
#uses an inner helper funciton to calculate volumne of triangle in space

def calculate_volume(m):
	#helper function: volume of triangle in space
	def triangle_volume(v1, v2, v3):
		v321 = v3[0] * v2[1] * v1[2]
		v231 = v2[0] * v3[1] * v1[2]
		v312 = v3[0] * v1[1] * v2[2] 
		v132 = v1[0] * v3[1] * v2[2]
		v213 = v2[0] * v1[1] * v3[2]
		v123 = v1[0] * v2[1] * v3[2]
		return (1.0/6.0) * (-v321 + v231 + v312 - v132 - v213 + v123)
	# main routine
	pos = m.positions()
	vol = 0
	for f in m.faces():
		f_v = m.circulate_face(f,mode='v')
		vol += triangle_volume(pos[f_v[0]],pos[f_v[1]],pos[f_v[2]])

	return vol   


'''
	1)
	Smoothing function using laplacian
	takes a pygel mesh object and max_iter the max number of iterations
'''
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
'''
	2)
	dual of a triangle mesh
	takes one pygel mesh object
'''
def dual(m):
	m2 = hmesh.Manifold()
	for v in m.vertices():
		new_vertices = zeros((len(m.circulate_vertex(v, 'f')), 3))
		for i, f in enumerate(m.circulate_vertex(v, 'f')):
			new_vertex = m.circulate_face(f, 'v')
			new_vertices[i] = (1/3) * (m.positions()[new_vertex[0]] + m.positions()[new_vertex[1]] + m.positions()[new_vertex[2]])
		m2.add_face(new_vertices)
	return m2

'''
main routine options 1-3

'''
#TODO: use argparse for parsing arguments

run_mode = int(sys.argv[1])
mesh_file = sys.argv[2]


# reading original mesh
print("reading mesh")
m = hmesh.load(getcwd() + mesh_file)
print("original mesh:")
mesh_stats(m)

#volume of the mesh
print(f"#Volume of the mesh: {calculate_volume(m)}")

if run_mode == 1:
	#smoothed mesh
	m_s = hmesh.Manifold(m)
	smooth(m_s, 1)
	print("smoothed mesh: ")
	mesh_stats(m_s)	
	print(f"#Volume of the smoothed mesh: {calculate_volume(m_s)}")
if run_mode == 2:
	#dual of the original mesh
	m_d = dual(m)
	print("dual of the mesh: ")
	mesh_stats(m_d)
	print("volume of a dual mesh not supported")


 
