---
title: First draft schemas
---

© 2022 Andra Waagmeester and Josh Moore.

## Draft Linked Data Schema for the "Breast metadata file"
Input: https://docs.google.com/spreadsheets/d/1Ivb14Pac_ADLaAuysPvulYtGAAbzE8ffludVfMLt6HM/edit#gid=397194

This folder contains a set of draft proposals for a linked-data schema to capture clinical data collected in the context of the [ΔTissue project](https://wellcomeleap.org/delta-tissue/).

### Introduction
Linked data removes ambiguity in data by using universal identifiers and the unified data model of triples. A triple consist of a three components, which resembles the [subject-verb-object word order](https://en.wikipedia.org/wiki/Subject%E2%80%93verb%E2%80%93object_word_order) in English sentence structures. Except, in linked-data triples the sentences primarily consists of [uniform identfiers](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier). These identifiers link the triples a in "web of data". 

Creating linked data can be described as a process where the identifiers needed are identified as well as the schema that describe the linked-data patterns one can expect. Identifiers can be obtained by searching [controlled vocabularies](https://en.wikipedia.org/wiki/Controlled_vocabulary) and [ontologies](https://en.wikipedia.org/wiki/Ontology_(information_science))

This document proposes a few schemas for the [breast metadata set](https://docs.google.com/spreadsheets/d/1Ivb14Pac_ADLaAuysPvulYtGAAbzE8ffludVfMLt6HM/edit#gid=397194):

* [Native schema](#native-schema): is a "clean-room" implementation but carries the burden of maintaining all terms
* [OBO schema](#schema-using-open-biomedical-ontologies-obofoundry): a more complete schema makes use of otologies like NCIt from OLS

### Native schema
In this schema we have not consulted external ontologies. This does hamper interoperability, i.e. the data is not easily linked to or from external linked data resources. Unless the data comes from an authoritative source in the domain. 

```shex
# Author: Andra Waagemeester
# Based on: https://docs.google.com/spreadsheets/d/1Ivb14Pac_ADLaAuysPvulYtGAAbzE8ffludVfMLt6HM/edit#gid=397194
# This model is fully based on the provided draft
# The definition need to be provided by the Delta Tissue team and will not be interoperable with other linked data
# sources.

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX patient: <http://patient.delta-tissue.org/subject>
PREFIX ancestry: <http://vocabulary.delta-tissue.org/ancestry/>
PREFIX ethnicity: <http://vocabulary.delta-tissue.org/ethnicity/>
PREFIX bodypart: <http://vocabulary.delta-tissue.org/bodypart/>
PREFIX diagnosis: <http://vocabulary.delta-tissue.org/diagnosis/>
PREFIX specimen: <http://vocabulary.delta-tissue.org/specimen/>
PREFIX measurement: <http://vocabulary.delta-tissue.org/measurement/>
PREFIX treatment: <http://vocabulary.delta-tissue.org/treatment/>
PREFIX imaging: <http://vocabulary.delta-tissue.org/imaging/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX dcterms: <http://purl.org/dc/terms/>

patient:Subject {
   patient:dob						xsd:DateTime;
   patient:measurement              @patient:Measurement* ;
   patient:ancestry   				[ ancestry:European
     								  ancestry:African
									  ancestry:Asian
									  ancestry:Middle_Eastern
									  ancestry:Indigenous
									  ancestry:Pacific_Islander
									  ancestry:East_Asian
                                    ]?;
   patient:Ethnicity				[
    								  ethnicity:Hispanic
                             		  ethnicity:Carribbean
  									]?;
  patient:archived_specimen 		@patient:Archived_Specimen* ;
  patient:treatment 		 		@patient:Treatment* ;
  patient:imaging 			 		@patient:Imaging* ;
  patient:prior_history_of_cancer	@patient:Prior_history_of_cancer* ;
  patient:genetic_Test				@patient:Genetic_Test* ;
  patient:family_history			@patient:Family_history* ;
  patient:metabolic				    @patient:Metabolic ;
  patient:parity					@patient:Parity ;
  patient:hypoxia_time				@patient:Hypoxia_time ;
  patient:formalin_fixation_time 	@patient:Formalin_fixation_time ;

}

patient:Archived_Specimen {
  patient:diagnosis				    @patient:Diagnosis ;
  patient:specimen					@patient:Specimen ;
}

patient:Diagnosis {
  patient:locality					[
    									bodypart:Left_breast
    									bodypart:Right_breast
  									];
  rdf:type							[
     									diagnosis:Invasive_cancer
    									diagnosis:Atypia
    									diagnosis:In_situ_cancer
    									diagnosis:Prophylactic_mastectomy_for_high_risk
								    ];
}

patient:Specimen {
  	specimen:collection_method		[
  										specimen:Biopsy
  										specimen:Mastectomy
];
    patient:locality					[
    									bodypart:Left_breast
    									bodypart:Right_breast
  									];
  	patient:measurement                 @patient:Measurement ;
  	patient:HER2                    [
  	                                    measurement:FISH
  	                                    measurement:IHC
  	                                ] ;
   patient:stage                    [
                                        measurement:0
                                        measurement:1
                                        measurement:2
                                        measurement:3
                                        measurement:4
                                    ]
}

patient:Measurement {
   rdf:type                         [
                                        measurement:ER
                                        measurement:PR
                                        measurement:Ki67
                                        measurement:BMI
                                        measurement:HgbA1c
                                        measurement:gravida
                                        measurement:para
                                        measurement:year_last_delivery
                                        measurement:hypoxia_time
                                        measurement:Formaline_fixation_time
                                    ] ;
   rdf:value                        rdfs:literal ;
   rdfs:comment                     xsd:string ;
}

patient:Treatment {
   rdf:type                         [
                                        treatment:adjuvant
                                        treatment:neoadjuvant
                                    ] ;
   patient:metastasis               @diagnosis:Metastasis ;

}

diagnosis:Metastasis {
    diagnosis:date_of_diagnosis     xsd:dateTime ;
    patient:locality                [
                                        bodypart:Bone
                                        bodypart:Lung
                                        bodypart:Liver
                                    ] ;
}

patient:Imaging {
    diagnosis:date_of_imaging   xsd:dateTime ;
    imaging:modality            [
                                    imaging:Ultrasound
                                    imaging:MRI
                                    imaging:PACT
    ]

}

patient:Prior_history_of_cancer {
     patient:prior_cancer_history   @patient:cancer_episode ;
}

patient:cancer_episode {
    diagnosis:date                  xsd:dateTime ;
    diagnosis:diagnosis             [
                                        diagnosis:Breast_cancer
                                        diagnosis:Ovarian_cancer
                                        diagnosis:other_cancer
                                    ];
    rdfs:comment                     xsd:string ;
}
``` 

### Schema using Open Biomedical Ontologies (OBOFoundry)
[The Open Biological and Biomedical Ontologies (OBO) Foundry](https://en.wikipedia.org/wiki/OBO_Foundry) provides a collection of curated and interlinked biomedical ontologies that can be searched from various search engines. We have use the [Ontology Lookup Service (OLS)](https://www.ebi.ac.uk/ols/index) provided by the European Bioinformatics Institute. We used the terms used in the provided breast-metadata spreadsheet and used those as search term in the OLS. The OLS then returned a series of potentially applicable ontology terms.

```shex
PREFIX ncit: <http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#>
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX patient: <http://patient.deltatissue.org/subject>
PREFIX specimen: <http://patient.deltatissue.org/specimen>
PREFIX treatment: <http://patient.deltatissue.org/treatment>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dce: <http://purl.org/dc/elements/1.1/>
# Author: Andra Waagemeester
# Based on: https://docs.google.com/spreadsheets/d/1Ivb14Pac_ADLaAuysPvulYtGAAbzE8ffludVfMLt6HM/edit#gid=397194
# This model is fully based on OBO

patient:id {
    rdf:type [obo:NCIT_C16960] ; # Patient
    patient:patient_property @patient:Age ; # patient:property needs to be defined by dt
    patient:patient_property @patient:Ancestry ;
    patient:patient_property @patient:Ethnicity ;
    obo:OBI_0100051 @patient:archived_specimen ; # Property Specimen
}

patient:Age {
    rdf:type [obo:NCIT_C25150] ; # Age
    rdf:value xsd:int ;
}

patient:Ancestry {
   rdf:type [obo:NCIT_C176763] ;
   rdf:value [
                obo:NCIT_C41260 # Asian"
                obo:NCIT_C128991 # Black Central American"
                obo:NCIT_C128992 # Black South American"
                obo:NCIT_C16352 # Black or African American"
                obo:NCIT_C41261 # White"
                obo:NCIT_C67109 # Multiracial"
                obo:NCIT_C77809 # South or Central American Indian"
                obo:NCIT_C77810 # Caribbean Indian"
                obo:NCIT_C77811 # Mediterranean"
                obo:NCIT_C77812 # North American"
                obo:NCIT_C77813 # North Coast of Africa"
                obo:NCIT_C77814 # Northern European"
                obo:NCIT_C77815 # Black South or Central American"
                obo:NCIT_C77816 # White Caribbean"
                obo:NCIT_C77817 # Western European"
                obo:NCIT_C77818 # White South or Central American"
                obo:NCIT_C77819 # Eastern European"
                obo:NCIT_C77820 # Middle Eastern"
                obo:NCIT_C16310 # Asian American"
                obo:NCIT_C104495 # Other Race"
                obo:NCIT_C126531 # Latin American"
                obo:NCIT_C126532 # South American"
                obo:NCIT_C126535 # Australian"
                obo:NCIT_C126536 # New Zealander"
                obo:NCIT_C126537 # Icelander"
                obo:NCIT_C126538 # Scandinavian"
                obo:NCIT_C42331 # African"
                obo:NCIT_C41259 # American Indian or Alaska Native"
                obo:NCIT_C41226 # African Caribbean"
                obo:NCIT_C43390 # Eskimo"
                obo:NCIT_C43851 # European"
                obo:NCIT_C43866 # Middle Eastern or North African"
               ]
}

patient:Ethnicity {
   rdf:type    [obo:NCIT_C16564 ] ;
   rdf:value   [
                obo:SCDO_1000116 # "Adja"
                obo:SCDO_1000117 # "Bariba"
                obo:SCDO_1000118 # "Dendi"
                obo:SCDO_1000119 # "Fon"
                obo:SCDO_1000120 # "Yoa"
                obo:SCDO_1000121 # "Betamaribe"
                obo:SCDO_1000122 # "Embu"
                obo:SCDO_1000123 # "Kalenjin"
                obo:SCDO_1000124 # "Kamba"
                obo:SCDO_1000125 # "Kikuyu"
                obo:SCDO_1000126 # "Kisii"
                obo:SCDO_1000127 # "Luhya"
                obo:SCDO_1000128 # "Luo"
                obo:SCDO_1000129 # "Maasai"
                obo:SCDO_1000130 # "Peulh"
                obo:SCDO_1000131 # "Yoruba"
                obo:SCDO_1000132 # "Meru"
                obo:SCDO_1000133 # "Mijikenda/Swahili"
                obo:SCDO_1000134 # "Somali"
                obo:SCDO_1000135 # "Taita/Taveta"
                obo:SCDO_1000136 # "Borana"
                obo:SCDO_1000137 # "Maragoli"
                obo:SCDO_1000138 # "Pokot"
                obo:SCDO_1000139 # "Turkana"
                obo:SCDO_1000141 # "Bassa"
                obo:NCIT_C17459 # "Hispanic or Latino"
                obo:NCIT_C158158 # "Han Chinese"
                obo:NCIT_C158159 # "Zhuang Chinese"
                obo:NCIT_C158160 # "Hui Chinese"
                obo:NCIT_C158161 # "Man Chinese"
                obo:NCIT_C158162 # "Uygur Chinese"
                obo:NCIT_C158163 # "Miao Chinese"
                obo:NCIT_C158164 # "Yi Chinese"
                obo:NCIT_C158165 # "Tujia Chinese"
                obo:NCIT_C158166 # "Zang Chinese"
                obo:NCIT_C158167 # "Mongol Chinese"
                obo:NCIT_C158168 # "Dong Chinese"
                obo:NCIT_C158169 # "Buyei Chinese"
                obo:NCIT_C158170 # "Yao Chinese"
                obo:NCIT_C158171 # "Bai Chinese"
                obo:NCIT_C158172 # "Chosen Chinese"
                obo:NCIT_C158173 # "Hani Chinese"
                obo:NCIT_C158174 # "Li Chinese"
                obo:NCIT_C158175 # "Kazak Chinese"
                obo:NCIT_C158176 # "Dai Chinese"
                obo:NCIT_C158177 # "She Chinese"
                obo:NCIT_C158178 # "Lisu Chinese"
                obo:NCIT_C158179 # "Dongxiang Chinese"
                obo:NCIT_C158180 # "Gelao Chinese"
                obo:NCIT_C158181 # "Lahu Chinese"
                obo:NCIT_C158182 # "Va Chinese"
                obo:NCIT_C158183 # "Sui Chinese"
                obo:NCIT_C158184 # "Naxi Chinese"
                obo:NCIT_C158185 # "Qiang Chinese"
                obo:NCIT_C158186 # "Tu Chinese"
                obo:NCIT_C158187 # "Mulao Chinese"
                obo:NCIT_C158188 # "Xibe Chinese"
                obo:NCIT_C158189 # "Kirgiz Chinese"
                obo:NCIT_C158190 # "Jingpo Chinese"
                obo:NCIT_C158191 # "Daur Chinese"
                obo:NCIT_C158192 # "Salar Chinese"
                obo:NCIT_C158193 # "Blang Chinese"
                obo:NCIT_C158194 # "Maonan Chinese"
                obo:NCIT_C158195 # "Tajik Chinese"
                obo:NCIT_C158196 # "Pumi Chinese"
                obo:NCIT_C158197 # "Achang Chinese"
                obo:NCIT_C158198 # "Nu Chinese"
                obo:NCIT_C158199 # "Ewenki Chinese"
                obo:NCIT_C158200 # "Gin Chinese"
                obo:NCIT_C158201 # "Jino Chinese"
                obo:NCIT_C158202 # "Deang Chinese"
                obo:NCIT_C158203 # "Bonan Chinese"
                obo:NCIT_C158204 # "Russ Chinese"
                obo:NCIT_C158205 # "Yugur Chinese"
                obo:NCIT_C158206 # "Uzbek Chinese"
                obo:NCIT_C158207 # "Monba Chinese"
                obo:NCIT_C158208 # "Oroqen Chinese"
                obo:NCIT_C158209 # "Derung Chinese"
                obo:NCIT_C158210 # "Hezhen Chinese"
                obo:NCIT_C158211 # "Gaoshan Chinese"
                obo:NCIT_C158212 # "Lhoba Chinese"
                obo:NCIT_C158213 # "Tatar Chinese"
                obo:NCIT_C128457 # "American Ethnicity"
                obo:NCIT_C128458 # "Australian/New Zealand Ethnicity"
                obo:NCIT_C128459 # "Intercontinental Ethnicity"
                obo:NCIT_C103283 # "Sephardic Jew"
                obo:NCIT_C17950 # "Ashkenazi Jew"
                obo:NCIT_C41222 # "Not Hispanic or Latino"
  ]
}

patient:archived_specimen {
    rdf:type [obo:NCIT_C19157] ;
    obo:RO_0040035 @patient:diagnosis ; # disease relationship
    obo:HSO_0000288 @specimen:collection_method ; # has sample collection protocol
    obo:TXPO_0001873 @specimen:Measurement ; # has finding
    obo:NCIT_R165 @specimen:Imaging ; # Procedure_Has_Imaged_Anatomy
}

patient:diagnosis {
   rdf:type     [obo:DOID_4] ;
   rdf:value    [
                    obo:NCIT_C27093 # "Stage 0 Squamous Cell Carcinoma"
                    obo:NCIT_C27282 # "Stage 0 AIDS-Related Anal Canal Cancer AJCC v6 and v7"
                    obo:NCIT_C27467 # "Stage 0 Lung Cancer AJCC v6 and v7"
                    obo:NCIT_C27790 # "Penile Carcinoma In Situ"
                    obo:NCIT_C28292 # "Squamous Cell Carcinoma In Situ of the Nipple"
                    obo:NCIT_C2906 # "Skin Squamous Cell Carcinoma In Situ"
                    obo:NCIT_C2917 # "Carcinoma In Situ"
                    obo:NCIT_C35758 # "Stage 0 Lung Large Cell Carcinoma AJCC v6 and v7"
                    obo:NCIT_C3637 # "Stage 0 Esophageal Cancer AJCC v6"
                    obo:NCIT_C3638 # "Stage 0 Colon Cancer AJCC v6 and v7"
                    obo:NCIT_C3639 # "Tracheal Carcinoma In Situ"
                    obo:NCIT_C3640 # "Stage 0 Skin Cancer"
                    obo:NCIT_C3641 # "Stage 0 Breast Cancer AJCC v6 and v7"
                    obo:NCIT_C3642 # "Grade III Prostatic Intraepithelial Neoplasia"
                    obo:NCIT_C3644 # "Stage 0is Bladder Urothelial Carcinoma AJCC v6 and v7"
                    obo:NCIT_C4000 # "Stage 0 Cervical Cancer AJCC v6"
                    obo:NCIT_C4520 # "Cervical Adenocarcinoma In Situ"
                    obo:NCIT_C4522 # "Stage 0 Vulvar Cancer AJCC v6"
                    obo:NCIT_C4529 # "Stage 0is Ureter Cancer AJCC v7"
                    obo:NCIT_C4531 # "Stage 0is Urethral Cancer AJCC v7"
                    obo:NCIT_C4588 # "Stage 0 Lip Cancer AJCC v6 and v7"
                    obo:NCIT_C4590 # "Stage 0 Oropharyngeal Carcinoma AJCC v6 and v7"
                    obo:NCIT_C4592 # "Stage 0 Epiglottic Carcinoma AJCC v6, v7, and v8"
                    obo:NCIT_C4593 # "Stage 0 Appendix Carcinoma AJCC v7"
                    obo:NCIT_C4594 # "Cecum Carcinoma In Situ"
                    obo:NCIT_C4597 # "Stage 0is Renal Pelvis Cancer AJCC v7"
                    obo:NCIT_C4853 # "Stage 0 Rectal Cancer AJCC v6 and v7"
                    obo:NCIT_C4892 # "Stage 0 Small Intestinal Cancer AJCC v7"
                    obo:NCIT_C5017 # "Stage 0 Rectosigmoid Cancer AJCC v6 and v7"
                    obo:NCIT_C5023 # "Stage 0 Esophageal Squamous Cell Carcinoma AJCC v7"
                    obo:NCIT_C5137 # "Breast Ductal Carcinoma In Situ, Non-Comedo Type"
                    obo:NCIT_C5138 # "Breast Ductal Carcinoma In Situ, Cribriform Pattern"
                    obo:NCIT_C5139 # "Breast Micropapillary Ductal Carcinoma In Situ"
                    obo:NCIT_C8932 # "Stage 0 Colorectal Cancer AJCC v6 and v7"
                    obo:NCIT_C9099 # "Stage 0 Nasopharyngeal Carcinoma AJCC v6, v7, and v8"
                    obo:NCIT_C9101 # "Stage 0 Hypopharyngeal Carcinoma AJCC v6, v7, and v8"
                    obo:NCIT_C9104 # "Stage 0 Lung Non-Small Cell Cancer AJCC v6 and v7"
                    obo:NCIT_C132783 # "Stage 0 Major Salivary Gland Cancer AJCC v8"
                    obo:NCIT_C132995 # "Stage 0 Oropharyngeal (p16-Negative) Carcinoma AJCC v8"
                    obo:NCIT_C133519 # "Pathologic Stage 0 Esophageal Squamous Cell Carcinoma AJCC v8"
                    obo:NCIT_C2924 # "Breast Ductal Carcinoma In Situ"
                    obo:NCIT_C35180 # "Digestive System Carcinoma In Situ"
                    obo:NCIT_C4439 # "Stage 0 Gallbladder Cancer AJCC v6 and v7"
                    obo:NCIT_C4587 # "Stage 0 Oral Cavity Cancer AJCC v6 and v7"
                    obo:NCIT_C4942 # "Stage 0 Pharyngeal Cancer"
                    obo:NCIT_C6877 # "Grade III Glandular Intraepithelial Neoplasia"
                    obo:NCIT_C7939 # "Stage 0 Lip and Oral Cavity Cancer AJCC v6 and v7"
                    obo:NCIT_C137839 # "Breast Pleomorphic Lobular Carcinoma In Situ"
                    obo:NCIT_C7788 # "Stage 0 Gastric Cancer AJCC v6 and v7"
                    obo:NCIT_C7794 # "Stage 0 Anal Canal Cancer AJCC v6 and v7"
                    obo:NCIT_C89550 # "Stage 0 Cervical Cancer AJCC v7"
                    obo:NCIT_C89771 # "Stage 0 Esophageal Cancer AJCC v7"
                    obo:NCIT_C9100 # "Stage 0 Laryngeal Cancer AJCC v6, v7, and V8"
                    obo:NCIT_C61602 # "Atypia Confined to the Basal and Parabasal Epithelial Layers"
                    obo:NCIT_C35989 # "Nuclear Atypia"
                    obo:NCIT_C8329 # "Severe Cytologic Atypia"
                    obo:NCIT_C8351 # "Koilocytotic Atypia"
                    obo:NCIT_C51139 # "Marked Nuclear Atypia Present"
                    obo:NCIT_C8327 # "Mild Cytologic Atypia"
                    obo:NCIT_C8328 # "Moderate Cytologic Atypia"
                    obo:NCIT_C9478 # "Atypia"
                    obo:NCIT_C8331 # "Mild Squamous Cell Atypia"
                    obo:NCIT_C8332 # "Moderate Squamous Cell Atypia"
                    obo:NCIT_C8333 # "Severe Squamous Cell Atypia"
                    obo:NCIT_C8337 # "Columnar Cell Atypia"
                    obo:NCIT_C8338 # "Mild Columnar Cell Atypia"
                    obo:NCIT_C8339 # "Moderate Columnar Cell Atypia"
                    obo:NCIT_C8340 # "Severe Columnar Cell Atypia"
                    obo:NCIT_C8342 # "Mild Glandular Cell Atypia"
                    obo:NCIT_C8343 # "Moderate Glandular Cell Atypia"
                    obo:NCIT_C8344 # "Severe Glandular Cell Atypia"
                    obo:NCIT_C8345 # "Transitional Cell Atypia"
                    obo:NCIT_C8346 # "Mild Transitional Cell Atypia"
                    obo:NCIT_C8347 # "Moderate Transitional Cell Atypia"
                    obo:NCIT_C8348 # "Severe Transitional Cell Atypia"
                    obo:NCIT_C8349 # "Post-Radiation Cytologic Changes with Dysplasia"
                    obo:NCIT_C8350 # "Atypia Suspicious for Malignancy"
                    obo:NCIT_C8352 # "Mild Koilocytotic Atypia"
                    obo:NCIT_C8448 # "Mesenchymal Cell Atypia"
                    obo:NCIT_C8450 # "Smooth Muscle Cell Atypia"
                    obo:NCIT_C8452 # "Striated Muscle Cell Atypia"
                    obo:NCIT_C8454 # "Fibroblastic Cell Atypia"
                    obo:NCIT_C8341 # "Glandular Cell Atypia"
                    obo:NCIT_C3975 # "Cervical Atypia"
                    obo:NCIT_C8326 # "Cytologic Atypia"
                    obo:NCIT_C8330 # "Squamous Cell Atypia"
                    obo:NCIT_C115966 # "Infiltrating Bladder Urothelial Carcinoma Associated with Urethral Carcinoma"
                    obo:NCIT_C123160 # "Lepidic Adenocarcinoma"
                    obo:NCIT_C27202 # "Infiltrating Bladder Urothelial Carcinoma, Micropapillary Variant"
                    obo:NCIT_C27474 # "Non-Muscle Invasive Bladder Carcinoma"
                    obo:NCIT_C27829 # "Invasive Breast Carcinoma by Histologic Grade"
                    obo:NCIT_C27830 # "Grade 1 Invasive Breast Carcinoma"
                    obo:NCIT_C27831 # "Grade 2 Invasive Breast Carcinoma"
                    obo:NCIT_C27832 # "Grade 3 Invasive Breast Carcinoma"
                    obo:NCIT_C27885 # "Infiltrating Bladder Urothelial Carcinoma"
                    obo:NCIT_C27905 # "Well Differentiated Prostate Adenocarcinoma"
                    obo:NCIT_C27906 # "Moderately Differentiated Prostate Adenocarcinoma"
                    obo:NCIT_C27916 # "Poorly Differentiated Prostate Adenocarcinoma"
                    obo:NCIT_C36084 # "Invasive Breast Micropapillary Carcinoma"
                    obo:NCIT_C36085 # "Invasive Breast Papillary Carcinoma"
                    obo:NCIT_C39816 # "Infiltrating Bladder Urothelial Carcinoma with Squamous Differentiation"
                    obo:NCIT_C39817 # "Infiltrating Bladder Urothelial Carcinoma with Glandular Differentiation"
                    obo:NCIT_C39818 # "Infiltrating Bladder Urothelial Carcinoma with Trophoblastic Differentiation"
                    obo:NCIT_C39819 # "Infiltrating Bladder Urothelial Carcinoma, Nested Variant"
                    obo:NCIT_C39820 # "Infiltrating Bladder Urothelial Carcinoma, Microcystic Variant"
                    obo:NCIT_C39821 # "Infiltrating Bladder Lymphoepithelioma-Like Carcinoma"
                    obo:NCIT_C39822 # "Infiltrating Bladder Urothelial Carcinoma, Lymphoma-Like Variant"
                    obo:NCIT_C39823 # "Infiltrating Bladder Urothelial Carcinoma, Plasmacytoid Variant"
                    obo:NCIT_C39824 # "Infiltrating Bladder Urothelial Carcinoma, Sarcomatoid Variant"
                    obo:NCIT_C39825 # "Infiltrating Bladder Urothelial Carcinoma, Sarcomatoid Variant with Heterologous Elements"
                    obo:NCIT_C39826 # "Infiltrating Bladder Urothelial Carcinoma, Sarcomatoid Variant without Heterologous Elements"
                    obo:NCIT_C39827 # "Infiltrating Bladder Urothelial Carcinoma, Clear Cell Variant"
                    obo:NCIT_C39828 # "Infiltrating Bladder Urothelial Carcinoma, Lipid-Rich Variant"
                    obo:NCIT_C39829 # "Infiltrating Bladder Urothelial Carcinoma with Giant Cells"
                    obo:NCIT_C39853 # "Infiltrating Urothelial Carcinoma"
                    obo:NCIT_C39879 # "Infiltrating Renal Pelvis and Ureter Urothelial Carcinoma"
                    obo:NCIT_C39880 # "Prostate Acinar Adenocarcinoma, Atrophic Variant"
                    obo:NCIT_C39881 # "Prostate Acinar Adenocarcinoma, Pseudohyperplastic Variant"
                    obo:NCIT_C39882 # "Prostate Acinar Adenocarcinoma, Foamy Gland Variant"
                    obo:NCIT_C39884 # "Prostate Acinar Adenocarcinoma, Oncocytic Variant"
                    obo:NCIT_C39885 # "Prostate Acinar Adenocarcinoma, Lymphoepithelioma-Like Variant"
                    obo:NCIT_C39895 # "Prostate Ductal Adenocarcinoma, Cribriform Pattern"
                    obo:NCIT_C39896 # "Prostate Ductal Adenocarcinoma, Papillary Pattern"
                    obo:NCIT_C39897 # "Prostate Ductal Adenocarcinoma, Solid Pattern"
                    obo:NCIT_C39902 # "Prostate Basal Cell Carcinoma"
                    obo:NCIT_C39903 # "Prostate Adenocarcinoma with Neuroendocrine Differentiation"
                    obo:NCIT_C4001 # "Breast Inflammatory Carcinoma"
                    obo:NCIT_C4536 # "Pituitary Gland Carcinoma"
                    obo:NCIT_C47847 # "Breast Carcinoma with Chondroid Metaplasia"
                    obo:NCIT_C47848 # "Breast Carcinoma with Osseous Metaplasia"
                    obo:NCIT_C5142 # "Invasive Breast Cribriform Carcinoma"
                    obo:NCIT_C5161 # "Breast Pleomorphic Carcinoma"
                    obo:NCIT_C5163 # "Breast Adenocarcinoma with Squamous Metaplasia"
                    obo:NCIT_C5167 # "High Grade Breast Mucoepidermoid Carcinoma"
                    obo:NCIT_C5168 # "Low Grade Breast Mucoepidermoid Carcinoma"
                    obo:NCIT_C5176 # "Metastatic Breast Signet Ring Cell Carcinoma"
                    obo:NCIT_C5178 # "Metastatic Breast Squamous Cell Carcinoma"
                    obo:NCIT_C5457 # "Invasive Breast Apocrine Carcinoma"
                    obo:NCIT_C54691 # "Invasive Breast Lobular Carcinoma, Signet Ring Variant"
                    obo:NCIT_C5530 # "Prostate Acinar Adenocarcinoma, Sarcomatoid Variant"
                    obo:NCIT_C5597 # "Prostate Undifferentiated Carcinoma"
                    obo:NCIT_C5649 # "Lung Acinar Adenocarcinoma"
                    obo:NCIT_C6987 # "Breast Ductal Carcinoma with Squamous Metaplasia"
                    obo:NCIT_C5536 # "Prostate Squamous Cell Carcinoma"
                    obo:NCIT_C162531 # "Invasive Adenocarcinoma in Adenomatous Polyp"
                    obo:NCIT_C171012 # "Recurrent Prostate Adenocarcinoma"
                    obo:NCIT_C9480 # "Invasive Carcinoma"
                    obo:NCIT_C7362 # "Breast Scirrhous Carcinoma"
                    obo:NCIT_C9135 # "Breast Tubular Carcinoma"
                    obo:NCIT_C156123 # "Thyroid Gland Follicular Carcinoma, Widely Invasive"
                    obo:NCIT_C156286 # "Advanced Prostate Adenocarcinoma"
                    obo:NCIT_C156287 # "Locally Advanced Prostate Adenocarcinoma"
                    obo:NCIT_C156289 # "Locally Advanced Unresectable Prostate Adenocarcinoma"
                    obo:NCIT_C46070 # "Contralateral Prophylactic Mastectomy"
                    obo:NCIT_C46072 # "Bilateral Prophylactic Mastectomy"
                    obo:NCIT_C94445 # "Prophylactic Mastectomy"
   ]
}

specimen:collection_method {
    rdfs:comment    xsd:string ;
    rdf:type [obo:NCIT_C70700 ] ; # Biospecimen Collection Method
    rdf:value [
            obo:NCIT_C15189 # Biopsy
            obo:NCIT_C51496 # "Left Radical Mastectomy"
            obo:NCIT_C51499 # "Right Radical Mastectomy"
            obo:NCIT_C15279 # "Radical Mastectomy"
            obo:NCIT_C51633 # "Excisional Biopsy of Breast"
            ## No distinction between left and right in NCIT
            obo:NCIT_C51698 # "Biopsy of Breast"
            obo:NCIT_C137849 # "Biopsy of Nipple and Areola"
            obo:NCIT_C137850 # "Full-thickness Skin Biopsy of Nipple and Areola"
            obo:NCIT_C137851 # "Core Biopsy of Breast"
    ]
}

specimen:Measurement {
    rdfs:comment    xsd:string ;
    rdf:type [obo:NCIT_C25209] ; # Measurement
    rdfs:domain [
                  obo:NCIT_C123557 # Ki67 Measurement
                  obo:NCIT_C184942 # HER2 Copy Number Measurement
                  obo:NCIT_C16149 # Progesterone Receptor Status
                  obo:NCIT_C16150 # Estrogen Receptor Status
                  obo:NCIT_C16899 # Stage
                  obo:NCIT_C103223 # Genetic Finding
                  obo:NCIT_C168828 # Reported BMI
                  obo:NCIT_C122507 # Hemoglobin A1c Increased
    ] ;
    rdf:value LITERAL ;
}

patient:Treatment {
    rdfs:comment    xsd:string ;
    obo:NCIT_P302 @patient:archived_specimen ; # Accepted_Therapeutic_Use_For
    rdf:type [obo:NCIT_C25409] ;
    rdfs:range @treatment:Neoadjuvant or @treatment:Adjuvant or @treatment:Metastasis ;
}

treatment:Neoadjuvant {
   rdfs:comment    xsd:string ;
   rdfs:range [
                obo:NCIT_C15632  #chemotherapy
                obo:NCIT_C15445  # Hormone Therapy
                obo:NCIT_C123603  # Pathologic Complete Response
   ] ;
}

treatment:Adjuvant {
    rdfs:comment    xsd:string ;
    rdfs:range [
                obo:NCIT_C15632  #chemotherapy
                obo:NCIT_C15445  # Hormone Therapy
                obo:NCIT_C123633  # Disease Recurrence Relative Location
    ] ;
}

treatment:Metastasis {
   dce:date     xsd:dateTime ;
   rdf:type     [obo:NCIT_C19151] ; # Metastasis
   rdfs:comment    xsd:string ;
   obo:RO_0001025 [
                    obo:NCIT_C12366 # Bone
                    obo:NCIT_C12468 # Lung
                    obo:NCIT_C12392 # Liver

   ]
}

specimen:Imaging {
   dce:date     xsd:dateTime ;

   rdf:range      [
                    obo:NCIT_C64384 # Ultrasound
                    obo:NCIT_C29934 # Magnetic Resonance Spectroscopic Imaging
                    obo:NCIT_C116443 # Thermoacoustic Computed Tomography
   ];
   rdfs:comment    xsd:string ;
}
```

### Schema using various schema providers, controlled vocabularies and ontologies. 

Other extensive resources providing uniform identifiers and schema patterns exists. Examples are:
* [schema.org](https://schema.org) e.g. [Patient](https://schema.org/Patient)
* [FHIR](https://www.hl7.org/) e.g. [Patient](https://www.hl7.org/fhir/patient.html)
* SNOMED [^1] [e.g. Patient](http://snomed.info/id/116154003)
* SIO [^1] [e.g. patient](http://semanticscience.org/resource/SIO_000393)

### Conclussions
A Linked data is a data stored on a machine readable format of triples that use uniform identifier to remove ambiguity. The identifiers link to definitions described in controlled vocabularies and ontologies. To describe the relationships or data patterns between the identifiers triples, schemas are used. In this document we have described two of such schemas. One where the identifiers (and definitions) are completely created within the project. The second use terms from the OBOFoundry ontologies. We also described other potential sources for ontological terms. 
The final ΔTissue schema will be a mix of those. The terms here were selected us who lack detailed knowledge about the described domain (i.e. breast cancer). Moving forward requires input from domain experts while going through the definitions described in the various ontologies. 








[^1]: Can also be search with the OLS
