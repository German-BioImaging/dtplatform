import json
import numpy as np
import pandas as pd
import sys

input = sys.argv[1]
output = sys.argv[2]

columns = {
    "ID Lab site": "lab",
    "ID clinical site": "clinic",
    "DOB": "birth_date",
    "Age ": "age",  # Note: trailing whitespace
    "Gender": "gender",
}

# Lookup tables
labs = pd.read_csv("labs.tsv", sep="\t")
labs = {v: k for k, v in dict(labs.to_dict("split")["data"]).items()}
clinics = pd.read_csv("clinics.tsv", sep="\t")
clinics = {v: k for k, v in dict(clinics.to_dict("split")["data"]).items()}
lookups = {
    "lab": labs,
    "clinic": clinics,
}

df = pd.read_csv(input, sep="\t")
df = df.rename(columns = columns)
df = df.drop(columns=df.columns.symmetric_difference(set(columns.values())))

# Fix birthdates. Note: to_datetime, uses lots of 2000s!
birth_date = pd.to_datetime(df["birth_date"]).dt.date
mask = pd.DatetimeIndex(birth_date).year > 2022
reduced = birth_date - np.timedelta64(100, "Y")
df["birth_date"].loc[mask] = reduced[mask]
df["birth_date"].loc[~mask] = birth_date[~mask]

# Turn identifiers into CURIEs
df.insert(0, "id", ["gbm:"+str(x) for x in df.index])

# Replace from lookup tables
df = df.replace(lookups)

# Try to inline JSON
def make_properties(row):
    return json.dumps({
        "age": row["age"],
        "birth_date": str(row["birth_date"]),
        "gender": row["gender"]})

df["properties"] = df.apply(make_properties, axis=1)
df = df.drop(columns=["age", "birth_date", "gender"])

# Output
df.to_csv(output, sep="\t", index=False, escapechar='\\', doublequote=False)
