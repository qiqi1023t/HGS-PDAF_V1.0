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

homo_ol_data=Dataset(homo_ol_file)
hete_ol_data=Dataset(hete_ol_file)

homo_h_data=Dataset(homo_h_file)
hete_h_data=Dataset(hete_h_file)

homo_hk_data=Dataset(homo_hk_file)
hete_hk_data=Dataset(hete_hk_file)

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

diff_homo_ol=np.zeros((nsteps,nobs))
diff_hete_ol=np.zeros((nsteps,nobs))
diff_homo_h=np.zeros((nsteps,nobs))
diff_hete_h=np.zeros((nsteps,nobs))
diff_homo_hk=np.zeros((nsteps,nobs))
diff_hete_hk=np.zeros((nsteps,nobs))

for j in range(0,nobs):
  title='avg_abs(forecast-obs)'
  obs_head=obs_data.variables['Head'][0:nsteps,j]
  head_homo_ol=homo_ol_data.variables['head_f'][0:nsteps,id_obs[j]-1]
  head_hete_ol=hete_ol_data.variables['head_f'][0:nsteps,id_obs[j]-1]
  head_homo_h=homo_h_data.variables['head_f'][0:nsteps,id_obs[j]-1]
  head_hete_h=hete_h_data.variables['head_f'][0:nsteps,id_obs[j]-1]
  head_homo_hk=homo_hk_data.variables['head_f'][0:nsteps,id_obs[j]-1]
  head_hete_hk=hete_hk_data.variables['head_f'][0:nsteps,id_obs[j]-1]
  diff_homo_ol[:,j]=np.abs(head_homo_ol-obs_head)
  diff_hete_ol[:,j]=np.abs(head_hete_ol-obs_head)
  diff_homo_h[:,j]=np.abs(head_homo_h-obs_head)
  diff_hete_h[:,j]=np.abs(head_hete_h-obs_head)
  diff_homo_hk[:,j]=np.abs(head_homo_hk-obs_head)
  diff_hete_hk[:,j]=np.abs(head_hete_hk-obs_head)

#yverage over nobs
avg_diff_homo_ol=np.average(diff_homo_ol,1)
avg_diff_hete_ol=np.average(diff_hete_ol,1)
avg_diff_homo_h=np.average(diff_homo_h,1)
avg_diff_hete_h=np.average(diff_hete_h,1)
avg_diff_homo_hk=np.average(diff_homo_hk,1)
avg_diff_hete_hk=np.average(diff_hete_hk,1)

t=np.arange(0,nsteps,1)
fig=plt.figure()
plt.plot(t,avg_diff_homo_ol,label='homo_no_DA')
plt.plot(t,avg_diff_hete_ol,label='hete_no_DA')
plt.plot(t,avg_diff_homo_h,label='homo_DA_h')
plt.plot(t,avg_diff_hete_h,label='hete_DA_h')
plt.plot(t,avg_diff_homo_hk,label='homo_DA_hk')
plt.plot(t,avg_diff_hete_hk,label='hete_DA_hk')
plt.title(title)
plt.legend()
plt.tight_layout()
#plt.show()
fig_title='avg_abs(forecast-obs)'
plt.savefig(fig_title,dpi=800,bbox_inches='tight')
