#!/usr/bin/env python

import sfaira
import time
import os

# from https://github.com/theislab/sfaira_tutorials/blob/master/tutorials/data_loaders.ipynb

basedir = '.'
datadir = os.path.join(basedir, 'raw')
metadir = os.path.join(basedir, 'meta')
cachedir = os.path.join(basedir, 'cache')

start = time.time()
ds = sfaira.data.Universe(data_path=datadir, meta_path=metadir, cache_path=cachedir)
ds.subset(key="organism", values=["Homo sapiens"])
ds.subset(key="organ", values=["brain"])
ds.download()
ds.load(verbose=1)
ds.streamline_features(match_to_release="104", subset_genes_to_type="protein_coding")
ds.streamline_metadata(schema="sfaira")
print(ds.adata)
print(ds.ids)
for key in ds.datasets:
    print(key, ds.datasets[key].layer_counts, ds.datasets[key].annotated)
stop= time.time()

print(f"Took {stop-start} seconds")


print("now run summarize")
