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
df.insert(0, "id", ["gbm:"+str(x) for x in df.index])
df.to_csv(output, sep="\t", index=False)
