import pandas as pd
from lunar_analysis.craters import density_table
def test_ratio():
    d=pd.DataFrame({"lat_deg":[0,0,0],"lon_deg":[0,180,200],"diameter_km":[10,10,10]})
    r=density_table(d,(5,)).iloc[0]
    assert r.near_count==1 and r.far_count==2 and r.far_to_near_density_ratio==2
