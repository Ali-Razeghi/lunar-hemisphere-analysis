from pathlib import Path
import numpy as np, rasterio
from rasterio.enums import Resampling
from .coordinates import hemisphere_masks

def inspect_dem(path:Path):
    with rasterio.open(path) as s:
        return {"width":s.width,"height":s.height,"dtype":s.dtypes[0],
                "bounds":[s.bounds.left,s.bounds.bottom,s.bounds.right,s.bounds.top],
                "transform":list(s.transform)[:6]}

def native_weighted_means(path:Path):
    sums={"near":0.,"far":0.}; ws={"near":0.,"far":0.}; ns={"near":0,"far":0}
    with rasterio.open(path) as s:
        for _,win in s.block_windows(1):
            z=s.read(1,window=win).astype(float)
            rr=np.arange(win.row_off,win.row_off+win.height)
            cc=np.arange(win.col_off,win.col_off+win.width)
            lon=s.transform.c+(cc+.5)*s.transform.a
            lat=s.transform.f+(rr+.5)*s.transform.e
            LON,LAT=np.meshgrid(lon,lat)
            near,far=hemisphere_masks(LON); valid=np.isfinite(z)
            weight=np.cos(np.radians(LAT))
            for name,mask in (("near",near),("far",far)):
                m=mask&valid
                sums[name]+=np.sum(z[m]*weight[m]); ws[name]+=np.sum(weight[m]); ns[name]+=m.sum()
    return {k:{"weighted_mean_m":float(sums[k]/ws[k]),"pixel_count":int(ns[k])} for k in sums}

def sample_dem(path:Path,max_width=1440):
    with rasterio.open(path) as s:
        scale=min(1,max_width/s.width); W=int(s.width*scale); H=int(s.height*scale)
        z=s.read(1,out_shape=(H,W),resampling=Resampling.average).astype(float)
        t=s.transform*s.transform.scale(s.width/W,s.height/H)
        lon=t.c+(np.arange(W)+.5)*t.a; lat=t.f+(np.arange(H)+.5)*t.e
        return z,lon,lat
