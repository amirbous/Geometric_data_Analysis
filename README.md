# Geometric_data_Analysis

<p>This repo features a list of applications on triangular meshes</p>

**setup**:

list of dependencies and version: `python3.9 + `, `numpy `,`pandas ` 

`pygel3d` The featured workflows are heavily reliant on pygel3d for processing the mesh


**structure of the repo**

`root` : python files and walkthrough (descriptions of each file in the contents section) 

`./data/` : Some example geometry files 


**Usage**

Each flow (pyhton file), has different run modes which can be found in contents

Running a flow requires a run mode (integer number) and a geometry file (unless specified otherwise in the contents description of the operation)

Some flows require two meshes (like in the case of registration with the ICP algorithm)

```
python3 <script> <run mode> <mesh> <optional mesh2>
```


**contents and description**

<ul>  
<li>smoothing_and_dual.py: (1) Laplacian smoothing of trinagle mesh, (2) dual of a triangle mesh. Also computes volume of triangle mesh</li>
<li>registration_icp : (1) Iterative closest point using the Kabsh algorithm, requires 2 mesh file for reconstruciton. Provides convergence results and plots of the algorithm. 