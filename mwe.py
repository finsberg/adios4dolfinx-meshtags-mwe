from pathlib import Path
from mpi4py import MPI
import dolfinx
import adios4dolfinx


comm = MPI.COMM_WORLD
mesh = dolfinx.mesh.create_unit_cube(
    comm=comm,
    cell_type=dolfinx.mesh.CellType.tetrahedron,
    nx=3,
    ny=3,
    nz=3,
)

mesh.topology.create_connectivity(mesh.topology.dim - 2, mesh.topology.dim)
mesh_tags = dolfinx.mesh.meshtags(mesh, mesh.topology.dim - 2, [], [])

adios4dolfinx.write_meshtags(
    meshtags=mesh_tags,
    mesh=mesh,
    filename=Path("meshtags.bp"),
    meshtag_name="Edge tags",
)
