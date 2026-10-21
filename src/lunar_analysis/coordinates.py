import numpy as np
def wrap_longitude(lon):
    return ((np.asarray(lon,dtype=float)+180)%360)-180
def hemisphere_masks(lon):
    x=wrap_longitude(lon); near=np.abs(x)<=90
    return near,~near
def angular_distance_deg(lat1,lon1,lat2,lon2):
    p1,p2=np.radians(lat1),np.radians(lat2)
    dl=np.radians(((np.asarray(lon1)-lon2+180)%360)-180)
    c=np.sin(p1)*np.sin(p2)+np.cos(p1)*np.cos(p2)*np.cos(dl)
    return np.degrees(np.arccos(np.clip(c,-1,1)))
