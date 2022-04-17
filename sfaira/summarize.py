#!/usr/bin/env python
from collections import defaultdict

count = 0
lookup = {}
print(f"datasets:")
for dataset, d in ds.datasets.items():
    print(f"  - dataset: '{dataset}'")
    lookup[dataset] = count
    count += 1

types = defaultdict(lambda: [0] * len(lookup))
for dataset, d in ds.datasets.items():
    cell_types = d.adata.obs["cell_type"].value_counts().to_dict()
    for cell_type, count in cell_types.items():
        types[cell_type][lookup[dataset]] += count

print(f"cell_types:")
for cell_type, datasets in sorted(types.items()):
    print(f"  - cell_type: '{cell_type}'")
    print(f"    datasets: {datasets}")
