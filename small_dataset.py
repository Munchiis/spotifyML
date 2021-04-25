import os,glob
import pandas as pd

path = "C:/Users/Fayr/Documents/GitHub/spotifyML/datasets"
files = glob.glob(os.path.join(path, '*.csv'))

df_from_each_file = (pd.read_csv(f, sep=',').iloc[0:30, :] for f in files)

df_merged = pd.concat(df_from_each_file, ignore_index=True)
df_merged.to_csv("small.csv")