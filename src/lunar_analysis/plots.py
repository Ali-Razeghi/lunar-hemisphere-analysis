from pathlib import Path
import numpy as np, matplotlib.pyplot as plt
from .coordinates import hemisphere_masks

def elevation_histogram(z,lon,lat,out:Path):
    LON=np.broadcast_to(lon,(len(lat),len(lon))); near,far=hemisphere_masks(LON)
    fig,ax=plt.subplots(figsize=(9,5.5))
    finite=z[np.isfinite(z)]; bins=np.linspace(np.percentile(finite,.5),np.percentile(finite,99.5),80)
    ax.hist(z[near].ravel(),bins=bins,density=True,alpha=.5,label="Near side")
    ax.hist(z[far].ravel(),bins=bins,density=True,alpha=.5,label="Far side")
    ax.set(xlabel="Elevation (m)",ylabel="Probability density",title="LOLA near-side vs far-side elevation")
    ax.legend(); fig.tight_layout(); fig.savefig(out,dpi=180); plt.close(fig)

def crater_csfd(df,out:Path):
    near,far=hemisphere_masks(df.lon_deg.to_numpy())
    th=np.logspace(0,np.log10(max(20,df.diameter_km.max())),80)
    area=2*np.pi*1737.4**2
    fig,ax=plt.subplots(figsize=(8,6))
    for name,m in [("Near side",near),("Far side",far)]:
        d=df.diameter_km.to_numpy()[m]
        y=np.array([np.sum(d>=x)/area for x in th])
        ax.loglog(th,y,label=name)
    ax.set(xlabel="Diameter threshold D (km)",ylabel="Cumulative density N(≥D) / km²",
           title="Lunar crater cumulative size-frequency distribution")
    ax.legend(); fig.tight_layout(); fig.savefig(out,dpi=180); plt.close(fig)
