# Geometric_data_Analysis

### Library for different geometrical data applicaiton

<p>Most of these techniques and algorithms have been featured as part of homeworks or assignements when taking the course 02580 - Geometric Data Analysis and Processing at DTU</p>

**setup**:

list of dependencies and version: `python3.9 + `, `numpy `,`pandas ` 

`pygel3d` The featured workflows are heavily reliant on pygel3d for processing the mesh


**structure of the repo**

`root` : python files and walkthrough (descriptions of each file in the contents section) 

`./data/` : Some example geometry files 


**Usage**

Running a flow somtimes requires a run mode (integer number), whether a worflow has multiple modes can be noted from the contents and description section (flows that have (1), (2)... numbering)

a geometry file (unless specified otherwise in the contents description of the operation)

Some flows require two meshes (like in the case of registration with the ICP algorithm)

```
python3 <script> <optional run mode> <mesh> <optional mesh2>
```


**contents and description**

<ul>  
<li>smoothing_and_dual.py: (1) Laplacian smoothing of trinagle mesh, (2) dual of a triangle mesh. Also computes volume of triangle mesh</li>
<li>registration_icp.py : Iterative closest point using the Kabsh algorithm, requires 2 mesh file for reconstruciton. Provides convergence results and plots of the algorithm. </li> 

	The implementation also uses kdtree for the icp part of the algorithm

<li>delauny_triangulation.py: (1) only features 2d deulauny triangulation</li> 