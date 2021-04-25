import os,glob
import pandas as pd

path = "C:/Users/jeche/Desktop/python/ML/Project_/spotifyML/"
files = glob.glob(os.path.join(path, '*.csv'))

df_from_each_file= (pd.read_csv(f, sep=',') for f in files)

df_merged = pd.concat(df_from_each_file, ignore_index=True)
df_merged.to_csv("top.csv")