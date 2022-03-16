#!/usr/bin/env python

from lib import graphql
from lib import convert_to_rich_table
import pandas as pd
from collections import defaultdict
from pprint import pprint
from rich import print as rprint


#!/usr/bin/env python

# page 4 from https://static-content.springer.com/esm/art%3A10.1038%2Fs41598-021-83913-7/MediaObjects/41598_2021_83913_MOESM1_ESM.pdf

data = """\
TCGA.EW.A3U0, TCGA.D8.A27M, TCGA.C8.A26X, TCGA.A2.A0CM; PIKFYVE high UNS, UNS, LAR, IM
TCGA.S3.AA10, TCGA.EW.A1PB, TCGA.GM.A3XL, TCGA.GM.A2DD; LAMB2 high IM, IM, IM, LAR
TCGA.EW.A3U0, TCGA.GM.A3XL, TCGA.OL.A5D7; PKD1 high UNS, IM, IM
TCGA.AO.A128, TCGA.AR.A0TS, TCGA.AQ.A04J; CREBBP high IM, BL1, MSL
TCGA.EW.A1PB, TCGA.E2.A1L7, TCGA.BH.A0RX; RGPD4 high IM, NA, NA
TCGA.D8.A27M, TCGA.OL.A66P, TCGA.E2.A1B6; IGHV2-70 high UNS, LAR, IM
TCGA.D8.A27M, TCGA.C8.A26X, TCGA.GM.A2DD; GGA1 high UNS, LAR, LAR
TCGA.D8.A27M, TCGA.E2.A1L7, TCGA.A2.A0SX; ATP9A high UNS, NA, BL2
TCGA.AO.A128, TCGA.GM.A2DH, TCGA.AR.A1AQ; ATG2B high IM, UNS, IM
TCGA.AO.A128, TCGA.A2.A04T, TCGA.AR.A1AQ; ZNF697 high IM, BL1, IM
TCGA.E2.A159, TCGA.EW.A1OV, TCGA.A2.A04T; SYBU high BL2, UNS, BL1
TCGA.AO.A128, TCGA.EW.A3U0, TCGA.OL.A66P; RALGAPA2 high IM, UNS, LAR
TCGA.D8.A27M, TCGA.GM.A3XL, TCGA.LL.A441; PPP1R3F high UNS, IM, MSL
TCGA.E2.A159, TCGA.EW.A1OV, TCGA.GM.A2DI; HIST1H2BC high BL2, UNS, NA"""

sample_to_genes = defaultdict(list)
for line in data.split("\n"):
    samples, rest = line.split(";")
    samples = [x.strip().replace(".","-") for x in samples.split(",")]
    rest = [x.strip() for x in rest.strip().split(" ")]
    for sample in samples:
        sample_to_genes[sample].append(rest[0])


omitted_fields = """
              score
              id
              case_id
              primary_site
              disease_type
"""
payload = {
    "query": """
query CaseFileCounts($filters: FiltersArgument) {
  viewer {
    repository {
      cases {
        hits(filters: $filters) {
          edges {
            node {
              submitter_id
              summary {
                experimental_strategies {
                  experimental_strategy
                  file_count
                }
              }
            }
          }
        }
      }
    }
  }
}""",

    "variable": {"filters":{"op":"in","content":{"field":"cases.submitter_id","value":["FILL-ME"]}}}
}

tbl = []
for sample in sample_to_genes:
    payload["variable"]["filters"]["content"]["value"] = sample
    r = graphql(payload)
    for x in r.json()["data"]["viewer"]["repository"]["cases"]["hits"]["edges"]:
        row = x["node"]
        row["Genes"] = sample_to_genes[sample]
        summary = row.pop("summary")
        if summary:
            for strategy in summary.get("experimental_strategies", []):
                if strategy.get("experimental_strategy") == "Tissue Slide":
                    row["Slides"] = strategy.get("file_count", "NA")
        tbl.append(row)
df = pd.DataFrame(tbl)
rprint(convert_to_rich_table(df))
