#!/usr/bin/env python

from lib import graphql
from slides import tcga_breast
from breast import breast
from ssm import ssm
from pprint import pprint

"""
[{'case_id': 'dcd5860c-7e3a-44f3-a732-fe92fe3fe300',
  'demographic': {'days_to_death': None,
                  'ethnicity': 'not hispanic or latino',
                  'gender': 'female',
                  'race': 'white',
                  'vital_status': 'Alive'},
  'diagnoses': {'hits': {'edges': [{'node': {'age_at_diagnosis': 25158.0,
                                             'id': 'RURpYWdub3NpczpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA6YjIwM2VlZmEtNGM2NC01NDA3LTlhMDItMDBmYzc2ODU1ZGFl',
                                             'primary_diagnosis': 'Infiltrating '
                                                                  'duct '
                                                                  'carcinoma, '
                                                                  'NOS'}}]}},
  'disease_type': 'Ductal and Lobular Neoplasms',
  'id': 'RUNhc2U6ZGNkNTg2MGMtN2UzYS00NGYzLWE3MzItZmU5MmZlM2ZlMzAwIzg5YzhkNjBjODI5NTBlMzE1ZmMxMTIyZjViZDkyYWFlIw==',
  'primary_site': 'Breast',
  'project': {'id': 'UHJvamVjdDpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDAjODljOGQ2MGM4Mjk1MGUzMTVmYzExMjJmNWJkOTJhYWUjOl8=',
              'program': {'name': 'TCGA'},
              'project_id': 'TCGA-BRCA'},
  'score': 4351,
  'submitter_id': 'TCGA-AN-A046',
"""

if __name__ == "__main__":
    from collections import defaultdict
    genes = defaultdict(list)
    r = graphql(breast())
    data = [x["node"] for x in r.json()["data"]["exploreCasesTableViewer"]["explore"]["cases"]["hits"]["edges"]]
    for node in data:
        case = node["submitter_id"]
        uuid = node["case_id"]
        r = graphql(ssm(uuid))
        # TODO: move this loop to a helper
        for outer in r.json()["data"]["viewer"]["explore"]["ssms"]["hits"]["edges"]:
            for inner in outer["node"]["consequence"]["hits"]["edges"]:
                symbol = inner["node"]["transcript"]["gene"]["symbol"]
                genes[symbol].append(case)

    for k, v in sorted(genes.items()):
        print(f"{k} ({len(v)}) = {' '.join(v)}")
