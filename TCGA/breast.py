#!/usr/bin/env python

from lib import graphql
from lib import convert_to_rich_table
import pandas as pd
from pprint import pprint
from rich import print as rpprint


# https://portal.gdc.cancer.gov/exploration?filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22content%22%3A%7B%22field%22%3A%22cases.diagnoses.tissue_or_organ_of_origin%22%2C%22value%22%3A%5B%22axillary%20tail%20of%20breast%22%2C%22breast%2C%20nos%22%2C%22central%20portion%20of%20breast%22%2C%22lower-inner%20quadrant%20of%20breast%22%2C%22lower-outer%20quadrant%20of%20breast%22%2C%22nipple%22%2C%22overlapping%20lesion%20of%20breast%22%2C%22upper-inner%20quadrant%20of%20breast%22%2C%22upper-outer%20quadrant%20of%20breast%22%5D%7D%2C%22op%22%3A%22in%22%7D%2C%7B%22content%22%3A%7B%22field%22%3A%22cases.primary_site%22%2C%22value%22%3A%5B%22breast%22%5D%7D%2C%22op%22%3A%22in%22%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22TCGA%22%5D%7D%7D%5D%7D
payload = {
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
    "variables":{"filters":{"op":"and","content":[{"content":{"field":"cases.diagnoses.tissue_or_organ_of_origin","value":["axillary tail of breast","breast, nos","central portion of breast","lower-inner quadrant of breast","lower-outer quadrant of breast","nipple","overlapping lesion of breast","upper-inner quadrant of breast","upper-outer quadrant of breast"]},"op":"in"},{"content":{"field":"cases.primary_site","value":["breast"]},"op":"in"},{"op":"in","content":{"field":"cases.project.program.name","value":["TCGA"]}}]},"cases_size":20,"cases_offset":0,"cases_score":"gene.gene_id","cases_sort":[]}}

r = graphql(payload)
data = [x["node"] for x in r.json()["data"]["exploreCasesTableViewer"]["explore"]["cases"]["hits"]["edges"]]
pprint(data)
#df = pd.DataFrame(data)
#pprint(convert_to_rich_table(df))
