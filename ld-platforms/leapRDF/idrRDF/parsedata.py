from rdflib import Graph, URIRef, Literal, Namespace, BNode
import pandas as pd
from rdflib.namespace import RDF, RDFS, DCTERMS, DC
from wikidataintegrator import wdi_core

omeroRDF = Graph()
HPAS = Namespace("http://www.proteinatlas.org/search/")
OMERO = Namespace("https://idr.openmicroscopy.org/webclient/img_detail/")
WD = Namespace("http://www.wikidata.org/entity/")
WDP = Namespace("http://www.wikidata.org/prop/direct/")
wikidata = dict()

# datasets.tsv
datasets = pd.read_csv("datasets.tsv", delimiter="\t", header=None)
datasetURIs = dict()
for index, row in datasets.iterrows():
    omeroRDF.add((HPAS[str(row[2])], RDFS.label, Literal(row[2])))
    datasetURIs[str(row[1])] = HPAS[str(row[2])]
    #omeroRDF.add((URIRef("http://deltatissue.net/project/"+str(row[1])), DCTERMS.isPartOf, URIRef("http://deltatissue.net/project/"+str(row[0]))))

# project_annotations
project_annotations = pd.read_csv("project_annotations.tsv", delimiter="\t", header=None)
print("project_annotations")
#projects
projects = pd.read_csv("projects.tsv", delimiter="\t", header=None)
print("projects...")

#images
images = pd.read_csv("images.tsv", delimiter="\t", header=None)
imageURIs = dict()
print("images...")

for index, row in images.iterrows():
    omeroRDF.add((OMERO[str(row[2])], DCTERMS.isPartOf, HPAS[0]))
    imageURIs[str(row[1])] = OMERO[str(row[2])]

print("image annotations...")
image_annotations  = pd.read_csv("image_annotations.tsv", delimiter="\t", header=None)
pd.set_option('display.max_rows', None)
for index,row in image_annotations.iterrows():
    thing = BNode()
    omeroRDF.add((OMERO[str(0)], WDP.P180, thing))
    omeroRDF.add((thing, RDF.type, WD.Q35120)) # Q35120 = THING
    
    if str(row[3]) == "Organism":
        if str(row[4]) in wikidata.keys():
            omeroRDF.add((thing, WDP.P703, wikidata[row[4]]))
        else:
            query = f"""
            SELECT * WHERE {{
               ?taxon wdt:P225 "{row[4]}"
            }}
            """
            result = wdi_core.WDFunctionsEngine.execute_sparql_query(query)
            if len(result["results"]["bindings"])>0:
                wikidata[str(row[4])] = URIRef(result["results"]["bindings"][0]["taxon"]["value"])
            else:
                print("missing "+row[4]+" in wikidata")
            omeroRDF.add((thing, WDP.P703, wikidata[str(row[4])]))    
            
    if str(row[3]) == "Pathology":
        print(row[4])
        # typo's
        if row[4] == "Carcinoma, endometroid":
            row[4] = "Carcinoma, endometrioid"
        
        # list for curation
        tocurate = ["Malignant lymphoma, non-Hodgkin's type, Low grade",
                   "Malignant melanoma, NOS" # isn't melanoma malignant by default?
                   "Malignant melanoma, Metastatic site",
                   "Malignant melanoma, NOS",
                   "Malignant melanoma, Metastatic site",
                   "Adenocarcinoma, Low grade",
                   "Carcinoid, malignant, NOS",
                   "Normal tissue, NOS"]
        if row[4] in tocurate :
            continue
            
        if str(row[4]) in wikidata.keys():
            omeroRDF.add((thing, WDP.P827, wikidata[row[4]]))
        else:
            query = f"""
            
            SELECT * WHERE {{
            VALUES ?pathology {{wd:Q12136}}
               {{?disease  wdt:P31 ?pathology .}}
                UNION
                {{?disease  wdt:P279 ?pathology .}}
                UNION
                {{?disease  wdt:P279/wdt:P31 ?pathology .}}
                UNION
                {{?disease  wdt:P279+ ?pathology .}}
               {{?disease rdfs:label "{row[4].lower()}"@en}}
               UNION
               {{?disease skos:altLabel "{row[4].lower()}"@en}}
            }}
            """
            print(query)
            result = wdi_core.WDFunctionsEngine.execute_sparql_query(query)
            if len(result["results"]["bindings"])>0:
                wikidata[str(row[4])] = URIRef(result["results"]["bindings"][0]["disease"]["value"])
            else:
                print("missing "+row[4]+" in wikidata")
            omeroRDF.add((thing, WDP.P827, wikidata[str(row[4])]))
            
        if str(row[3]) == "Organism Part":
            print(row[4])
            if str(row[4]) in wikidata.keys():
                omeroRDF.add((thing, WDP.P827, wikidata[row[4]]))
            else:
                query = f"""

                SELECT * WHERE {{
                VALUES ?organ {{wd:Q103812529 wd:Q4936952 wd:Q712378 wd:Q24060765 wd:Q103843025 wd:Q27162596}}
                   {{?anatomical_structure  wdt:P31 ?organ .}}
                    UNION
                    {{?anatomical_structure  wdt:P279 ?organ .}}
                    UNION
                    {{?anatomical_structure  wdt:P279/wdt:P31 ?organ .}}
                    UNION
                    {{?anatomical_structure  wdt:P279+ ?organ .}}
                   {{?anatomical_structure rdfs:label "{row[4].lower()}"@en}}
                   UNION
                   {{?anatomical_structure skos:altLabel "{row[4].lower()}"@en}}
                }}
                """
                print(query)
                result = wdi_core.WDFunctionsEngine.execute_sparql_query(query)
                if len(result["results"]["bindings"])>0:
                    wikidata[str(row[4])] = URIRef(result["results"]["bindings"][0]["anatomical_structure"]["value"])
                else:
                    print("missing "+row[4]+" in wikidata")
                omeroRDF.add((thing, WDP.P827, wikidata[str(row[4])]))
            
    
    if str(row[3]) == "Sex":
        if row[4] == "Female":
            omeroRDF.add((thing, WDP.P21, WD.Q6581072))
        elif row[4] == "Male":
            omeroRDF.add((thing, WDP.P21, WD.Q6581097))
            
    if str(row[3]) == "Age":
        omeroRDF.add((thing, WDP.P3629, Literal(row[4])))
                   
    if str(row[3])== "Antibody Identifier URL":
        omeroRDF.add((thing, DC.identifier, URIRef(row[4])))
        
    if str(row[3])=="Gene Symbol":
        omeroRDF.add((thing, WDP.P353, Literal(row[4])))
        
    if str(row[3]) =="Antibody Identifier URL":
        omeroRDF.add((thing, DC.identifier, URIRef(row[4])))
    
    if str(row[3]) =="Gene Identifier URL":
        omeroRDF.add((thing, DC.identifier, URIRef(row[4])))
        
print("generate RDF")
omeroRDF.serialize(format="turtle", destination="hpa_omero.ttl")
get_ipython().system('gzip hpa_omero.ttl')





