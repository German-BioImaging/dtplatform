#!/usr/bin/env python

from lib import graphql
from pprint import pprint

# https://portal.gdc.cancer.gov/cases/f45aa0b2-f3de-4db5-9730-e5c6c4e2ed3a
def ssm(case_id):
    return {
        "id": "ssm",
        "query": """
    query SsmsTable_relayQuery(
  $ssmTested: FiltersArgument
  $ssmCaseFilter: FiltersArgument
  $ssmsTable_size: Int
  $consequenceFilters: FiltersArgument
  $ssmsTable_offset: Int
  $ssmsTable_filters: FiltersArgument
  $score: String
  $sort: [Sort]
) {
  viewer {
    explore {
      cases {
        hits(first: 0, filters: $ssmTested) {
          total
        }
      }
      filteredCases: cases {
        hits(first: 0, filters: $ssmCaseFilter) {
          total
        }
      }
      ssms {
        hits(
          first: $ssmsTable_size
          offset: $ssmsTable_offset
          filters: $ssmsTable_filters
          score: $score
          sort: $sort
        ) {
          total
          edges {
            node {
              id
              score
              genomic_dna_change
              mutation_subtype
              ssm_id
              consequence {
                hits(first: 1, filters: $consequenceFilters) {
                  edges {
                    node {
                      transcript {
                        is_canonical
                        annotation {
                          vep_impact
                          polyphen_impact
                          polyphen_score
                          sift_score
                          sift_impact
                        }
                        consequence_type
                        gene {
                          gene_id
                          symbol
                        }
                        aa_change
                      }
                      id
                    }
                  }
                }
              }
              filteredOccurences: occurrence {
                hits(first: 0, filters: $ssmCaseFilter) {
                  total
                }
              }
              occurrence {
                hits(first: 0, filters: $ssmTested) {
                  total
                }
              }
            }
          }
        }
      }
    }
  }
}
""",
        "variables": {
            "ssmTested": {
                "content": [
                    {
                        "content": {
                            "field": "cases.available_variation_data",
                            "value": ["ssm"],
                        },
                        "op": "in",
                    }
                ],
                "op": "and",
            },
            "ssmCaseFilter": {
                "content": [
                    {
                        "content": {
                            "field": "available_variation_data",
                            "value": ["ssm"],
                        },
                        "op": "in",
                    },
                    {
                        "content": {
                            "field": "cases.project.project_id",
                            "value": ["TCGA-BRCA"],
                        },
                        "op": "in",
                    },
                ],
                "op": "and",
            },
            "ssmsTable_size": 10,
            "consequenceFilters": {
                "content": [
                    {
                        "content": {
                            "field": "consequence.transcript.is_canonical",
                            "value": ["true"],
                        },
                        "op": "in",
                    }
                ],
                "op": "and",
            },
            "ssmsTable_offset": 0,
            "ssmsTable_filters": {
                "content": [
                    {
                        "content": {
                            "field": "cases.case_id",
                            "value": [case_id],
                        },
                        "op": "in",
                    }
                ],
                "op": "and",
            },
            "score": "occurrence.case.project.project_id",
            "sort": [
                {"field": "_score", "order": "desc"},
                {"field": "_uid", "order": "asc"},
            ],
        },
    }


if __name__ == "__main__":
    import sys

    for uuid in sys.argv[1:]:
        r = graphql(ssm(uuid))
        for outer in r.json()["data"]["viewer"]["explore"]["ssms"]["hits"]["edges"]:
            for inner in outer["node"]["consequence"]["hits"]["edges"]:
                print(inner["node"]["transcript"]["gene"])
        example = """
                                                                     {'node': {'consequence': {'hits': {'edges': [{'node': {'id': 'U1NNQ29uc2VxdWVuY2U6MDVlMzk5ZWEtZTg4Zi01ZGQyLWFhNDUtYzY4NDI4MTY1MWVhOjUwYjg0NTgyLTdmNzItNWI0MC1iYmM4LWZiZGEwM2E4N2VlOA==',
                                                                                                                    'transcript': {'aa_change': 'K303Nfs*25',
                                                                                                                                   'annotation': {'polyphen_impact': '',
                                                                                                                                                  'polyphen_score': None,
                                                                                                                                                  'sift_impact': '',
                                                                                                                                                  'sift_score': None,
                                                                                                                                                  'vep_impact': 'HIGH'},
                                                                                                                                   'consequence_type': 'frameshift_variant',
                                                                                                                                   'gene': {'gene_id': 'ENSG00000149781',
                                                                                                                                            'symbol': 'FERMT3'},
                                                                                                                                   'is_canonical': True}}}]}},
                                                                       'filteredOccurences': {'hits': {'total': 1}},
                                                                       'genomic_dna_change': 'chr11:g.64219538delG',
                                                                       'id': 'U3NtOjA1ZTM5OWVhLWU4OGYtNWRkMi1hYTQ1LWM2ODQyODE2NTFlYSNmNWQxZDE4ZjVjYmQ4OGJhMjA4NGZkNGQ3OWU4YmZkMyM=',
                                                                       'mutation_subtype': 'Small '
                                                                                           'deletion',
                                                                       'occurrence': {'hits': {'total': 1}},
                                                                       'score': 1,
                                                                       'ssm_id': '05e399ea-e88f-5dd2-aa45-c684281651ea'}}],
                                                                       """
