import numpy as np
from lunar_analysis.coordinates import wrap_longitude,hemisphere_masks
def test_wrap():
    assert np.allclose(wrap_longitude([0,90,180,270,360]),[0,90,-180,-90,0])
def test_hemispheres_0360():
    n,f=hemisphere_masks([0,89,91,180,270])
    assert n.tolist()==[True,True,False,False,True]
