#!/usr/bin/env python

from TCGA.lib import graphql
from TCGA.lib import convert_to_rich_table
import pandas as pd


def biospecimen(case):
    return {
        "query": """
query BiospecimenCard_relayQuery(
  $filters: FiltersArgument
  $fileFilters: FiltersArgument
) {
  viewer {
    repository {
      cases {
        hits(first: 1, filters: $filters) {
          edges {
            node {
              case_id
              submitter_id
              project {
                project_id
                id
              }
              files {
                hits(first: 99, filters: $fileFilters) {
                  edges {
                    node {
                      file_name
                      file_size
                      data_format
                      file_id
                      md5sum
                      acl
                      state
                      access
                      submitter_id
                      id
                    }
                  }
                }
              }
              samples {
                hits(first: 99) {
                  total
                  edges {
                    node {
                      submitter_id
                      sample_id
                      sample_type
                      sample_type_id
                      tissue_type
                      tumor_code
                      tumor_code_id
                      oct_embedded
                      shortest_dimension
                      intermediate_dimension
                      longest_dimension
                      is_ffpe
                      pathology_report_uuid
                      tumor_descriptor
                      current_weight
                      initial_weight
                      composition
                      time_between_clamping_and_freezing
                      time_between_excision_and_freezing
                      days_to_sample_procurement
                      freezing_method
                      preservation_method
                      days_to_collection
                      portions {
                        hits(first: 99) {
                          total
                          edges {
                            node {
                              submitter_id
                              portion_id
                              portion_number
                              weight
                              is_ffpe
                              analytes {
                                hits(first: 99) {
                                  total
                                  edges {
                                    node {
                                      submitter_id
                                      analyte_id
                                      analyte_type
                                      analyte_type_id
                                      well_number
                                      amount
                                      a260_a280_ratio
                                      concentration
                                      spectrophotometer_method
                                      aliquots {
                                        hits(first: 99) {
                                          total
                                          edges {
                                            node {
                                              submitter_id
                                              aliquot_id
                                              source_center
                                              amount
                                              concentration
                                              analyte_type
                                              analyte_type_id
                                              id
                                            }
                                          }
                                        }
                                      }
                                      id
                                    }
                                  }
                                }
                              }
                              slides {
                                hits(first: 99) {
                                  total
                                  edges {
                                    node {
                                      submitter_id
                                      slide_id
                                      percent_tumor_nuclei
                                      percent_monocyte_infiltration
                                      percent_normal_cells
                                      percent_stromal_cells
                                      percent_eosinophil_infiltration
                                      percent_lymphocyte_infiltration
                                      percent_neutrophil_infiltration
                                      section_location
                                      percent_granulocyte_infiltration
                                      percent_necrosis
                                      percent_inflam_infiltration
                                      number_proliferating_cells
                                      percent_tumor_cells
                                      id
                                    }
                                  }
                                }
                              }
                              id
                            }
                          }
                        }
                      }
                      id
                    }
                  }
                }
              }
              id
            }
          }
        }
      }
    }
  }
}
        """,
        "variables": {
            "filters": {
                "content": [
                    {
                        "content": {
                            "field": "cases.case_id",
                            "value": ["dcd5860c-7e3a-44f3-a732-fe92fe3fe300"],
                        },
                        "op": "in",
                    }
                ],
                "op": "and",
            },
            "fileFilters": {
                "content": [
                    {
                        "content": {
                            "field": "cases.case_id",
                            "value": ["dcd5860c-7e3a-44f3-a732-fe92fe3fe300"],
                        },
                        "op": "in",
                    },
#                   {
#                       "content": {
#                           "field": "files.data_type",
#                           "value": ["Biospecimen Supplement", "Slide Image"],
#                       },
#                       "op": "in",
#                   },
                ],
                "op": "and",
            },
        },
    }


def biospecimen_parsed(case, data_format=("BCR SSF XML"), filename_pattern="clinical_patient_brca.txt"):
    r = graphql(biospecimen(case))
    for x in r.json()["data"]["viewer"]["repository"]["cases"]["hits"]["edges"]:
        files = x["node"]["files"]
        for fnode in files["hits"]["edges"]:
            attrs = fnode["node"]
            if data_format and attrs["data_format"] not in data_format:
                continue
            if filename_pattern and filename_pattern not in attrs["file_name"]:
                continue
            yield fnode["node"]


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        # https://portal.gdc.cancer.gov/cases/dcd5860c-7e3a-44f3-a732-fe92fe3fe300
        rows = biospecimen_parsed("dcd5860c-7e3a-44f3-a732-fe92fe3fe300")
    else:
        rows = biospecimen_parsed(sys.argv[1], data_format="BCR Biotab")

    for row in rows:
        print(row["file_id"])
        #print(row)
        example = {
            "node": {
                "case_id": "dcd5860c-7e3a-44f3-a732-fe92fe3fe300",
                "files": {
                    "hits": {
                        "edges": [
                            {
                                "node": {
                                    "access": "open",
                                    "acl": ["open"],
                                    "data_format": "SVS",
                                    "file_id": "5a69a438-d7b2-40fa-afc1-0d02de55ee02",
                                    "file_name": "TCGA-AN-A046-01Z-00-DX1.C529B94F-AFE3-4701-BC98-5D6EDF7B82C0.svs",
                                    "file_size": 422331173.0,
                                    "id": "Q2FzZUZpbGU6ZGNkNTg2MGMtN2UzYS00NGYzLWE3MzItZmU5MmZlM2ZlMzAwOjVhNjlhNDM4LWQ3YjItNDBmYS1hZmMxLTBkMDJkZTU1ZWUwMg==",
                                    "md5sum": "48140822274e171a56cf6a2b90d1cc42",
                                    "state": "released",
                                    "submitter_id": "TCGA-AN-A046-01Z-00-DX1_slide_image",
                                }
                            },
                            {
                                "node": {
                                    "access": "open",
                                    "acl": ["open"],
                                    "data_format": "BCR Biotab",
                                    "file_id": "43569ab9-5a32-45ef-a07e-e93f45416a16",
                                    "file_name": "nationwidechildrens.org_biospecimen_shipment_portion_brca.txt",
                                    "file_size": 154614.0,
                                    "id": "Q2FzZUZpbGU6ZGNkNTg2MGMtN2UzYS00NGYzLWE3MzItZmU5MmZlM2ZlMzAwOjQzNTY5YWI5LTVhMzItNDVlZi1hMDdlLWU5M2Y0NTQxNmExNg==",
                                    "md5sum": "2a79ad158a204d1af81108b178280bea",
                                    "state": "released",
                                    "submitter_id": "nationwidechildrens.org_biospecimen_shipment_portion_brca.txt",
                                }
                            },
                            {
                                "node": {
                                    "access": "open",
                                    "acl": ["open"],
                                    "data_format": "BCR Biotab",
                                    "file_id": "5907be67-69f6-4339-8264-952a2462bea5",
                                    "file_name": "nationwidechildrens.org_ssf_normal_controls_brca.txt",
                                    "file_size": 217642.0,
                                    "id": "Q2FzZUZpbGU6ZGNkNTg2MGMtN2UzYS00NGYzLWE3MzItZmU5MmZlM2ZlMzAwOjU5MDdiZTY3LTY5ZjYtNDMzOS04MjY0LTk1MmEyNDYyYmVhNQ==",
                                    "md5sum": "f5b49c0103a9f1dc12555f4eb0c8dfaa",
                                    "state": "released",
                                    "submitter_id": "nationwidechildrens.org_ssf_normal_controls_brca.txt",
                                }
                            },
                            {
                                "node": {
                                    "access": "open",
                                    "acl": ["open"],
                                    "data_format": "BCR SSF XML",
                                    "file_id": "397ba792-0095-4f1b-91ba-8d41f11bef3c",
                                    "file_name": "nationwidechildrens.org_ssf.TCGA-AN-A046.xml",
                                    "file_size": 15518.0,
                                    "id": "Q2FzZUZpbGU6ZGNkNTg2MGMtN2UzYS00NGYzLWE3MzItZmU5MmZlM2ZlMzAwOjM5N2JhNzkyLTAwOTUtNGYxYi05MWJhLThkNDFmMTFiZWYzYw==",
                                    "md5sum": "fd097ea85a5dc9c77dcd72c202ac9a8d",
                                    "state": "released",
                                    "submitter_id": "nationwidechildrens.org_ssf.TCGA-AN-A046.xml",
                                }
                            },
                            {
                                "node": {
                                    "access": "open",
                                    "acl": ["open"],
                                    "data_format": "BCR Biotab",
                                    "file_id": "c10090b8-fa42-4e32-86a0-9dedceb5b605",
                                    "file_name": "nationwidechildrens.org_biospecimen_slide_brca.txt",
                                    "file_size": 417578.0,
                                    "id": "Q2FzZUZpbGU6ZGNkNTg2MGMtN2UzYS00NGYzLWE3MzItZmU5MmZlM2ZlMzAwOmMxMDA5MGI4LWZhNDItNGUzMi04NmEwLTlkZWRjZWI1YjYwNQ==",
                                    "md5sum": "039253c77a6125842558ba2a20ec5187",
                                    "state": "released",
                                    "submitter_id": "nationwidechildrens.org_biospecimen_slide_brca.txt",
                                }
                            },
                            {
                                "node": {
                                    "access": "open",
                                    "acl": ["open"],
                                    "data_format": "SVS",
                                    "file_id": "3a4bf726-ba8e-4d41-969f-222e554578e5",
                                    "file_name": "TCGA-AN-A046-01A-02-BS2.74a56161-07f1-4980-a2fd-2c9123fb87bc.svs",
                                    "file_size": 160675922.0,
                                    "id": "Q2FzZUZpbGU6ZGNkNTg2MGMtN2UzYS00NGYzLWE3MzItZmU5MmZlM2ZlMzAwOjNhNGJmNzI2LWJhOGUtNGQ0MS05NjlmLTIyMmU1NTQ1NzhlNQ==",
                                    "md5sum": "ec27f6f4ab5a4b4903a5ba71197e070c",
                                    "state": "released",
                                    "submitter_id": "TCGA-AN-A046-01A-02-BS2_slide_image",
                                }
                            },
                            {
                                "node": {
                                    "access": "open",
                                    "acl": ["open"],
                                    "data_format": "BCR Biotab",
                                    "file_id": "edbb5de2-d0b5-4a07-a0e1-19e952a5117d",
                                    "file_name": "nationwidechildrens.org_biospecimen_diagnostic_slides_brca.txt",
                                    "file_size": 118858.0,
                                    "id": "Q2FzZUZpbGU6ZGNkNTg2MGMtN2UzYS00NGYzLWE3MzItZmU5MmZlM2ZlMzAwOmVkYmI1ZGUyLWQwYjUtNGEwNy1hMGUxLTE5ZTk1MmE1MTE3ZA==",
                                    "md5sum": "4dce72daab60c6b11c5973b421ea35f0",
                                    "state": "released",
                                    "submitter_id": "nationwidechildrens.org_biospecimen_diagnostic_slides_brca.txt",
                                }
                            },
                            {
                                "node": {
                                    "access": "open",
                                    "acl": ["open"],
                                    "data_format": "BCR Biotab",
                                    "file_id": "c5039e7e-14d8-4e59-ba20-0d3fa38b86df",
                                    "file_name": "nationwidechildrens.org_biospecimen_sample_brca.txt",
                                    "file_size": 1005255.0,
                                    "id": "Q2FzZUZpbGU6ZGNkNTg2MGMtN2UzYS00NGYzLWE3MzItZmU5MmZlM2ZlMzAwOmM1MDM5ZTdlLTE0ZDgtNGU1OS1iYTIwLTBkM2ZhMzhiODZkZg==",
                                    "md5sum": "0fa678866ff3f85a842d821463c8c5d6",
                                    "state": "released",
                                    "submitter_id": "nationwidechildrens.org_biospecimen_sample_brca.txt",
                                }
                            },
                            {
                                "node": {
                                    "access": "open",
                                    "acl": ["open"],
                                    "data_format": "BCR Biotab",
                                    "file_id": "22656b71-476a-4b5f-9f3b-82afb29a34bc",
                                    "file_name": "nationwidechildrens.org_biospecimen_portion_brca.txt",
                                    "file_size": 358732.0,
                                    "id": "Q2FzZUZpbGU6ZGNkNTg2MGMtN2UzYS00NGYzLWE3MzItZmU5MmZlM2ZlMzAwOjIyNjU2YjcxLTQ3NmEtNGI1Zi05ZjNiLTgyYWZiMjlhMzRiYw==",
                                    "md5sum": "1700cc8fa282635235473bac179ef2c5",
                                    "state": "released",
                                    "submitter_id": "nationwidechildrens.org_biospecimen_portion_brca.txt",
                                }
                            },
                            {
                                "node": {
                                    "access": "open",
                                    "acl": ["open"],
                                    "data_format": "SVS",
                                    "file_id": "511f38a2-3d38-4cea-b1f9-d3923b63e481",
                                    "file_name": "TCGA-AN-A046-01A-01-BS1.5bc254f8-5363-470e-9963-4ccfd57a3457.svs",
                                    "file_size": 223522554.0,
                                    "id": "Q2FzZUZpbGU6ZGNkNTg2MGMtN2UzYS00NGYzLWE3MzItZmU5MmZlM2ZlMzAwOjUxMWYzOGEyLTNkMzgtNGNlYS1iMWY5LWQzOTIzYjYzZTQ4MQ==",
                                    "md5sum": "ebee26b28aa1b8a27cbf6fc10b648b7c",
                                    "state": "released",
                                    "submitter_id": "TCGA-AN-A046-01A-01-BS1_slide_image",
                                }
                            },
                            {
                                "node": {
                                    "access": "open",
                                    "acl": ["open"],
                                    "data_format": "BCR Biotab",
                                    "file_id": "a24d7574-e419-47ce-9293-b9b29f854a10",
                                    "file_name": "nationwidechildrens.org_biospecimen_protocol_brca.txt",
                                    "file_size": 789503.0,
                                    "id": "Q2FzZUZpbGU6ZGNkNTg2MGMtN2UzYS00NGYzLWE3MzItZmU5MmZlM2ZlMzAwOmEyNGQ3NTc0LWU0MTktNDdjZS05MjkzLWI5YjI5Zjg1NGExMA==",
                                    "md5sum": "8528185ddd57118e0109dd50d1f48303",
                                    "state": "released",
                                    "submitter_id": "nationwidechildrens.org_biospecimen_protocol_brca.txt",
                                }
                            },
                            {
                                "node": {
                                    "access": "open",
                                    "acl": ["open"],
                                    "data_format": "BCR Biotab",
                                    "file_id": "d0c967b5-78ee-4bc4-9493-3cbe44af1bf5",
                                    "file_name": "nationwidechildrens.org_biospecimen_analyte_brca.txt",
                                    "file_size": 1728468.0,
                                    "id": "Q2FzZUZpbGU6ZGNkNTg2MGMtN2UzYS00NGYzLWE3MzItZmU5MmZlM2ZlMzAwOmQwYzk2N2I1LTc4ZWUtNGJjNC05NDkzLTNjYmU0NGFmMWJmNQ==",
                                    "md5sum": "103577529e4355cfd0a5da055ea5a403",
                                    "state": "released",
                                    "submitter_id": "nationwidechildrens.org_biospecimen_analyte_brca.txt",
                                }
                            },
                            {
                                "node": {
                                    "access": "open",
                                    "acl": ["open"],
                                    "data_format": "BCR Biotab",
                                    "file_id": "41fd4c6c-2932-4c6b-914f-7abaea9dc8a0",
                                    "file_name": "nationwidechildrens.org_ssf_tumor_samples_brca.txt",
                                    "file_size": 353327.0,
                                    "id": "Q2FzZUZpbGU6ZGNkNTg2MGMtN2UzYS00NGYzLWE3MzItZmU5MmZlM2ZlMzAwOjQxZmQ0YzZjLTI5MzItNGM2Yi05MTRmLTdhYmFlYTlkYzhhMA==",
                                    "md5sum": "f694515fd191ab8d3c0b073e6f2fc7cb",
                                    "state": "released",
                                    "submitter_id": "nationwidechildrens.org_ssf_tumor_samples_brca.txt",
                                }
                            },
                            {
                                "node": {
                                    "access": "open",
                                    "acl": ["open"],
                                    "data_format": "BCR XML",
                                    "file_id": "1c7ac431-2608-4f26-9ddc-2003f54e53a4",
                                    "file_name": "nationwidechildrens.org_biospecimen.TCGA-AN-A046.xml",
                                    "file_size": 85580.0,
                                    "id": "Q2FzZUZpbGU6ZGNkNTg2MGMtN2UzYS00NGYzLWE3MzItZmU5MmZlM2ZlMzAwOjFjN2FjNDMxLTI2MDgtNGYyNi05ZGRjLTIwMDNmNTRlNTNhNA==",
                                    "md5sum": "31cb6c4d0bb724174c0385bbfcde307f",
                                    "state": "released",
                                    "submitter_id": "nationwidechildrens.org_biospecimen.TCGA-AN-A046.xml",
                                }
                            },
                            {
                                "node": {
                                    "access": "open",
                                    "acl": ["open"],
                                    "data_format": "BCR Biotab",
                                    "file_id": "950ee56c-df20-4b39-867e-c73f17d0f4f6",
                                    "file_name": "nationwidechildrens.org_biospecimen_aliquot_brca.txt",
                                    "file_size": 2561498.0,
                                    "id": "Q2FzZUZpbGU6ZGNkNTg2MGMtN2UzYS00NGYzLWE3MzItZmU5MmZlM2ZlMzAwOjk1MGVlNTZjLWRmMjAtNGIzOS04NjdlLWM3M2YxN2QwZjRmNg==",
                                    "md5sum": "518662abcb430af9704a29d32e596c4b",
                                    "state": "released",
                                    "submitter_id": "nationwidechildrens.org_biospecimen_aliquot_brca.txt",
                                }
                            },
                        ]
                    }
                },
                "id": "Q2FzZTpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA=",
                "project": {
                    "id": "UHJvamVjdDpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA6Xw==",
                    "project_id": "TCGA-BRCA",
                },
                "samples": {
                    "hits": {
                        "edges": [
                            {
                                "node": {
                                    "composition": None,
                                    "current_weight": None,
                                    "days_to_collection": 27.0,
                                    "days_to_sample_procurement": None,
                                    "freezing_method": None,
                                    "id": "U2FtcGxlOmRjZDU4NjBjLTdlM2EtNDRmMy1hNzMyLWZlOTJmZTNmZTMwMDo1N2FmZjA5Zi0wZTk3LTRlNjUtYTIyNy0zZGM3YTg1MTYzNjc=",
                                    "initial_weight": 150.0,
                                    "intermediate_dimension": None,
                                    "is_ffpe": "false",
                                    "longest_dimension": None,
                                    "oct_embedded": "true",
                                    "pathology_report_uuid": "1304FB17-A20A-4EBC-9CC8-1554808AC1F6",
                                    "portions": {
                                        "hits": {
                                            "edges": [
                                                {
                                                    "node": {
                                                        "analytes": {
                                                            "hits": {
                                                                "edges": [
                                                                    {
                                                                        "node": {
                                                                            "a260_a280_ratio": 1.73,
                                                                            "aliquots": {
                                                                                "hits": {
                                                                                    "edges": [
                                                                                        {
                                                                                            "node": {
                                                                                                "aliquot_id": "20eb1da4-ef70-49dd-956f-18d65725ba27",
                                                                                                "amount": None,
                                                                                                "analyte_type": None,
                                                                                                "analyte_type_id": None,
                                                                                                "concentration": 0.16,
                                                                                                "id": "QWxpcXVvdDpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA6NTdhZmYwOWYtMGU5Ny00ZTY1LWEyMjctM2RjN2E4NTE2MzY3OmFmNWJmOTc2LWNjYTMtNDRkZC05ZWIyLWE1NWUyOWFjZDU2Yjo1MTlkMjM0Ni03MTAzLTQyNWQtOTEwZC0xNmVkNjZjOWQxZDE6MjBlYjFkYTQtZWY3MC00OWRkLTk1NmYtMThkNjU3MjViYTI3",
                                                                                                "source_center": "23",
                                                                                                "submitter_id": "TCGA-AN-A046-01A-21R-A034-07",
                                                                                            }
                                                                                        },
                                                                                        {
                                                                                            "node": {
                                                                                                "aliquot_id": "7140c7c1-cba8-41f3-82ff-fb34cd0d8ca2",
                                                                                                "amount": None,
                                                                                                "analyte_type": None,
                                                                                                "analyte_type_id": None,
                                                                                                "concentration": 0.16,
                                                                                                "id": "QWxpcXVvdDpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA6NTdhZmYwOWYtMGU5Ny00ZTY1LWEyMjctM2RjN2E4NTE2MzY3OmFmNWJmOTc2LWNjYTMtNDRkZC05ZWIyLWE1NWUyOWFjZDU2Yjo1MTlkMjM0Ni03MTAzLTQyNWQtOTEwZC0xNmVkNjZjOWQxZDE6NzE0MGM3YzEtY2JhOC00MWYzLTgyZmYtZmIzNGNkMGQ4Y2Ey",
                                                                                                "source_center": "23",
                                                                                                "submitter_id": "TCGA-AN-A046-01A-21R-A035-13",
                                                                                            }
                                                                                        },
                                                                                    ],
                                                                                    "total": 2,
                                                                                }
                                                                            },
                                                                            "amount": None,
                                                                            "analyte_id": "519d2346-7103-425d-910d-16ed66c9d1d1",
                                                                            "analyte_type": "RNA",
                                                                            "analyte_type_id": "R",
                                                                            "concentration": 0.16,
                                                                            "id": "QW5hbHl0ZTpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA6NTdhZmYwOWYtMGU5Ny00ZTY1LWEyMjctM2RjN2E4NTE2MzY3OmFmNWJmOTc2LWNjYTMtNDRkZC05ZWIyLWE1NWUyOWFjZDU2Yjo1MTlkMjM0Ni03MTAzLTQyNWQtOTEwZC0xNmVkNjZjOWQxZDE=",
                                                                            "spectrophotometer_method": "UV Spec",
                                                                            "submitter_id": "TCGA-AN-A046-01A-21R",
                                                                            "well_number": None,
                                                                        }
                                                                    },
                                                                    {
                                                                        "node": {
                                                                            "a260_a280_ratio": None,
                                                                            "aliquots": {
                                                                                "hits": {
                                                                                    "edges": [
                                                                                        {
                                                                                            "node": {
                                                                                                "aliquot_id": "180989ad-10c3-43ff-9494-e4395468e864",
                                                                                                "amount": None,
                                                                                                "analyte_type": None,
                                                                                                "analyte_type_id": None,
                                                                                                "concentration": 0.5,
                                                                                                "id": "QWxpcXVvdDpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA6NTdhZmYwOWYtMGU5Ny00ZTY1LWEyMjctM2RjN2E4NTE2MzY3OmFmNWJmOTc2LWNjYTMtNDRkZC05ZWIyLWE1NWUyOWFjZDU2YjpiZDY5MzcwYS0zM2ZjLTQ1Y2YtYWRhOS1lMGIxMzYyMjY1NzM6MTgwOTg5YWQtMTBjMy00M2ZmLTk0OTQtZTQzOTU0NjhlODY0",
                                                                                                "source_center": "23",
                                                                                                "submitter_id": "TCGA-AN-A046-01A-21X-A048-08",
                                                                                            }
                                                                                        },
                                                                                        {
                                                                                            "node": {
                                                                                                "aliquot_id": "70585480-d007-4e9c-8b15-beb08313b6a4",
                                                                                                "amount": None,
                                                                                                "analyte_type": None,
                                                                                                "analyte_type_id": None,
                                                                                                "concentration": 0.5,
                                                                                                "id": "QWxpcXVvdDpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA6NTdhZmYwOWYtMGU5Ny00ZTY1LWEyMjctM2RjN2E4NTE2MzY3OmFmNWJmOTc2LWNjYTMtNDRkZC05ZWIyLWE1NWUyOWFjZDU2YjpiZDY5MzcwYS0zM2ZjLTQ1Y2YtYWRhOS1lMGIxMzYyMjY1NzM6NzA1ODU0ODAtZDAwNy00ZTljLThiMTUtYmViMDgzMTNiNmE0",
                                                                                                "source_center": "23",
                                                                                                "submitter_id": "TCGA-AN-A046-01A-21X-A049-09",
                                                                                            }
                                                                                        },
                                                                                    ],
                                                                                    "total": 2,
                                                                                }
                                                                            },
                                                                            "amount": None,
                                                                            "analyte_id": "bd69370a-33fc-45cf-ada9-e0b136226573",
                                                                            "analyte_type": "Repli-G X (Qiagen) DNA",
                                                                            "analyte_type_id": "X",
                                                                            "concentration": None,
                                                                            "id": "QW5hbHl0ZTpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA6NTdhZmYwOWYtMGU5Ny00ZTY1LWEyMjctM2RjN2E4NTE2MzY3OmFmNWJmOTc2LWNjYTMtNDRkZC05ZWIyLWE1NWUyOWFjZDU2YjpiZDY5MzcwYS0zM2ZjLTQ1Y2YtYWRhOS1lMGIxMzYyMjY1NzM=",
                                                                            "spectrophotometer_method": None,
                                                                            "submitter_id": "TCGA-AN-A046-01A-21X",
                                                                            "well_number": None,
                                                                        }
                                                                    },
                                                                    {
                                                                        "node": {
                                                                            "a260_a280_ratio": None,
                                                                            "aliquots": {
                                                                                "hits": {
                                                                                    "edges": [
                                                                                        {
                                                                                            "node": {
                                                                                                "aliquot_id": "0bc7b1e8-67be-462d-bf55-b71648ca4727",
                                                                                                "amount": None,
                                                                                                "analyte_type": None,
                                                                                                "analyte_type_id": None,
                                                                                                "concentration": 0.5,
                                                                                                "id": "QWxpcXVvdDpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA6NTdhZmYwOWYtMGU5Ny00ZTY1LWEyMjctM2RjN2E4NTE2MzY3OmFmNWJmOTc2LWNjYTMtNDRkZC05ZWIyLWE1NWUyOWFjZDU2YjpkYWJjMTM2ZS1jMGIyLTRkMTctYTU1Yi03Njc2ZjNlNjE2MDQ6MGJjN2IxZTgtNjdiZS00NjJkLWJmNTUtYjcxNjQ4Y2E0NzI3",
                                                                                                "source_center": "23",
                                                                                                "submitter_id": "TCGA-AN-A046-01A-21W-A051-08",
                                                                                            }
                                                                                        },
                                                                                        {
                                                                                            "node": {
                                                                                                "aliquot_id": "696dfa31-8ff8-4b4f-a6e5-b59c34fae1f7",
                                                                                                "amount": None,
                                                                                                "analyte_type": None,
                                                                                                "analyte_type_id": None,
                                                                                                "concentration": 0.5,
                                                                                                "id": "QWxpcXVvdDpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA6NTdhZmYwOWYtMGU5Ny00ZTY1LWEyMjctM2RjN2E4NTE2MzY3OmFmNWJmOTc2LWNjYTMtNDRkZC05ZWIyLWE1NWUyOWFjZDU2YjpkYWJjMTM2ZS1jMGIyLTRkMTctYTU1Yi03Njc2ZjNlNjE2MDQ6Njk2ZGZhMzEtOGZmOC00YjRmLWE2ZTUtYjU5YzM0ZmFlMWY3",
                                                                                                "source_center": "23",
                                                                                                "submitter_id": "TCGA-AN-A046-01A-21W-A050-09",
                                                                                            }
                                                                                        },
                                                                                    ],
                                                                                    "total": 2,
                                                                                }
                                                                            },
                                                                            "amount": None,
                                                                            "analyte_id": "dabc136e-c0b2-4d17-a55b-7676f3e61604",
                                                                            "analyte_type": "Repli-G (Qiagen) DNA",
                                                                            "analyte_type_id": "W",
                                                                            "concentration": None,
                                                                            "id": "QW5hbHl0ZTpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA6NTdhZmYwOWYtMGU5Ny00ZTY1LWEyMjctM2RjN2E4NTE2MzY3OmFmNWJmOTc2LWNjYTMtNDRkZC05ZWIyLWE1NWUyOWFjZDU2YjpkYWJjMTM2ZS1jMGIyLTRkMTctYTU1Yi03Njc2ZjNlNjE2MDQ=",
                                                                            "spectrophotometer_method": None,
                                                                            "submitter_id": "TCGA-AN-A046-01A-21W",
                                                                            "well_number": None,
                                                                        }
                                                                    },
                                                                    {
                                                                        "node": {
                                                                            "a260_a280_ratio": 1.98,
                                                                            "aliquots": {
                                                                                "hits": {
                                                                                    "edges": [
                                                                                        {
                                                                                            "node": {
                                                                                                "aliquot_id": "732f1a50-2b82-4ea5-8d44-c3b90e6dca04",
                                                                                                "amount": None,
                                                                                                "analyte_type": None,
                                                                                                "analyte_type_id": None,
                                                                                                "concentration": 0.08,
                                                                                                "id": "QWxpcXVvdDpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA6NTdhZmYwOWYtMGU5Ny00ZTY1LWEyMjctM2RjN2E4NTE2MzY3OmFmNWJmOTc2LWNjYTMtNDRkZC05ZWIyLWE1NWUyOWFjZDU2YjpmMDVmZWQ0ZC01MTc0LTQ4NDUtYTc4Zi0zYzgyY2MwZWIxYTc6NzMyZjFhNTAtMmI4Mi00ZWE1LThkNDQtYzNiOTBlNmRjYTA0",
                                                                                                "source_center": "23",
                                                                                                "submitter_id": "TCGA-AN-A046-01A-21D-A045-09",
                                                                                            }
                                                                                        },
                                                                                        {
                                                                                            "node": {
                                                                                                "aliquot_id": "7fc3a21d-f7fe-474e-905e-8f503cd34f4b",
                                                                                                "amount": None,
                                                                                                "analyte_type": None,
                                                                                                "analyte_type_id": None,
                                                                                                "concentration": 0.16,
                                                                                                "id": "QWxpcXVvdDpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA6NTdhZmYwOWYtMGU5Ny00ZTY1LWEyMjctM2RjN2E4NTE2MzY3OmFmNWJmOTc2LWNjYTMtNDRkZC05ZWIyLWE1NWUyOWFjZDU2YjpmMDVmZWQ0ZC01MTc0LTQ4NDUtYTc4Zi0zYzgyY2MwZWIxYTc6N2ZjM2EyMWQtZjdmZS00NzRlLTkwNWUtOGY1MDNjZDM0ZjRi",
                                                                                                "source_center": "23",
                                                                                                "submitter_id": "TCGA-AN-A046-01A-21D-A033-02",
                                                                                            }
                                                                                        },
                                                                                        {
                                                                                            "node": {
                                                                                                "aliquot_id": "c62fa764-5d48-4bbc-ad18-6e0aff57fa4f",
                                                                                                "amount": None,
                                                                                                "analyte_type": None,
                                                                                                "analyte_type_id": None,
                                                                                                "concentration": 0.16,
                                                                                                "id": "QWxpcXVvdDpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA6NTdhZmYwOWYtMGU5Ny00ZTY1LWEyMjctM2RjN2E4NTE2MzY3OmFmNWJmOTc2LWNjYTMtNDRkZC05ZWIyLWE1NWUyOWFjZDU2YjpmMDVmZWQ0ZC01MTc0LTQ4NDUtYTc4Zi0zYzgyY2MwZWIxYTc6YzYyZmE3NjQtNWQ0OC00YmJjLWFkMTgtNmUwYWZmNTdmYTRm",
                                                                                                "source_center": "23",
                                                                                                "submitter_id": "TCGA-AN-A046-01A-21D-A036-01",
                                                                                            }
                                                                                        },
                                                                                        {
                                                                                            "node": {
                                                                                                "aliquot_id": "d371585c-0e14-45f5-b296-160d9261825d",
                                                                                                "amount": None,
                                                                                                "analyte_type": None,
                                                                                                "analyte_type_id": None,
                                                                                                "concentration": 0.08,
                                                                                                "id": "QWxpcXVvdDpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA6NTdhZmYwOWYtMGU5Ny00ZTY1LWEyMjctM2RjN2E4NTE2MzY3OmFmNWJmOTc2LWNjYTMtNDRkZC05ZWIyLWE1NWUyOWFjZDU2YjpmMDVmZWQ0ZC01MTc0LTQ4NDUtYTc4Zi0zYzgyY2MwZWIxYTc6ZDM3MTU4NWMtMGUxNC00NWY1LWIyOTYtMTYwZDkyNjE4MjVk",
                                                                                                "source_center": "23",
                                                                                                "submitter_id": "TCGA-AN-A046-01A-21D-A044-08",
                                                                                            }
                                                                                        },
                                                                                        {
                                                                                            "node": {
                                                                                                "aliquot_id": "ebba0fc0-8380-45ba-a4dc-632a8543bf41",
                                                                                                "amount": None,
                                                                                                "analyte_type": None,
                                                                                                "analyte_type_id": None,
                                                                                                "concentration": 0.16,
                                                                                                "id": "QWxpcXVvdDpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA6NTdhZmYwOWYtMGU5Ny00ZTY1LWEyMjctM2RjN2E4NTE2MzY3OmFmNWJmOTc2LWNjYTMtNDRkZC05ZWIyLWE1NWUyOWFjZDU2YjpmMDVmZWQ0ZC01MTc0LTQ4NDUtYTc4Zi0zYzgyY2MwZWIxYTc6ZWJiYTBmYzAtODM4MC00NWJhLWE0ZGMtNjMyYTg1NDNiZjQx",
                                                                                                "source_center": "23",
                                                                                                "submitter_id": "TCGA-AN-A046-01A-21D-A032-05",
                                                                                            }
                                                                                        },
                                                                                    ],
                                                                                    "total": 5,
                                                                                }
                                                                            },
                                                                            "amount": None,
                                                                            "analyte_id": "f05fed4d-5174-4845-a78f-3c82cc0eb1a7",
                                                                            "analyte_type": "DNA",
                                                                            "analyte_type_id": "D",
                                                                            "concentration": 0.16,
                                                                            "id": "QW5hbHl0ZTpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA6NTdhZmYwOWYtMGU5Ny00ZTY1LWEyMjctM2RjN2E4NTE2MzY3OmFmNWJmOTc2LWNjYTMtNDRkZC05ZWIyLWE1NWUyOWFjZDU2YjpmMDVmZWQ0ZC01MTc0LTQ4NDUtYTc4Zi0zYzgyY2MwZWIxYTc=",
                                                                            "spectrophotometer_method": "UV Spec",
                                                                            "submitter_id": "TCGA-AN-A046-01A-21D",
                                                                            "well_number": None,
                                                                        }
                                                                    },
                                                                ],
                                                                "total": 4,
                                                            }
                                                        },
                                                        "id": "UG9ydGlvbjpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA6NTdhZmYwOWYtMGU5Ny00ZTY1LWEyMjctM2RjN2E4NTE2MzY3OmFmNWJmOTc2LWNjYTMtNDRkZC05ZWIyLWE1NWUyOWFjZDU2Yg==",
                                                        "is_ffpe": "false",
                                                        "portion_id": "af5bf976-cca3-44dd-9eb2-a55e29acd56b",
                                                        "portion_number": "21",
                                                        "slides": {
                                                            "hits": {
                                                                "edges": [
                                                                    {
                                                                        "node": {
                                                                            "id": "U2xpZGU6ZGNkNTg2MGMtN2UzYS00NGYzLWE3MzItZmU5MmZlM2ZlMzAwOjU3YWZmMDlmLTBlOTctNGU2NS1hMjI3LTNkYzdhODUxNjM2NzphZjViZjk3Ni1jY2EzLTQ0ZGQtOWViMi1hNTVlMjlhY2Q1NmI6NWJjMjU0ZjgtNTM2My00NzBlLTk5NjMtNGNjZmQ1N2EzNDU3",
                                                                            "number_proliferating_cells": None,
                                                                            "percent_eosinophil_infiltration": None,
                                                                            "percent_granulocyte_infiltration": None,
                                                                            "percent_inflam_infiltration": None,
                                                                            "percent_lymphocyte_infiltration": 1.0,
                                                                            "percent_monocyte_infiltration": 1.0,
                                                                            "percent_necrosis": 1.0,
                                                                            "percent_neutrophil_infiltration": 0.0,
                                                                            "percent_normal_cells": 0.0,
                                                                            "percent_stromal_cells": 7.0,
                                                                            "percent_tumor_cells": 92.0,
                                                                            "percent_tumor_nuclei": 92.0,
                                                                            "section_location": "TOP",
                                                                            "slide_id": "5bc254f8-5363-470e-9963-4ccfd57a3457",
                                                                            "submitter_id": "TCGA-AN-A046-01A-01-BS1",
                                                                        }
                                                                    },
                                                                    {
                                                                        "node": {
                                                                            "id": "U2xpZGU6ZGNkNTg2MGMtN2UzYS00NGYzLWE3MzItZmU5MmZlM2ZlMzAwOjU3YWZmMDlmLTBlOTctNGU2NS1hMjI3LTNkYzdhODUxNjM2NzphZjViZjk3Ni1jY2EzLTQ0ZGQtOWViMi1hNTVlMjlhY2Q1NmI6NzRhNTYxNjEtMDdmMS00OTgwLWEyZmQtMmM5MTIzZmI4N2Jj",
                                                                            "number_proliferating_cells": None,
                                                                            "percent_eosinophil_infiltration": None,
                                                                            "percent_granulocyte_infiltration": None,
                                                                            "percent_inflam_infiltration": None,
                                                                            "percent_lymphocyte_infiltration": 6.0,
                                                                            "percent_monocyte_infiltration": 2.0,
                                                                            "percent_necrosis": 1.0,
                                                                            "percent_neutrophil_infiltration": 0.0,
                                                                            "percent_normal_cells": 0.0,
                                                                            "percent_stromal_cells": 10.0,
                                                                            "percent_tumor_cells": 89.0,
                                                                            "percent_tumor_nuclei": 80.0,
                                                                            "section_location": "BOTTOM",
                                                                            "slide_id": "74a56161-07f1-4980-a2fd-2c9123fb87bc",
                                                                            "submitter_id": "TCGA-AN-A046-01A-02-BS2",
                                                                        }
                                                                    },
                                                                ],
                                                                "total": 2,
                                                            }
                                                        },
                                                        "submitter_id": "TCGA-AN-A046-01A-21",
                                                        "weight": 20.0,
                                                    }
                                                }
                                            ],
                                            "total": 1,
                                        }
                                    },
                                    "preservation_method": None,
                                    "sample_id": "57aff09f-0e97-4e65-a227-3dc7a8516367",
                                    "sample_type": "Primary Tumor",
                                    "sample_type_id": "01",
                                    "shortest_dimension": None,
                                    "submitter_id": "TCGA-AN-A046-01A",
                                    "time_between_clamping_and_freezing": None,
                                    "time_between_excision_and_freezing": None,
                                    "tissue_type": "Not Reported",
                                    "tumor_code": None,
                                    "tumor_code_id": None,
                                    "tumor_descriptor": None,
                                }
                            },
                            {
                                "node": {
                                    "composition": None,
                                    "current_weight": None,
                                    "days_to_collection": None,
                                    "days_to_sample_procurement": 0.0,
                                    "freezing_method": None,
                                    "id": "U2FtcGxlOmRjZDU4NjBjLTdlM2EtNDRmMy1hNzMyLWZlOTJmZTNmZTMwMDpiOGEwOWU4NC01MzBmLTQzOWItOGU5ZC1hNmIwYzFhZTdmYWU=",
                                    "initial_weight": None,
                                    "intermediate_dimension": None,
                                    "is_ffpe": "true",
                                    "longest_dimension": None,
                                    "oct_embedded": "No",
                                    "pathology_report_uuid": None,
                                    "portions": {
                                        "hits": {
                                            "edges": [
                                                {
                                                    "node": {
                                                        "analytes": {
                                                            "hits": {
                                                                "edges": [],
                                                                "total": 0,
                                                            }
                                                        },
                                                        "id": "UG9ydGlvbjpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA6YjhhMDllODQtNTMwZi00MzliLThlOWQtYTZiMGMxYWU3ZmFlOjQyNWM5NTQ4LWUwYzAtNTVhOS04NjQ0LWJhMjMyYmVhN2U1OA==",
                                                        "is_ffpe": None,
                                                        "portion_id": "425c9548-e0c0-55a9-8644-ba232bea7e58",
                                                        "portion_number": None,
                                                        "slides": {
                                                            "hits": {
                                                                "edges": [
                                                                    {
                                                                        "node": {
                                                                            "id": "U2xpZGU6ZGNkNTg2MGMtN2UzYS00NGYzLWE3MzItZmU5MmZlM2ZlMzAwOmI4YTA5ZTg0LTUzMGYtNDM5Yi04ZTlkLWE2YjBjMWFlN2ZhZTo0MjVjOTU0OC1lMGMwLTU1YTktODY0NC1iYTIzMmJlYTdlNTg6ODIzMzg1YmEtMTc1OS00MTFlLWI4ZGItYzE5Nzc2NTUyMzVk",
                                                                            "number_proliferating_cells": None,
                                                                            "percent_eosinophil_infiltration": None,
                                                                            "percent_granulocyte_infiltration": None,
                                                                            "percent_inflam_infiltration": None,
                                                                            "percent_lymphocyte_infiltration": None,
                                                                            "percent_monocyte_infiltration": None,
                                                                            "percent_necrosis": None,
                                                                            "percent_neutrophil_infiltration": None,
                                                                            "percent_normal_cells": None,
                                                                            "percent_stromal_cells": None,
                                                                            "percent_tumor_cells": None,
                                                                            "percent_tumor_nuclei": None,
                                                                            "section_location": "Not Reported",
                                                                            "slide_id": "823385ba-1759-411e-b8db-c1977655235d",
                                                                            "submitter_id": "TCGA-AN-A046-01Z-00-DX1",
                                                                        }
                                                                    }
                                                                ],
                                                                "total": 1,
                                                            }
                                                        },
                                                        "submitter_id": None,
                                                        "weight": None,
                                                    }
                                                }
                                            ],
                                            "total": 1,
                                        }
                                    },
                                    "preservation_method": "FFPE",
                                    "sample_id": "b8a09e84-530f-439b-8e9d-a6b0c1ae7fae",
                                    "sample_type": "Primary Tumor",
                                    "sample_type_id": "01",
                                    "shortest_dimension": None,
                                    "submitter_id": "TCGA-AN-A046-01Z",
                                    "time_between_clamping_and_freezing": None,
                                    "time_between_excision_and_freezing": None,
                                    "tissue_type": "Not Reported",
                                    "tumor_code": None,
                                    "tumor_code_id": None,
                                    "tumor_descriptor": None,
                                }
                            },
                            {
                                "node": {
                                    "composition": None,
                                    "current_weight": None,
                                    "days_to_collection": 27.0,
                                    "days_to_sample_procurement": None,
                                    "freezing_method": None,
                                    "id": "U2FtcGxlOmRjZDU4NjBjLTdlM2EtNDRmMy1hNzMyLWZlOTJmZTNmZTMwMDpjMWY4Mjk2MS02ZTM2LTQ2ODgtOTQwZC0zMDBjYjgxZGIxZGE=",
                                    "initial_weight": None,
                                    "intermediate_dimension": None,
                                    "is_ffpe": "false",
                                    "longest_dimension": None,
                                    "oct_embedded": "false",
                                    "pathology_report_uuid": None,
                                    "portions": {
                                        "hits": {
                                            "edges": [
                                                {
                                                    "node": {
                                                        "analytes": {
                                                            "hits": {
                                                                "edges": [
                                                                    {
                                                                        "node": {
                                                                            "a260_a280_ratio": None,
                                                                            "aliquots": {
                                                                                "hits": {
                                                                                    "edges": [
                                                                                        {
                                                                                            "node": {
                                                                                                "aliquot_id": "2de15869-ea93-45a5-b36b-13d22e04e4f6",
                                                                                                "amount": None,
                                                                                                "analyte_type": None,
                                                                                                "analyte_type_id": None,
                                                                                                "concentration": 0.5,
                                                                                                "id": "QWxpcXVvdDpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA6YzFmODI5NjEtNmUzNi00Njg4LTk0MGQtMzAwY2I4MWRiMWRhOmZjMWNhZTZkLWE2MDMtNDgzYS1hOWYwLTM2MDczNmM0MDE3MDoxZTg2OTUxYi01NTBjLTQ2N2ItODgyNS05ZDA4MmM5Y2NiZjI6MmRlMTU4NjktZWE5My00NWE1LWIzNmItMTNkMjJlMDRlNGY2",
                                                                                                "source_center": "23",
                                                                                                "submitter_id": "TCGA-AN-A046-10A-01W-A053-08",
                                                                                            }
                                                                                        },
                                                                                        {
                                                                                            "node": {
                                                                                                "aliquot_id": "7fd1a063-e742-4ebc-acbd-c81ba11f1cc3",
                                                                                                "amount": None,
                                                                                                "analyte_type": None,
                                                                                                "analyte_type_id": None,
                                                                                                "concentration": 0.5,
                                                                                                "id": "QWxpcXVvdDpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA6YzFmODI5NjEtNmUzNi00Njg4LTk0MGQtMzAwY2I4MWRiMWRhOmZjMWNhZTZkLWE2MDMtNDgzYS1hOWYwLTM2MDczNmM0MDE3MDoxZTg2OTUxYi01NTBjLTQ2N2ItODgyNS05ZDA4MmM5Y2NiZjI6N2ZkMWEwNjMtZTc0Mi00ZWJjLWFjYmQtYzgxYmExMWYxY2Mz",
                                                                                                "source_center": "23",
                                                                                                "submitter_id": "TCGA-AN-A046-10A-01W-A055-09",
                                                                                            }
                                                                                        },
                                                                                    ],
                                                                                    "total": 2,
                                                                                }
                                                                            },
                                                                            "amount": None,
                                                                            "analyte_id": "1e86951b-550c-467b-8825-9d082c9ccbf2",
                                                                            "analyte_type": "Repli-G (Qiagen) DNA",
                                                                            "analyte_type_id": "W",
                                                                            "concentration": None,
                                                                            "id": "QW5hbHl0ZTpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA6YzFmODI5NjEtNmUzNi00Njg4LTk0MGQtMzAwY2I4MWRiMWRhOmZjMWNhZTZkLWE2MDMtNDgzYS1hOWYwLTM2MDczNmM0MDE3MDoxZTg2OTUxYi01NTBjLTQ2N2ItODgyNS05ZDA4MmM5Y2NiZjI=",
                                                                            "spectrophotometer_method": None,
                                                                            "submitter_id": "TCGA-AN-A046-10A-01W",
                                                                            "well_number": None,
                                                                        }
                                                                    },
                                                                    {
                                                                        "node": {
                                                                            "a260_a280_ratio": 1.94,
                                                                            "aliquots": {
                                                                                "hits": {
                                                                                    "edges": [
                                                                                        {
                                                                                            "node": {
                                                                                                "aliquot_id": "6f853697-3b85-4685-8f68-1c66828ef8ba",
                                                                                                "amount": None,
                                                                                                "analyte_type": None,
                                                                                                "analyte_type_id": None,
                                                                                                "concentration": 0.17,
                                                                                                "id": "QWxpcXVvdDpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA6YzFmODI5NjEtNmUzNi00Njg4LTk0MGQtMzAwY2I4MWRiMWRhOmZjMWNhZTZkLWE2MDMtNDgzYS1hOWYwLTM2MDczNmM0MDE3MDo3YmZmNGU1OS04NmM0LTQ1NjgtYjQ4Ni1lZjc2MDc2ZGI0MWY6NmY4NTM2OTctM2I4NS00Njg1LThmNjgtMWM2NjgyOGVmOGJh",
                                                                                                "source_center": "23",
                                                                                                "submitter_id": "TCGA-AN-A046-10A-01D-A037-01",
                                                                                            }
                                                                                        },
                                                                                        {
                                                                                            "node": {
                                                                                                "aliquot_id": "9274ecd8-cb72-4aab-bb9b-766f2e1d3eb7",
                                                                                                "amount": None,
                                                                                                "analyte_type": None,
                                                                                                "analyte_type_id": None,
                                                                                                "concentration": 0.08,
                                                                                                "id": "QWxpcXVvdDpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA6YzFmODI5NjEtNmUzNi00Njg4LTk0MGQtMzAwY2I4MWRiMWRhOmZjMWNhZTZkLWE2MDMtNDgzYS1hOWYwLTM2MDczNmM0MDE3MDo3YmZmNGU1OS04NmM0LTQ1NjgtYjQ4Ni1lZjc2MDc2ZGI0MWY6OTI3NGVjZDgtY2I3Mi00YWFiLWJiOWItNzY2ZjJlMWQzZWI3",
                                                                                                "source_center": "23",
                                                                                                "submitter_id": "TCGA-AN-A046-10A-01D-A046-08",
                                                                                            }
                                                                                        },
                                                                                        {
                                                                                            "node": {
                                                                                                "aliquot_id": "c634eea0-133e-4540-9251-ca860882208d",
                                                                                                "amount": None,
                                                                                                "analyte_type": None,
                                                                                                "analyte_type_id": None,
                                                                                                "concentration": 0.17,
                                                                                                "id": "QWxpcXVvdDpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA6YzFmODI5NjEtNmUzNi00Njg4LTk0MGQtMzAwY2I4MWRiMWRhOmZjMWNhZTZkLWE2MDMtNDgzYS1hOWYwLTM2MDczNmM0MDE3MDo3YmZmNGU1OS04NmM0LTQ1NjgtYjQ4Ni1lZjc2MDc2ZGI0MWY6YzYzNGVlYTAtMTMzZS00NTQwLTkyNTEtY2E4NjA4ODIyMDhk",
                                                                                                "source_center": "23",
                                                                                                "submitter_id": "TCGA-AN-A046-10A-01D-A031-02",
                                                                                            }
                                                                                        },
                                                                                        {
                                                                                            "node": {
                                                                                                "aliquot_id": "edd7f88b-5c8c-446e-8daa-cd8cad41ef47",
                                                                                                "amount": None,
                                                                                                "analyte_type": None,
                                                                                                "analyte_type_id": None,
                                                                                                "concentration": 0.08,
                                                                                                "id": "QWxpcXVvdDpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA6YzFmODI5NjEtNmUzNi00Njg4LTk0MGQtMzAwY2I4MWRiMWRhOmZjMWNhZTZkLWE2MDMtNDgzYS1hOWYwLTM2MDczNmM0MDE3MDo3YmZmNGU1OS04NmM0LTQ1NjgtYjQ4Ni1lZjc2MDc2ZGI0MWY6ZWRkN2Y4OGItNWM4Yy00NDZlLThkYWEtY2Q4Y2FkNDFlZjQ3",
                                                                                                "source_center": "23",
                                                                                                "submitter_id": "TCGA-AN-A046-10A-01D-A047-09",
                                                                                            }
                                                                                        },
                                                                                    ],
                                                                                    "total": 4,
                                                                                }
                                                                            },
                                                                            "amount": None,
                                                                            "analyte_id": "7bff4e59-86c4-4568-b486-ef76076db41f",
                                                                            "analyte_type": "DNA",
                                                                            "analyte_type_id": "D",
                                                                            "concentration": 0.17,
                                                                            "id": "QW5hbHl0ZTpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA6YzFmODI5NjEtNmUzNi00Njg4LTk0MGQtMzAwY2I4MWRiMWRhOmZjMWNhZTZkLWE2MDMtNDgzYS1hOWYwLTM2MDczNmM0MDE3MDo3YmZmNGU1OS04NmM0LTQ1NjgtYjQ4Ni1lZjc2MDc2ZGI0MWY=",
                                                                            "spectrophotometer_method": "UV Spec",
                                                                            "submitter_id": "TCGA-AN-A046-10A-01D",
                                                                            "well_number": None,
                                                                        }
                                                                    },
                                                                    {
                                                                        "node": {
                                                                            "a260_a280_ratio": None,
                                                                            "aliquots": {
                                                                                "hits": {
                                                                                    "edges": [
                                                                                        {
                                                                                            "node": {
                                                                                                "aliquot_id": "8b29c2dd-5ad9-4dac-9f58-3425a15d87d8",
                                                                                                "amount": None,
                                                                                                "analyte_type": None,
                                                                                                "analyte_type_id": None,
                                                                                                "concentration": 0.5,
                                                                                                "id": "QWxpcXVvdDpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA6YzFmODI5NjEtNmUzNi00Njg4LTk0MGQtMzAwY2I4MWRiMWRhOmZjMWNhZTZkLWE2MDMtNDgzYS1hOWYwLTM2MDczNmM0MDE3MDpmYmRiZTkwNS0xNDU2LTQ0ZWUtYTJiOC01OTJhMjJjMGI0Nzk6OGIyOWMyZGQtNWFkOS00ZGFjLTlmNTgtMzQyNWExNWQ4N2Q4",
                                                                                                "source_center": "23",
                                                                                                "submitter_id": "TCGA-AN-A046-10A-01X-A054-09",
                                                                                            }
                                                                                        },
                                                                                        {
                                                                                            "node": {
                                                                                                "aliquot_id": "8e490f11-6cc8-4820-8cee-308f88eea008",
                                                                                                "amount": None,
                                                                                                "analyte_type": None,
                                                                                                "analyte_type_id": None,
                                                                                                "concentration": 0.5,
                                                                                                "id": "QWxpcXVvdDpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA6YzFmODI5NjEtNmUzNi00Njg4LTk0MGQtMzAwY2I4MWRiMWRhOmZjMWNhZTZkLWE2MDMtNDgzYS1hOWYwLTM2MDczNmM0MDE3MDpmYmRiZTkwNS0xNDU2LTQ0ZWUtYTJiOC01OTJhMjJjMGI0Nzk6OGU0OTBmMTEtNmNjOC00ODIwLThjZWUtMzA4Zjg4ZWVhMDA4",
                                                                                                "source_center": "23",
                                                                                                "submitter_id": "TCGA-AN-A046-10A-01X-A052-08",
                                                                                            }
                                                                                        },
                                                                                    ],
                                                                                    "total": 2,
                                                                                }
                                                                            },
                                                                            "amount": None,
                                                                            "analyte_id": "fbdbe905-1456-44ee-a2b8-592a22c0b479",
                                                                            "analyte_type": "Repli-G X (Qiagen) DNA",
                                                                            "analyte_type_id": "X",
                                                                            "concentration": None,
                                                                            "id": "QW5hbHl0ZTpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA6YzFmODI5NjEtNmUzNi00Njg4LTk0MGQtMzAwY2I4MWRiMWRhOmZjMWNhZTZkLWE2MDMtNDgzYS1hOWYwLTM2MDczNmM0MDE3MDpmYmRiZTkwNS0xNDU2LTQ0ZWUtYTJiOC01OTJhMjJjMGI0Nzk=",
                                                                            "spectrophotometer_method": None,
                                                                            "submitter_id": "TCGA-AN-A046-10A-01X",
                                                                            "well_number": None,
                                                                        }
                                                                    },
                                                                ],
                                                                "total": 3,
                                                            }
                                                        },
                                                        "id": "UG9ydGlvbjpkY2Q1ODYwYy03ZTNhLTQ0ZjMtYTczMi1mZTkyZmUzZmUzMDA6YzFmODI5NjEtNmUzNi00Njg4LTk0MGQtMzAwY2I4MWRiMWRhOmZjMWNhZTZkLWE2MDMtNDgzYS1hOWYwLTM2MDczNmM0MDE3MA==",
                                                        "is_ffpe": "false",
                                                        "portion_id": "fc1cae6d-a603-483a-a9f0-360736c40170",
                                                        "portion_number": "01",
                                                        "slides": {
                                                            "hits": {
                                                                "edges": [],
                                                                "total": 0,
                                                            }
                                                        },
                                                        "submitter_id": "TCGA-AN-A046-10A-01",
                                                        "weight": 2.0,
                                                    }
                                                }
                                            ],
                                            "total": 1,
                                        }
                                    },
                                    "preservation_method": None,
                                    "sample_id": "c1f82961-6e36-4688-940d-300cb81db1da",
                                    "sample_type": "Blood Derived Normal",
                                    "sample_type_id": "10",
                                    "shortest_dimension": None,
                                    "submitter_id": "TCGA-AN-A046-10A",
                                    "time_between_clamping_and_freezing": None,
                                    "time_between_excision_and_freezing": None,
                                    "tissue_type": "Not Reported",
                                    "tumor_code": None,
                                    "tumor_code_id": None,
                                    "tumor_descriptor": None,
                                }
                            },
                        ],
                        "total": 3,
                    }
                },
                "submitter_id": "TCGA-AN-A046",
            }
        }
