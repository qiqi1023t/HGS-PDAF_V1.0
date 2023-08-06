#compare the free run between hete and homo

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
from matplotlib import cm
from netCDF4 import Dataset

# Read coordinates
coordinate_file='/p/home/jusers/tang1/jureca/dev_hgs-pdaf/postprocessing/write_coordinate/coordinates.dat'
coord_data=np.loadtxt(coordinate_file)

# model simulation
homo_ol_file='/p/home/jusers/tang1/jureca/dev_hgs-pdaf/run_scripts/jureca/work/n100_homo_ol/001/hgs-flow.da.nc'
hete_ol_file='/p/home/jusers/tang1/jureca/dev_hgs-pdaf/run_scripts/jureca/work/n100_hete_ol/001/hgs-flow.da.nc'

homo_h_file='/p/home/jusers/tang1/jureca/dev_hgs-pdaf/run_scripts/jureca/work/n100_homo_h_005/001/hgs-flow.da.nc'
hete_h_file='/p/home/jusers/tang1/jureca/dev_hgs-pdaf/run_scripts/jureca/work/n100_hete_h_005/001/hgs-flow.da.nc'

homo_hk_file='/p/home/jusers/tang1/jureca/dev_hgs-pdaf/run_scripts/jureca/work/n100_homo_hk_005/001/hgs-flow.da.nc'
hete_hk_file='/p/home/jusers/tang1/jusuf/dev_hgs-pdaf/run_scripts/jusuf/work/n100_hete_hk_h_damp0.9/001/hgs-flow.da.nc'

homo_hs_h_file='/p/home/jusers/tang1/jusuf/dev_hgs-pdaf/run_scripts/jusuf/work/n100_homo_hs_h/001/hgs-flow.da.nc'
hete_hs_h_file='/p/home/jusers/tang1/jusuf/dev_hgs-pdaf/run_scripts/jusuf/work/n100_hete_hs_h/001/hgs-flow.da.nc'

homo_hs_hs_file='/p/home/jusers/tang1/jusuf/dev_hgs-pdaf/run_scripts/jusuf/work/n100_homo_hs_hs/001/hgs-flow.da.nc'
hete_hs_hs_file='/p/home/jusers/tang1/jusuf/dev_hgs-pdaf/run_scripts/jusuf/work/n100_hete_hs_hs/001/hgs-flow.da.nc'

homo_hs_s_file='/p/home/jusers/tang1/jusuf/dev_hgs-pdaf/run_scripts/jusuf/work/n100_homo_hs_s/001/hgs-flow.da.nc'
hete_hs_s_file='/p/home/jusers/tang1/jusuf/dev_hgs-pdaf/run_scripts/jusuf/work/n100_hete_hs_s/001/hgs-flow.da.nc'

homo_hsk_hs_file='/p/home/jusers/tang1/jusuf/dev_hgs-pdaf/run_scripts/jusuf/work/n100_homo_hsk_hs/001/hgs-flow.da.nc'
hete_hsk_hs_file='/p/home/jusers/tang1/jusuf/dev_hgs-pdaf/run_scripts/jusuf/work/n100_hete_hsk_hs_damp0.02/001/hgs-flow.da.nc'

name_list=[homo_ol_file,hete_ol_file,homo_h_file,hete_h_file,homo_hs_h_file,hete_hs_h_file,homo_hs_hs_file,hete_hs_hs_file,homo_hs_s_file,hete_hs_s_file,homo_hk_file,hete_hk_file,homo_hsk_hs_file,hete_hsk_hs_file]


# observations
obs_file='/p/project/cjicg41/jicg4139/input_HGS-PDAF/observation/obs_HEAD.nc'
obs_data=Dataset(obs_file)

# select observation point
# read observation file
# read the number of observations
nobs=obs_data.dimensions['n_obs'].size
x=obs_data.variables['x'][:]
y=obs_data.variables['y'][:]
z=obs_data.variables['z'][:]
id_obs=obs_data.variables['obs_id'][:]
nsteps=95

diff=np.zeros((nsteps,nobs))

# Read model simulation

for file_name in name_list:
  print(file_name)
  fore=Dataset(file_name)
  sum=0
  cnt=0
  for j in range(0,nobs):
    obs=obs_data.variables['Head'][0:nsteps,j]
    sim=fore.variables['head_f'][0:nsteps,id_obs[j]-1]
    diff[:,j]=sim-obs
  rms=np.sqrt(np.mean(np.square(diff)))
  print(rms)











