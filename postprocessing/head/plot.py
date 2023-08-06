#compare the free run between hete and homo

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
from matplotlib import cm
from netCDF4 import Dataset
import vtk

# Read coordinates
coordinate_file='/p/home/jusers/tang1/jureca/dev_hgs-pdaf/postprocessing/write_coordinate/coordinates.dat'
coord_data=np.loadtxt(coordinate_file)

homo_file='/p/home/jusers/tang1/jureca/dev_hgs-pdaf/run_scripts/jureca/work/n100_homo_ol/001/hgs-flow.da.nc'
hete_file='/p/home/jusers/tang1/jureca/dev_hgs-pdaf/run_scripts/jureca/work/n100_hete_ol/001/hgs-flow.da.nc'

homo_data=Dataset(homo_file)
hete_data=Dataset(hete_file)

head_homo=homo_data.variables['head_f'][1,:]
head_hete=hete_data.variables['head_f'][1,:]

diff=np.abs(head_hete-head_homo)
print(np.mean(diff))
# Visualise the diff - map$

# Create 3D meshgrid
x,y,z=np.meshgrid(coord_data[:,0],coord_data[:,1],coord_data[:,2],sparse=True)
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.
ax.tricontourf(x, y, z, z, cmap=plt.cm.CMRmap)






