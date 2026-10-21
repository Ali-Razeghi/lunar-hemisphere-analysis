import argparse,json
from pathlib import Path
from .dem import inspect_dem,native_weighted_means,sample_dem
from .craters import load_robbins,density_table
from .plots import elevation_histogram,crater_csfd

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--dem",type=Path,required=True)
    p.add_argument("--craters",type=Path)
    p.add_argument("--output-dir",type=Path,default=Path("outputs"))
    p.add_argument("--native-means",action="store_true")
    a=p.parse_args(); a.output_dir.mkdir(parents=True,exist_ok=True)
    result={"dem":inspect_dem(a.dem)}
    z,lon,lat=sample_dem(a.dem); elevation_histogram(z,lon,lat,a.output_dir/"elevation_histogram.png")
    if a.native_means: result["native_full_resolution"]=native_weighted_means(a.dem)
    if a.craters:
        df=load_robbins(a.craters); tab=density_table(df)
        tab.to_csv(a.output_dir/"hemisphere_crater_density.csv",index=False)
        crater_csfd(df,a.output_dir/"crater_csfd.png")
        result["crater_rows"]=len(df); result["crater_density"]=tab.to_dict("records")
    (a.output_dir/"analysis_summary.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
