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

homo_ol_data=Dataset(homo_ol_file)
hete_ol_data=Dataset(hete_ol_file)

homo_h_data=Dataset(homo_h_file)
hete_h_data=Dataset(hete_h_file)

homo_hk_data=Dataset(homo_hk_file)
hete_hk_data=Dataset(hete_hk_file)

homo_hs_h_data=Dataset(homo_hs_h_file)
hete_hs_h_data=Dataset(hete_hs_h_file)

homo_hs_hs_data=Dataset(homo_hs_hs_file)
hete_hs_hs_data=Dataset(hete_hs_hs_file)

homo_hs_s_data=Dataset(homo_hs_s_file)
hete_hs_s_data=Dataset(hete_hs_s_file)


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

# Loop over 8 observations

for j in range(0,nobs):
  title='obs_'+str(j+1)
  obs_head=obs_data.variables['Head'][:,j]
  head_homo_ol=homo_ol_data.variables['head_f'][:,id_obs[j]-1]
  head_hete_ol=hete_ol_data.variables['head_f'][:,id_obs[j]-1]
  head_homo_h=homo_h_data.variables['head_f'][:,id_obs[j]-1]
  head_hete_h=hete_h_data.variables['head_f'][:,id_obs[j]-1]
  head_homo_hk=homo_hk_data.variables['head_f'][:,id_obs[j]-1]
  head_hete_hk=hete_hk_data.variables['head_f'][:,id_obs[j]-1]
  head_homo_hs_h=homo_hs_h_data.variables['head_f'][:,id_obs[j]-1]
  head_hete_hs_h=hete_hs_h_data.variables['head_f'][:,id_obs[j]-1]
  head_homo_hs_hs=homo_hs_hs_data.variables['head_f'][:,id_obs[j]-1]
  head_hete_hs_hs=hete_hs_hs_data.variables['head_f'][:,id_obs[j]-1]
  head_homo_hs_s=homo_hs_s_data.variables['head_f'][:,id_obs[j]-1]
  head_hete_hs_s=hete_hs_s_data.variables['head_f'][:,id_obs[j]-1]

  t=np.arange(0,95,1)
  fig=plt.figure()
  plt.plot(t,obs_head,label='obs')
  plt.plot(t,head_homo_ol,label='homo_no_DA')
  plt.plot(t,head_hete_ol,label='hete_no_DA')
  plt.plot(t,head_homo_h,label='homo_DA_h')
  plt.plot(t,head_hete_h,label='hete_DA_h')
  plt.plot(t,head_homo_hk,label='homo_DA_hK')
  #plt.plot(t,head_hete_hk,label='hete_DA_hK')
  #plt.plot(t,head_homo_hs_h,label='homo_DA_hs_h')
  #plt.plot(t,head_hete_hs_h,label='hete_DA_hs_h')
  #plt.plot(t,head_homo_hs_hs,label='homo_DA_hs_hs')
  #plt.plot(t,head_hete_hs_hs,label='hete_DA_hs_hs')
  #plt.plot(t,head_homo_hs_s,label='homo_DA_hs_s')
  #plt.plot(t,head_hete_hs_s,label='hete_DA_hs_s')

  plt.title(title)
  plt.legend()
  plt.tight_layout()
  #plt.show()
  fig_title='obs_fore_'+str(j+1)
  plt.savefig(fig_title,dpi=800,bbox_inches='tight')












