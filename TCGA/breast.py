#!/usr/bin/env python

from lib import graphql
from lib import convert_to_rich_table
import pandas as pd
from pprint import pprint
from rich import print as rpprint


# https://portal.gdc.cancer.gov/exploration?filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22content%22%3A%7B%22field%22%3A%22cases.diagnoses.tissue_or_organ_of_origin%22%2C%22value%22%3A%5B%22axillary%20tail%20of%20breast%22%2C%22breast%2C%20nos%22%2C%22central%20portion%20of%20breast%22%2C%22lower-inner%20quadrant%20of%20breast%22%2C%22lower-outer%20quadrant%20of%20breast%22%2C%22nipple%22%2C%22overlapping%20lesion%20of%20breast%22%2C%22upper-inner%20quadrant%20of%20breast%22%2C%22upper-outer%20quadrant%20of%20breast%22%5D%7D%2C%22op%22%3A%22in%22%7D%2C%7B%22content%22%3A%7B%22field%22%3A%22cases.primary_site%22%2C%22value%22%3A%5B%22breast%22%5D%7D%2C%22op%22%3A%22in%22%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22TCGA%22%5D%7D%7D%5D%7D
def breast():
    return {
        "query": """

query ExploreCasesTable_relayQuery(
  $filters: FiltersArgument
  $cases_size: Int
  $cases_offset: Int
  $cases_score: String
  $cases_sort: [Sort]
) {
  exploreCasesTableViewer: viewer {
    explore {
      cases {
        hits(
          first: $cases_size
          offset: $cases_offset
          filters: $filters
          score: $cases_score
          sort: $cases_sort
        ) {
          total
          edges {
            node {
              score
              id
              case_id
              primary_site
              disease_type
              submitter_id
              project {
                project_id
                program {
                  name
                }
                id
              }
              diagnoses {
                hits(first: 1) {
                  edges {
                    node {
                      primary_diagnosis
                      age_at_diagnosis
                      id
                    }
                  }
                }
              }
              demographic {
                gender
                ethnicity
                race
                days_to_death
                vital_status
              }
              summary {
                data_categories {
                  file_count
                  data_category
                }
                experimental_strategies {
                  experimental_strategy
                  file_count
                }
                file_count
              }
            }
          }
        }
      }
    }
  }
}""",
        "variables": {
            "filters": {
                "op": "and",
                "content": [
                    {
                        "content": {
                            "field": "cases.diagnoses.tissue_or_organ_of_origin",
                            "value": [
                                "axillary tail of breast",
                                "breast, nos",
                                "central portion of breast",
                                "lower-inner quadrant of breast",
                                "lower-outer quadrant of breast",
                                "nipple",
                                "overlapping lesion of breast",
                                "upper-inner quadrant of breast",
                                "upper-outer quadrant of breast",
                            ],
                        },
                        "op": "in",
                    },
                    {
                        "content": {"field": "cases.primary_site", "value": ["breast"]},
                        "op": "in",
                    },
                    {
                        "op": "in",
                        "content": {
                            "field": "cases.project.program.name",
                            "value": ["TCGA"],
                        },
                    },
                ],
            },
            "cases_size": 20,
            "cases_offset": 0,
            "cases_score": "gene.gene_id",
            "cases_sort": [],
        },
    }


def breast_rows():
    r = graphql(breast())
    for x in r.json()["data"]["exploreCasesTableViewer"]["explore"]["cases"]["hits"][
        "edges"
    ]:
        example = {
            "case_id": "f45aa0b2-f3de-4db5-9730-e5c6c4e2ed3a",
            "demographic": {
                "days_to_death": None,
                "ethnicity": "hispanic or latino",
                "gender": "female",
                "race": "white",
                "vital_status": "Alive",
            },
            "diagnoses": {
                "hits": {
                    "edges": [
                        {
                            "node": {
                                "age_at_diagnosis": 14316.0,
                                "id": "RURpYWdub3NpczpmNDVhYTBiMi1mM2RlLTRkYjUtOTczMC1lNWM2YzRlMmVkM2E6Mjg4ZWJkNWMtYTZlZi01M2M3LWEyMjMtYzY5Y2RiOWUwNDdh",
                                "primary_diagnosis": "Intraductal micropapillary carcinoma",
                            }
                        }
                    ]
                }
            },
            "disease_type": "Ductal and Lobular Neoplasms",
            "id": "RUNhc2U6ZjQ1YWEwYjItZjNkZS00ZGI1LTk3MzAtZTVjNmM0ZTJlZDNhIzg5YzhkNjBjODI5NTBlMzE1ZmMxMTIyZjViZDkyYWFlIw==",
            "primary_site": "Breast",
            "project": {
                "id": "UHJvamVjdDpmNDVhYTBiMi1mM2RlLTRkYjUtOTczMC1lNWM2YzRlMmVkM2EjODljOGQ2MGM4Mjk1MGUzMTVmYzExMjJmNWJkOTJhYWUjOl8=",
                "program": {"name": "TCGA"},
                "project_id": "TCGA-BRCA",
            },
            "score": 432,
            "submitter_id": "TCGA-EW-A2FV",
            "summary": {
                "data_categories": [
                    {"data_category": "Structural Variation", "file_count": 4.0},
                    {
                        "data_category": "Simple Nucleotide Variation",
                        "file_count": 17.0,
                    },
                    {"data_category": "Copy Number Variation", "file_count": 6.0},
                    {"data_category": "Transcriptome Profiling", "file_count": 4.0},
                    {"data_category": "DNA Methylation", "file_count": 3.0},
                    {"data_category": "Sequencing Reads", "file_count": 6.0},
                    {"data_category": "Biospecimen", "file_count": 14.0},
                    {"data_category": "Clinical", "file_count": 10.0},
                    {"data_category": "Proteome Profiling", "file_count": 1.0},
                ],
                "experimental_strategies": [
                    {"experimental_strategy": "RNA-Seq", "file_count": 9.0},
                    {"experimental_strategy": "WXS", "file_count": 19.0},
                    {"experimental_strategy": "miRNA-Seq", "file_count": 3.0},
                    {"experimental_strategy": "Genotyping Array", "file_count": 6.0},
                    {"experimental_strategy": "Methylation Array", "file_count": 3.0},
                    {"experimental_strategy": "Diagnostic Slide", "file_count": 1.0},
                    {"experimental_strategy": "Tissue Slide", "file_count": 1.0},
                    {
                        "experimental_strategy": "Reverse Phase Protein Array",
                        "file_count": 1.0,
                    },
                ],
                "file_count": 65.0,
            },
        }
        yield x["node"]
    target = {
        "case": None,
        "case_uuid": None,
        "slide": None,
        "number": None,
        "project": None,
        "project_name": None,
        "location": None,
        "date": None,
        "file_uuid": None,
        "program": None,
    }


if __name__ == "__main__":
    for row in breast_rows():
        print(row)
