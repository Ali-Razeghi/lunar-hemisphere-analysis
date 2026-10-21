from pathlib import Path
import numpy as np,pandas as pd
from .coordinates import hemisphere_masks
R=1737.4
HEMI_AREA=2*np.pi*R**2

def load_robbins(path:Path):
    df=pd.read_csv(path,low_memory=False)
    req=["LAT_CIRC_IMG","LON_CIRC_IMG","DIAM_CIRC_IMG"]
    miss=[c for c in req if c not in df.columns]
    if miss: raise ValueError(f"Missing Robbins columns: {miss}")
    return df[req].rename(columns={"LAT_CIRC_IMG":"lat_deg","LON_CIRC_IMG":"lon_deg",
        "DIAM_CIRC_IMG":"diameter_km"}).apply(pd.to_numeric,errors="coerce").dropna()

def density_table(df,thresholds=(1,2,5,20)):
    near,far=hemisphere_masks(df.lon_deg.to_numpy()); d=df.diameter_km.to_numpy()
    rows=[]
    for t in thresholds:
        n=int(np.sum(near&(d>=t))); f=int(np.sum(far&(d>=t)))
        rows.append({"min_diameter_km":t,"near_count":n,"far_count":f,
          "near_density_per_million_km2":n/HEMI_AREA*1e6,
          "far_density_per_million_km2":f/HEMI_AREA*1e6,
          "far_to_near_density_ratio":f/n})
    return pd.DataFrame(rows)
