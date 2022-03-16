#!/usr/bin/env python

import json
import requests
import pandas as pd
from rich.table import Table


GRAPHQL_API = "https://api.gdc.cancer.gov/v0/graphql"


# Replace with rich-tools
def convert_to_rich_table(data_table: pd.DataFrame) -> "Table":
    table = Table(show_header=True, header_style="bold green")
    for column in data_table.columns:
        table.add_column(column)

    for row in range(len(data_table)):
        row = [str(i) for i in data_table.iloc[row, :].values.tolist()]
        table.add_row(*row)

    return table


def graphql(payload):
    return requests.post(GRAPHQL_API, json=payload)
