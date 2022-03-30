#!/usr/bin/env python

from lib import graphql
from pprint import pprint


# https://portal.gdc.cancer.gov/repository?facetTab=files&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22TCGA%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22files.data_format%22%2C%22value%22%3A%5B%22svs%22%5D%7D%7D%5D%7D
def slides():
    return {
    "id": "q1",
    "query": """
query Queries($filters_0: FiltersArgument!, $first_1: Int!, $offset_2: Int!) {
  viewer {
    ...F2
  }
}
fragment F0 on CaseAggregations {
  demographic__ethnicity {
    buckets {
      doc_count
      key
    }
  }
  demographic__gender {
    buckets {
      doc_count
      key
    }
  }
  demographic__race {
    buckets {
      doc_count
      key
    }
  }
  demographic__vital_status {
    buckets {
      doc_count
      key
    }
  }
  disease_type {
    buckets {
      doc_count
      key
    }
  }
  primary_site {
    buckets {
      doc_count
      key
    }
  }
  project__project_id {
    buckets {
      doc_count
      key
    }
  }
  project__program__name {
    buckets {
      doc_count
      key
    }
  }
}
fragment F1 on FileAggregations {
  cases__project__project_id {
    buckets {
      doc_count
      key
    }
  }
  cases__primary_site {
    buckets {
      doc_count
      key
    }
  }
  data_category {
    buckets {
      doc_count
      key
    }
  }
  data_type {
    buckets {
      doc_count
      key
    }
  }
  experimental_strategy {
    buckets {
      doc_count
      key
    }
  }
  data_format {
    buckets {
      doc_count
      key
    }
  }
  access {
    buckets {
      doc_count
      key
    }
  }
}
fragment F2 on Root {
  cart_summary {
    _aggregations2IB88U: aggregations(filters: $filters_0) {
      fs {
        value
      }
    }
  }
  repository {
    cases {
      _aggregationsvROS: aggregations(
        filters: $filters_0
        aggregations_filter_themselves: true
      ) {
        ...F0
      }
      _hits80KmU: hits(
        score: "annotations.annotation_id"
        first: $first_1
        offset: $offset_2
        filters: $filters_0
      ) {
        total
      }
    }
    files {
      _aggregationsvROS: aggregations(
        filters: $filters_0
        aggregations_filter_themselves: true
      ) {
        ...F1
      }
      _hits3sJdUG: hits(
        first: $first_1
        offset: $offset_2
        filters: $filters_0
      ) {
        total
      }
    }
  }
}
""",
    "variables": {
        "filters_0": {
            "op": "and",
            "content": [
                {
                    "op": "in",
                    "content": {
                        "field": "cases.project.program.name",
                        "value": ["TCGA"],
                    },
                },
                {
                    "op": "in",
                    "content": {"field": "files.data_format", "value": ["svs"]},
                },
            ],
        },
        "first_1": 20,
        "offset_2": 0,
    },
}

# https://portal.gdc.cancer.gov/exploration?filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22content%22%3A%7B%22field%22%3A%22cases.diagnoses.tissue_or_organ_of_origin%22%2C%22value%22%3A%5B%22axillary%20tail%20of%20breast%22%2C%22breast%2C%20nos%22%2C%22central%20portion%20of%20breast%22%2C%22lower-inner%20quadrant%20of%20breast%22%2C%22lower-outer%20quadrant%20of%20breast%22%2C%22nipple%22%2C%22overlapping%20lesion%20of%20breast%22%2C%22upper-inner%20quadrant%20of%20breast%22%2C%22upper-outer%20quadrant%20of%20breast%22%5D%7D%2C%22op%22%3A%22in%22%7D%2C%7B%22content%22%3A%7B%22field%22%3A%22cases.primary_site%22%2C%22value%22%3A%5B%22breast%22%5D%7D%2C%22op%22%3A%22in%22%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22TCGA%22%5D%7D%7D%5D%7D
def tcga_breast():
    return {
    "id": "q1",
    "query": """
    query Queries($first_0: Int!, $offset_1: Int!, $filters_2: FiltersArgument!) {
  viewer {
    ...F1
  }
}
fragment F0 on SsmAggregations {
  consequence__transcript__annotation__vep_impact {
    buckets {
      doc_count
      key
    }
  }
  consequence__transcript__annotation__polyphen_impact {
    buckets {
      doc_count
      key
    }
  }
  consequence__transcript__annotation__sift_impact {
    buckets {
      doc_count
      key
    }
  }
  consequence__transcript__consequence_type {
    buckets {
      doc_count
      key
    }
  }
  mutation_subtype {
    buckets {
      doc_count
      key
    }
  }
  occurrence__case__observation__variant_calling__variant_caller {
    buckets {
      doc_count
      key
    }
  }
}
fragment F1 on Root {
  explore {
    cases {
      _hits1usPD9: hits(
        first: $first_0
        offset: $offset_1
        filters: $filters_2
        score: "gene.gene_id"
      ) {
        total
      }
    }
    genes {
      _hits4C7eGD: hits(filters: $filters_2) {
        total
      }
    }
    cnvs {
      _hits4C7eGD: hits(filters: $filters_2) {
        total
      }
    }
    ssms {
      _aggregations2YYe0C: aggregations(
        filters: $filters_2
        aggregations_filter_themselves: false
      ) {
        ...F0
      }
      _hits4C7eGD: hits(filters: $filters_2) {
        total
      }
      _hits2PHjFL: hits {
        total
      }
      _hits1fx5X6: hits {
        total
      }
    }
  }
}
    """,
    "variables": {
        "first_0": 20,
        "offset_1": 0,
        "filters_2": {
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
    },
}

if __name__ == "__main__":
    r = graphql(tcga_breast())
    pprint(r.json())
