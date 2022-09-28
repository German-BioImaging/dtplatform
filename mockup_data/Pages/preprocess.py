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

# Output
df.to_csv(output, sep="\t", index=False)
