# Auto generated from model.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-10-12T15:38:33
# Schema: gbm
#
# id: https://wellcomeleap.org/delta-tissue/models/mdr/gbm
# description: Delta Tissue MDR model for glioblatoma data.
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Date, Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = "0.0.1"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ECOGSTATUS = CurieNamespace('ECOGStatus', 'http://example.org/UNKNOWN/ECOGStatus/')
SPECIMENENUM = CurieNamespace('SpecimenEnum', 'http://example.org/UNKNOWN/SpecimenEnum/')
BOOLEAN = CurieNamespace('boolean', 'http://example.org/UNKNOWN/boolean/')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
EFO = CurieNamespace('efo', 'http://www.ebi.ac.uk/efo/')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
GBM = CurieNamespace('gbm', 'https://wellcomeleap.org/delta-tissue/ns/gbm/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MDR = CurieNamespace('mdr', 'https://wellcomeleap.org/delta-tissue/ns/mdr/')
OBO = CurieNamespace('obo', 'http://purl.obolibrary.org/obo/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'https://schema.org/')
SIO = CurieNamespace('sio', 'http://semanticscience.org/resource/')
WDT = CurieNamespace('wdt', 'http://www.wikidata.org/prop/direct/')
DEFAULT_ = GBM

# Helper
def _instantiate(v, base_type):
    if isinstance(v, base_type):
        return v
    else:
        obj = dict(as_dict(v)) # Copy
        if "@type" in obj:
            type_name = obj.pop('@type')
            base_type = globals()[type_name]
        return base_type(**obj)

# Types

# Class references
class GBMSubjectSubjectId(URIorCURIE):
    pass


class DatafileUri(extended_str):
    pass


class FormatUri(extended_str):
    pass


class BaseSubjectSubjectId(URIorCURIE):
    pass


@dataclass
class GBMSubject(YAMLRoot):
    """
    Central class of the MDR model, or "Patient".
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBO.NCIT_C16960
    class_class_curie: ClassVar[str] = "obo:NCIT_C16960"
    class_name: ClassVar[str] = "GBMSubject"
    class_model_uri: ClassVar[URIRef] = GBM.GBMSubject

    subject_id: Union[str, GBMSubjectSubjectId] = None
    subject_properties: Optional[Union[dict, "GBMProperties"]] = None
    source_site: Optional[Union[str, List[str]]] = empty_list()
    source_datafile: Optional[Union[str, DatafileUri]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject_id):
            self.MissingRequiredField("subject_id")
        if not isinstance(self.subject_id, GBMSubjectSubjectId):
            self.subject_id = GBMSubjectSubjectId(self.subject_id)

        if self.subject_properties is not None and not isinstance(self.subject_properties, GBMProperties):
            self.subject_properties = _instantiate(self.subject_properties, GBMProperties)

        if not isinstance(self.source_site, list):
            self.source_site = [self.source_site] if self.source_site is not None else []
        self.source_site = [v if isinstance(v, str) else str(v) for v in self.source_site]

        if self.source_datafile is not None and not isinstance(self.source_datafile, DatafileUri):
            self.source_datafile = DatafileUri(self.source_datafile)

        super().__post_init__(**kwargs)


@dataclass
class GBMProperties(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GBM.GBMProperties
    class_class_curie: ClassVar[str] = "gbm:GBMProperties"
    class_name: ClassVar[str] = "GBMProperties"
    class_model_uri: ClassVar[URIRef] = GBM.GBMProperties

    diagnosis: Optional[Union[dict, "Pathology"]] = None
    quality: Optional[Union[Union[dict, "Quality"], List[Union[dict, "Quality"]]]] = empty_list()
    birthDate: Optional[Union[str, XSDDate]] = None
    subject_age: Optional[int] = None
    subject_gender: Optional[Union[str, "GenderEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.diagnosis is not None and not isinstance(self.diagnosis, Pathology):
            self.diagnosis = _instantiate(self.diagnosis, Pathology)

        if not isinstance(self.quality, list):
            self.quality = [self.quality] if self.quality is not None else []
        self.quality = [_instantiate(v, Quality) for v in self.quality]

        if self.birthDate is not None and not isinstance(self.birthDate, XSDDate):
            self.birthDate = XSDDate(self.birthDate)

        if self.subject_age is not None and not isinstance(self.subject_age, int):
            self.subject_age = int(self.subject_age)

        if self.subject_gender is not None and not isinstance(self.subject_gender, GenderEnum):
            self.subject_gender = GenderEnum(self.subject_gender)

        super().__post_init__(**kwargs)


class Finding(YAMLRoot):
    """
    Target of a NCIT_R108 "disease has finding"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GBM.Finding
    class_class_curie: ClassVar[str] = "gbm:Finding"
    class_name: ClassVar[str] = "Finding"
    class_model_uri: ClassVar[URIRef] = GBM.Finding


@dataclass
class DiseaseResponse(Finding):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBO.NCIT_C50995
    class_class_curie: ClassVar[str] = "obo:NCIT_C50995"
    class_name: ClassVar[str] = "DiseaseResponse"
    class_model_uri: ClassVar[URIRef] = GBM.DiseaseResponse

    value: Optional[Union[Union[str, "DiseaseReponseEnum"], List[Union[str, "DiseaseReponseEnum"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.value, list):
            self.value = [self.value] if self.value is not None else []
        self.value = [v if isinstance(v, DiseaseReponseEnum) else DiseaseReponseEnum(v) for v in self.value]

        super().__post_init__(**kwargs)


@dataclass
class DieseaseProgression(Finding):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBO.NCIT_C17747
    class_class_curie: ClassVar[str] = "obo:NCIT_C17747"
    class_name: ClassVar[str] = "DieseaseProgression"
    class_model_uri: ClassVar[URIRef] = GBM.DieseaseProgression

    value: Optional[Union[Union[bool, Bool], List[Union[bool, Bool]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.value, list):
            self.value = [self.value] if self.value is not None else []
        self.value = [v if isinstance(v, Bool) else Bool(v) for v in self.value]

        super().__post_init__(**kwargs)


@dataclass
class Edamatous(Finding):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBO.PATO_0001450
    class_class_curie: ClassVar[str] = "obo:PATO_0001450"
    class_name: ClassVar[str] = "Edamatous"
    class_model_uri: ClassVar[URIRef] = GBM.Edamatous

    value: Optional[Union[Union[bool, Bool], List[Union[bool, Bool]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.value, list):
            self.value = [self.value] if self.value is not None else []
        self.value = [v if isinstance(v, Bool) else Bool(v) for v in self.value]

        super().__post_init__(**kwargs)


@dataclass
class PseudoProgression(Finding):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBO.NCIT_C98298
    class_class_curie: ClassVar[str] = "obo:NCIT_C98298"
    class_name: ClassVar[str] = "PseudoProgression"
    class_model_uri: ClassVar[URIRef] = GBM.PseudoProgression

    value: Optional[Union[Union[bool, Bool], List[Union[bool, Bool]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.value, list):
            self.value = [self.value] if self.value is not None else []
        self.value = [v if isinstance(v, Bool) else Bool(v) for v in self.value]

        super().__post_init__(**kwargs)


@dataclass
class OverallSurvival(Finding):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBO.NCIT_C125201
    class_class_curie: ClassVar[str] = "obo:NCIT_C125201"
    class_name: ClassVar[str] = "OverallSurvival"
    class_model_uri: ClassVar[URIRef] = GBM.OverallSurvival

    unit: Optional[str] = None
    value: Optional[Union[int, List[int]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if not isinstance(self.value, list):
            self.value = [self.value] if self.value is not None else []
        self.value = [v if isinstance(v, int) else int(v) for v in self.value]

        super().__post_init__(**kwargs)


@dataclass
class ProgressiveFreeSurvival(Finding):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBO.NCIT_C28234
    class_class_curie: ClassVar[str] = "obo:NCIT_C28234"
    class_name: ClassVar[str] = "ProgressiveFreeSurvival"
    class_model_uri: ClassVar[URIRef] = GBM.ProgressiveFreeSurvival

    unit: Optional[str] = None
    value: Optional[Union[int, List[int]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if not isinstance(self.value, list):
            self.value = [self.value] if self.value is not None else []
        self.value = [v if isinstance(v, int) else int(v) for v in self.value]

        super().__post_init__(**kwargs)


class History(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GBM.History
    class_class_curie: ClassVar[str] = "gbm:History"
    class_name: ClassVar[str] = "History"
    class_model_uri: ClassVar[URIRef] = GBM.History


@dataclass
class DrugUse(History):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBO.NCIT_C81246
    class_class_curie: ClassVar[str] = "obo:NCIT_C81246"
    class_name: ClassVar[str] = "DrugUse"
    class_model_uri: ClassVar[URIRef] = GBM.DrugUse

    timestamp: Optional[Union[dict, "Timestamp"]] = None
    label: Optional[str] = None
    range: Optional[str] = None
    unit: Optional[Union[str, "Term"]] = None
    value: Optional[Union[int, List[int]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.timestamp is not None and not isinstance(self.timestamp, Timestamp):
            self.timestamp = _instantiate(self.timestamp, Timestamp)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.range is not None and not isinstance(self.range, str):
            self.range = str(self.range)

        if self.unit is not None and not isinstance(self.unit, Term):
            self.unit = Term(self.unit)

        if not isinstance(self.value, list):
            self.value = [self.value] if self.value is not None else []
        self.value = [v if isinstance(v, int) else int(v) for v in self.value]

        super().__post_init__(**kwargs)


@dataclass
class Bevacizumab(History):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBO.NCIT_C2039
    class_class_curie: ClassVar[str] = "obo:NCIT_C2039"
    class_name: ClassVar[str] = "Bevacizumab"
    class_model_uri: ClassVar[URIRef] = GBM.Bevacizumab

    unit: Optional[str] = None
    value: Optional[Union[int, List[int]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if not isinstance(self.value, list):
            self.value = [self.value] if self.value is not None else []
        self.value = [v if isinstance(v, int) else int(v) for v in self.value]

        super().__post_init__(**kwargs)


@dataclass
class Temozolomide(History):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBO.NCIT_C1244
    class_class_curie: ClassVar[str] = "obo:NCIT_C1244"
    class_name: ClassVar[str] = "Temozolomide"
    class_model_uri: ClassVar[URIRef] = GBM.Temozolomide

    unit: Optional[str] = None
    value: Optional[Union[int, List[int]]] = empty_list()
    has_quality: Optional[Union[str, "Term"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if not isinstance(self.value, list):
            self.value = [self.value] if self.value is not None else []
        self.value = [v if isinstance(v, int) else int(v) for v in self.value]

        if self.has_quality is not None and not isinstance(self.has_quality, Term):
            self.has_quality = Term(self.has_quality)

        super().__post_init__(**kwargs)


@dataclass
class Localization(YAMLRoot):
    """
    Anatomical localization along with qualifiers
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBO.NCIT_C13717
    class_class_curie: ClassVar[str] = "obo:NCIT_C13717"
    class_name: ClassVar[str] = "Localization"
    class_model_uri: ClassVar[URIRef] = GBM.Localization

    value: Optional[Union[Union[str, "LocalizationEnum"], List[Union[str, "LocalizationEnum"]]]] = empty_list()
    location_qualifier: Optional[Union[str, "LocalizationEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.value, list):
            self.value = [self.value] if self.value is not None else []
        self.value = [v if isinstance(v, LocalizationEnum) else LocalizationEnum(v) for v in self.value]

        if self.location_qualifier is not None and not isinstance(self.location_qualifier, LocalizationEnum):
            self.location_qualifier = LocalizationEnum(self.location_qualifier)

        super().__post_init__(**kwargs)


class Measurement(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GBM.Measurement
    class_class_curie: ClassVar[str] = "gbm:Measurement"
    class_name: ClassVar[str] = "Measurement"
    class_model_uri: ClassVar[URIRef] = GBM.Measurement


@dataclass
class IDH(Measurement):
    """
    IDH1/IDH2 Mutation Analysis
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBO.NCIT_C157185
    class_class_curie: ClassVar[str] = "obo:NCIT_C157185"
    class_name: ClassVar[str] = "IDH"
    class_model_uri: ClassVar[URIRef] = GBM.IDH

    value: Optional[Union[Union[str, "MutationTypeEnum"], List[Union[str, "MutationTypeEnum"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.value, list):
            self.value = [self.value] if self.value is not None else []
            self.value = [v if isinstance(v, MutationTypeEnum) else MutationTypeEnum(v) for v in self.value]

        super().__post_init__(**kwargs)


@dataclass
class MGMT(Measurement):
    """
    MGMT Methylation Assay status
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBO.NCIT_C79101
    class_class_curie: ClassVar[str] = "obo:NCIT_C79101"
    class_name: ClassVar[str] = "MGMT"
    class_model_uri: ClassVar[URIRef] = GBM.MGMT

    value: Optional[Union[Union[str, "MethylationEnum"], List[Union[str, "MethylationEnum"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.value, list):
            self.value = [self.value] if self.value is not None else []
        self.value = [v if isinstance(v, MethylationEnum) else MethylationEnum(v) for v in self.value]

        super().__post_init__(**kwargs)


@dataclass
class Pathology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GBM.Pathology
    class_class_curie: ClassVar[str] = "gbm:Pathology"
    class_name: ClassVar[str] = "Pathology"
    class_model_uri: ClassVar[URIRef] = GBM.Pathology

    quality: Optional[Union[Union[dict, "Quality"], List[Union[dict, "Quality"]]]] = empty_list()
    pathology_finding: Optional[Union[Union[dict, Finding], List[Union[dict, Finding]]]] = empty_list()
    pathology_history: Optional[Union[Union[dict, History], List[Union[dict, History]]]] = empty_list()
    pathology_measurement: Optional[Union[Union[dict, Measurement], List[Union[dict, Measurement]]]] = empty_list()
    pathology_localization: Optional[Union[Union[dict, Localization], List[Union[dict, Localization]]]] = empty_list()
    pathology_specimen: Optional[Union[Union[dict, "BioSpecimen"], List[Union[dict, "BioSpecimen"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.quality, list):
            self.quality = [self.quality] if self.quality is not None else []
        self.quality = [_instantiate(v, Quality) for v in self.quality]

        if not isinstance(self.pathology_finding, list):
            self.pathology_finding = [self.pathology_finding] if self.pathology_finding is not None else []
        self.pathology_finding = [_instantiate(v, Finding) for v in self.pathology_finding]

        if not isinstance(self.pathology_history, list):
            self.pathology_history = [self.pathology_history] if self.pathology_history is not None else []
        self.pathology_history = [_instantiate(v, History) for v in self.pathology_history]

        if not isinstance(self.pathology_measurement, list):
            self.pathology_measurement = [self.pathology_measurement] if self.pathology_measurement is not None else []
        self.pathology_measurement = [_instantiate(v, Measurement) for v in self.pathology_measurement]

        if not isinstance(self.pathology_localization, list):
            self.pathology_localization = [self.pathology_localization] if self.pathology_localization is not None else []
        self.pathology_localization = [_instantiate(v, Localization) for v in self.pathology_localization]

        if not isinstance(self.pathology_specimen, list):
            self.pathology_specimen = [self.pathology_specimen] if self.pathology_specimen is not None else []
        self.pathology_specimen = [_instantiate(v, BioSpecimen) for v in self.pathology_specimen]

        super().__post_init__(**kwargs)


class GbmPathology(Pathology):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBO.DOID_3068
    class_class_curie: ClassVar[str] = "obo:DOID_3068"
    class_name: ClassVar[str] = "GbmPathology"
    class_model_uri: ClassVar[URIRef] = GBM.GbmPathology


class AiiiPathology(Pathology):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBO.FIXME
    class_class_curie: ClassVar[str] = "obo:FIXME"
    class_name: ClassVar[str] = "AiiiPathology"
    class_model_uri: ClassVar[URIRef] = GBM.AiiiPathology


@dataclass
class BioSpecimen(YAMLRoot):
    """
    Archived specimen from a subject.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBO.NCIT_C70700
    class_class_curie: ClassVar[str] = "obo:NCIT_C70700"
    class_name: ClassVar[str] = "BioSpecimen"
    class_model_uri: ClassVar[URIRef] = GBM.BioSpecimen

    value: Optional[Union[str, List[str]]] = empty_list()
    range: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.value, list):
            self.value = [self.value] if self.value is not None else []
        self.value = [v if isinstance(v, str) else str(v) for v in self.value]

        if self.range is not None and not isinstance(self.range, str):
            self.range = str(self.range)

        super().__post_init__(**kwargs)


@dataclass
class Root(YAMLRoot):
    """
    Root container for the primary identifiers in this dataset.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MDR.Root
    class_class_curie: ClassVar[str] = "mdr:Root"
    class_name: ClassVar[str] = "Root"
    class_model_uri: ClassVar[URIRef] = GBM.Root

    datasets: Optional[Union[Union[str, DatafileUri], List[Union[str, DatafileUri]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.datasets, list):
            self.datasets = [self.datasets] if self.datasets is not None else []
        self.datasets = [v if isinstance(v, DatafileUri) else DatafileUri(v) for v in self.datasets]

        super().__post_init__(**kwargs)


@dataclass
class Datafile(YAMLRoot):
    """
    Dataset definition which introduced a particular subject.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT.Dataset
    class_class_curie: ClassVar[str] = "dcat:Dataset"
    class_name: ClassVar[str] = "Datafile"
    class_model_uri: ClassVar[URIRef] = GBM.Datafile

    uri: Union[str, DatafileUri] = None
    label: Optional[str] = None
    format: Optional[Union[str, FormatUri]] = None
    issued: Optional[str] = None
    modified: Optional[str] = None
    subjects: Optional[Union[Dict[Union[str, GBMSubjectSubjectId], Union[dict, GBMSubject]], List[Union[dict, GBMSubject]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.uri):
            self.MissingRequiredField("uri")
        if not isinstance(self.uri, DatafileUri):
            self.uri = DatafileUri(self.uri)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.format is not None and not isinstance(self.format, FormatUri):
            self.format = FormatUri(self.format)

        if self.issued is not None and not isinstance(self.issued, str):
            self.issued = str(self.issued)

        if self.modified is not None and not isinstance(self.modified, str):
            self.modified = str(self.modified)

        self._normalize_inlined_as_list(slot_name="subjects", slot_type=GBMSubject, key_name="subject_id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Format(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MDR.Format
    class_class_curie: ClassVar[str] = "mdr:Format"
    class_name: ClassVar[str] = "Format"
    class_model_uri: ClassVar[URIRef] = GBM.Format

    uri: Union[str, FormatUri] = None
    label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.uri):
            self.MissingRequiredField("uri")
        if not isinstance(self.uri, FormatUri):
            self.uri = FormatUri(self.uri)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        super().__post_init__(**kwargs)


@dataclass
class BaseSubject(YAMLRoot):
    """
    Central class of the MDR model, or "Patient".
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MDR.BaseSubject
    class_class_curie: ClassVar[str] = "mdr:BaseSubject"
    class_name: ClassVar[str] = "BaseSubject"
    class_model_uri: ClassVar[URIRef] = GBM.BaseSubject

    subject_id: Union[str, BaseSubjectSubjectId] = None
    source_site: Optional[Union[str, List[str]]] = empty_list()
    source_datafile: Optional[Union[str, DatafileUri]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject_id):
            self.MissingRequiredField("subject_id")
        if not isinstance(self.subject_id, BaseSubjectSubjectId):
            self.subject_id = BaseSubjectSubjectId(self.subject_id)

        if not isinstance(self.source_site, list):
            self.source_site = [self.source_site] if self.source_site is not None else []
        self.source_site = [v if isinstance(v, str) else str(v) for v in self.source_site]

        if self.source_datafile is not None and not isinstance(self.source_datafile, DatafileUri):
            self.source_datafile = DatafileUri(self.source_datafile)

        super().__post_init__(**kwargs)


@dataclass
class BaseProperties(YAMLRoot):
    """
    Bnode representing the properties associated with a patient.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MDR.BaseProperties
    class_class_curie: ClassVar[str] = "mdr:BaseProperties"
    class_name: ClassVar[str] = "BaseProperties"
    class_model_uri: ClassVar[URIRef] = GBM.BaseProperties

    quality: Optional[Union[Union[dict, "Quality"], List[Union[dict, "Quality"]]]] = empty_list()
    birthDate: Optional[Union[str, XSDDate]] = None
    subject_age: Optional[int] = None
    subject_gender: Optional[Union[str, "GenderEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.quality, list):
            self.quality = [self.quality] if self.quality is not None else []
        self.quality = [_instantiate(v, Quality) for v in self.quality]

        if self.birthDate is not None and not isinstance(self.birthDate, XSDDate):
            self.birthDate = XSDDate(self.birthDate)

        if self.subject_age is not None and not isinstance(self.subject_age, int):
            self.subject_age = int(self.subject_age)

        if self.subject_gender is not None and not isinstance(self.subject_gender, GenderEnum):
            self.subject_gender = GenderEnum(self.subject_gender)

        super().__post_init__(**kwargs)


class Quality(YAMLRoot):
    """
    A quality that is had by a patient.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MDR.Quality
    class_class_curie: ClassVar[str] = "mdr:Quality"
    class_name: ClassVar[str] = "Quality"
    class_model_uri: ClassVar[URIRef] = GBM.Quality


@dataclass
class ECOG(Quality):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBO.NCIT_C102408
    class_class_curie: ClassVar[str] = "obo:NCIT_C102408"
    class_name: ClassVar[str] = "ECOG"
    class_model_uri: ClassVar[URIRef] = GBM.ECOG

    value: Optional[Union[str, List[str]]] = empty_list()
    range: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.value, list):
            self.value = [self.value] if self.value is not None else []
        self.value = [v if isinstance(v, str) else str(v) for v in self.value]

        if self.range is not None and not isinstance(self.range, str):
            self.range = str(self.range)

        super().__post_init__(**kwargs)


@dataclass
class Dead(Quality):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBO.NCIT_C28554
    class_class_curie: ClassVar[str] = "obo:NCIT_C28554"
    class_name: ClassVar[str] = "Dead"
    class_model_uri: ClassVar[URIRef] = GBM.Dead

    value: Optional[Union[str, List[str]]] = empty_list()
    range: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.value, list):
            self.value = [self.value] if self.value is not None else []
        self.value = [v if isinstance(v, str) else str(v) for v in self.value]

        if self.range is not None and not isinstance(self.range, str):
            self.range = str(self.range)

        super().__post_init__(**kwargs)


@dataclass
class LymphocyteCount(Quality):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EFO.EFO_0004587
    class_class_curie: ClassVar[str] = "efo:EFO_0004587"
    class_name: ClassVar[str] = "LymphocyteCount"
    class_model_uri: ClassVar[URIRef] = GBM.LymphocyteCount

    timestamp: Optional[Union[dict, "Timestamp"]] = None
    value: Optional[Union[float, List[float]]] = empty_list()
    unit: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.timestamp is not None and not isinstance(self.timestamp, Timestamp):
            self.timestamp = _instantiate(self.timestamp, Timestamp)

        if not isinstance(self.value, list):
            self.value = [self.value] if self.value is not None else []
        self.value = [v if isinstance(v, float) else float(v) for v in self.value]

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass
class Timestamp(YAMLRoot):
    """
    Sometimes the target of IAO_0000581 (TBD)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MDR.Timestamp
    class_class_curie: ClassVar[str] = "mdr:Timestamp"
    class_name: ClassVar[str] = "Timestamp"
    class_model_uri: ClassVar[URIRef] = GBM.Timestamp

    label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        super().__post_init__(**kwargs)


# Enumerations
class DiseaseReponseEnum(EnumDefinitionImpl):

    ProgressiveDisease = PermissibleValue(text="ProgressiveDisease",
                                                           meaning=OBO.NCIT_C35571)
    PartialRemission = PermissibleValue(text="PartialRemission",
                                                       meaning=OBO.NCIT_C18058)
    StableDisease = PermissibleValue(text="StableDisease",
                                                 meaning=OBO.NCIT_C18213)
    CompleteRemission = PermissibleValue(text="CompleteRemission",
                                                         meaning=OBO.NCIT_C4870)

    _defn = EnumDefinition(
        name="DiseaseReponseEnum",
    )

class ECOGStatus(EnumDefinitionImpl):

    ECOG0 = PermissibleValue(text="ECOG0",
                                 meaning=OBO.NCIT_C105722)
    ECOG1 = PermissibleValue(text="ECOG1",
                                 meaning=OBO.NCIT_C105723)

    _defn = EnumDefinition(
        name="ECOGStatus",
    )

class LocalizationEnum(EnumDefinitionImpl):

    Right = PermissibleValue(text="Right",
                                 meaning=OBO.NCIT_C25228)
    Dorsal = PermissibleValue(text="Dorsal",
                                   meaning=OBO.NCIT_C45874)
    FrontalR = PermissibleValue(text="FrontalR",
                                       meaning=OBO.NCIT_C12352)
    TemporalD = PermissibleValue(text="TemporalD",
                                         meaning=OBO.NCIT_C12353)
    ParietalR = PermissibleValue(text="ParietalR",
                                         meaning=OBO.NCIT_C12354)

    _defn = EnumDefinition(
        name="LocalizationEnum",
    )

class MethylationEnum(EnumDefinitionImpl):

    UnmethylatedMGMTGenePromoter = PermissibleValue(text="UnmethylatedMGMTGenePromoter",
                                                                               meaning=OBO.NCIT_C132892)
    MGMTGenePromoterMethylation = PermissibleValue(text="MGMTGenePromoterMethylation",
                                                                             meaning=OBO.NCIT_C153562)

    _defn = EnumDefinition(
        name="MethylationEnum",
    )

class MutationTypeEnum(EnumDefinitionImpl):

    GeneMutation = PermissibleValue(text="GeneMutation",
                                               meaning=OBO.NCIT_C18093)
    WildType = PermissibleValue(text="WildType",
                                       meaning=OBO.NCIT_C62195)

    _defn = EnumDefinition(
        name="MutationTypeEnum",
    )

class GenderEnum(EnumDefinitionImpl):

    M = PermissibleValue(text="M",
                         meaning=OBO.NCIT_C16576)
    F = PermissibleValue(text="F",
                         meaning=OBO.NCIT_C20197)
    unknown = PermissibleValue(text="unknown",
                                     description="gender is not known")

    _defn = EnumDefinition(
        name="GenderEnum",
    )

class SpecimenEnum(EnumDefinitionImpl):

    Biopsy = PermissibleValue(text="Biopsy",
                                   meaning=OBO.NCIT_C15189)
    CompleteResection = PermissibleValue(text="CompleteResection",
                                                         meaning=OBO.NCIT_C175027)
    PartialResection = PermissibleValue(text="PartialResection",
                                                       meaning=OBO.NCIT_C131680)

    _defn = EnumDefinition(
        name="SpecimenEnum",
    )

class Term(EnumDefinitionImpl):

    steroid = PermissibleValue(text="steroid",
                                     meaning=OBO.CHEBI_35341)
    Adjuvant = PermissibleValue(text="Adjuvant",
                                       meaning=OBO.NCIT_C2140)
    Cycle = PermissibleValue(text="Cycle",
                                 meaning=OBO.NCIT_C25472)
    DrugFIXME = PermissibleValue(text="DrugFIXME",
                                         meaning=OBO.UO_0000022)
    Percentage = PermissibleValue(text="Percentage",
                                           meaning=OBO.SIO_001413)
    Ki67Measurement = PermissibleValue(text="Ki67Measurement",
                                                     meaning=OBO.NCIT_C123557)
    ProgesteroneReceptorStatus = PermissibleValue(text="ProgesteroneReceptorStatus",
                                                                           meaning=OBO.NCIT_C16149)
    HER2CopyNumberMeasurement = PermissibleValue(text="HER2CopyNumberMeasurement",
                                                                         meaning=OBO.NCIT_C184942)
    EstrogenReceptorStatus = PermissibleValue(text="EstrogenReceptorStatus",
                                                                   meaning=OBO.NCIT_C16150)
    GlycosylatedHemoglobinMeasurement = PermissibleValue(text="GlycosylatedHemoglobinMeasurement",
                                                                                         meaning=OBO.NCIT_C64849)
    BodyMassIndex = PermissibleValue(text="BodyMassIndex",
                                                 meaning=OBO.NCIT_C16358)
    Gene = PermissibleValue(text="Gene",
                               meaning=OBO.NCIT_C16612)

    _defn = EnumDefinition(
        name="Term",
    )

class TimeEnum(EnumDefinitionImpl):

    Month = PermissibleValue(text="Month",
                                 meaning=OBO.NCIT_C29846)
    Minute = PermissibleValue(text="Minute",
                                   meaning=OBO.SIO_000434)

    _defn = EnumDefinition(
        name="TimeEnum",
    )

# Slots
class slots:
    pass

slots.datasets = Slot(uri=MDR.datafiles, name="datasets", curie=MDR.curie('datafiles'),
                   model_uri=GBM.datasets, domain=None, range=Optional[Union[Union[str, DatafileUri], List[Union[str, DatafileUri]]]])

slots.quality = Slot(uri=OBO.RO_0000086, name="quality", curie=OBO.curie('RO_0000086'),
                   model_uri=GBM.quality, domain=None, range=Optional[Union[Union[dict, Quality], List[Union[dict, Quality]]]])

slots.birthDate = Slot(uri=SCHEMA.birthDate, name="birthDate", curie=SCHEMA.curie('birthDate'),
                   model_uri=GBM.birthDate, domain=None, range=Optional[Union[str, XSDDate]])

slots.domain = Slot(uri=RDFS.domain, name="domain", curie=RDFS.curie('domain'),
                   model_uri=GBM.domain, domain=None, range=Optional[str])

slots.label = Slot(uri=RDFS.label, name="label", curie=RDFS.curie('label'),
                   model_uri=GBM.label, domain=None, range=Optional[str])

slots.range = Slot(uri=RDFS.range, name="range", curie=RDFS.curie('range'),
                   model_uri=GBM.range, domain=None, range=Optional[str])

slots.startDate = Slot(uri=SCHEMA.startDate, name="startDate", curie=SCHEMA.curie('startDate'),
                   model_uri=GBM.startDate, domain=None, range=Optional[Union[str, XSDDate]])

slots.timestamp = Slot(uri=OBO.IAO_0000581, name="timestamp", curie=OBO.curie('IAO_0000581'),
                   model_uri=GBM.timestamp, domain=None, range=Optional[Union[dict, Timestamp]])

slots.value = Slot(uri=RDF.value, name="value", curie=RDF.curie('value'),
                   model_uri=GBM.value, domain=None, range=Optional[Union[str, List[str]]])

slots.unit = Slot(uri=SIO.SIO_000221, name="unit", curie=SIO.curie('SIO_000221'),
                   model_uri=GBM.unit, domain=None, range=Optional[str])

slots.gBMSubject__subject_properties = Slot(uri=SIO.SIO_000223, name="gBMSubject__subject_properties", curie=SIO.curie('SIO_000223'),
                   model_uri=GBM.gBMSubject__subject_properties, domain=None, range=Optional[Union[dict, GBMProperties]])

slots.gBMProperties__diagnosis = Slot(uri=SCHEMA.diagnosis, name="gBMProperties__diagnosis", curie=SCHEMA.curie('diagnosis'),
                   model_uri=GBM.gBMProperties__diagnosis, domain=None, range=Optional[Union[dict, Pathology]])

slots.temozolomide__has_quality = Slot(uri=OBO.RO_0000086x, name="temozolomide__has_quality", curie=OBO.curie('RO_0000086x'),
                   model_uri=GBM.temozolomide__has_quality, domain=None, range=Optional[Union[str, "Term"]])

slots.localization__location_qualifier = Slot(uri=OBO.NCIT_A4, name="localization__location_qualifier", curie=OBO.curie('NCIT_A4'),
                   model_uri=GBM.localization__location_qualifier, domain=None, range=Optional[Union[str, "LocalizationEnum"]])

slots.pathology__pathology_finding = Slot(uri=OBO.NCIT_R108, name="pathology__pathology_finding", curie=OBO.curie('NCIT_R108'),
                   model_uri=GBM.pathology__pathology_finding, domain=None, range=Optional[Union[Union[dict, Finding], List[Union[dict, Finding]]]])

slots.pathology__pathology_history = Slot(uri=OBO.BFO_0000185, name="pathology__pathology_history", curie=OBO.curie('BFO_0000185'),
                   model_uri=GBM.pathology__pathology_history, domain=None, range=Optional[Union[Union[dict, History], List[Union[dict, History]]]])

slots.pathology__pathology_measurement = Slot(uri=OBO.MICRO_0001469, name="pathology__pathology_measurement", curie=OBO.curie('MICRO_0001469'),
                   model_uri=GBM.pathology__pathology_measurement, domain=None, range=Optional[Union[Union[dict, Measurement], List[Union[dict, Measurement]]]])

slots.pathology__pathology_localization = Slot(uri=WDT.P927, name="pathology__pathology_localization", curie=WDT.curie('P927'),
                   model_uri=GBM.pathology__pathology_localization, domain=None, range=Optional[Union[Union[dict, Localization], List[Union[dict, Localization]]]])

slots.pathology__pathology_specimen = Slot(uri=OBO.HSO_0000308, name="pathology__pathology_specimen", curie=OBO.curie('HSO_0000308'),
                   model_uri=GBM.pathology__pathology_specimen, domain=None, range=Optional[Union[Union[dict, BioSpecimen], List[Union[dict, BioSpecimen]]]])

slots.datafile__uri = Slot(uri=GBM.uri, name="datafile__uri", curie=GBM.curie('uri'),
                   model_uri=GBM.datafile__uri, domain=None, range=URIRef)

slots.datafile__format = Slot(uri=DCTERMS.format, name="datafile__format", curie=DCTERMS.curie('format'),
                   model_uri=GBM.datafile__format, domain=None, range=Optional[Union[str, FormatUri]])

slots.datafile__issued = Slot(uri=DCTERMS.issued, name="datafile__issued", curie=DCTERMS.curie('issued'),
                   model_uri=GBM.datafile__issued, domain=None, range=Optional[str])

slots.datafile__modified = Slot(uri=DCTERMS.modified, name="datafile__modified", curie=DCTERMS.curie('modified'),
                   model_uri=GBM.datafile__modified, domain=None, range=Optional[str])

slots.datafile__subjects = Slot(uri=OBO.subjects, name="datafile__subjects", curie=OBO.curie('subjects'),
                   model_uri=GBM.datafile__subjects, domain=None, range=Optional[Union[Dict[Union[str, GBMSubjectSubjectId], Union[dict, GBMSubject]], List[Union[dict, GBMSubject]]]])

slots.format__uri = Slot(uri=GBM.uri, name="format__uri", curie=GBM.curie('uri'),
                   model_uri=GBM.format__uri, domain=None, range=URIRef)

slots.baseSubject__source_site = Slot(uri=SIO.SIO_000066, name="baseSubject__source_site", curie=SIO.curie('SIO_000066'),
                   model_uri=GBM.baseSubject__source_site, domain=None, range=Optional[Union[str, List[str]]])

slots.baseSubject__source_datafile = Slot(uri=DCTERMS.isPartOf, name="baseSubject__source_datafile", curie=DCTERMS.curie('isPartOf'),
                   model_uri=GBM.baseSubject__source_datafile, domain=None, range=Optional[Union[str, DatafileUri]])

slots.baseSubject__subject_id = Slot(uri=DCTERMS.identifier, name="baseSubject__subject_id", curie=DCTERMS.curie('identifier'),
                   model_uri=GBM.baseSubject__subject_id, domain=None, range=URIRef)

slots.baseProperties__subject_age = Slot(uri=FOAF.age, name="baseProperties__subject_age", curie=FOAF.curie('age'),
                   model_uri=GBM.baseProperties__subject_age, domain=None, range=Optional[int])

slots.baseProperties__subject_gender = Slot(uri=SCHEMA.gender, name="baseProperties__subject_gender", curie=SCHEMA.curie('gender'),
                   model_uri=GBM.baseProperties__subject_gender, domain=None, range=Optional[Union[str, "GenderEnum"]])

slots.DiseaseResponse_value = Slot(uri=RDF.value, name="DiseaseResponse_value", curie=RDF.curie('value'),
                   model_uri=GBM.DiseaseResponse_value, domain=DiseaseResponse, range=Optional[Union[Union[str, "DiseaseReponseEnum"], List[Union[str, "DiseaseReponseEnum"]]]])

slots.DieseaseProgression_value = Slot(uri=RDF.value, name="DieseaseProgression_value", curie=RDF.curie('value'),
                   model_uri=GBM.DieseaseProgression_value, domain=DieseaseProgression, range=Optional[Union[Union[bool, Bool], List[Union[bool, Bool]]]])

slots.Edamatous_value = Slot(uri=RDF.value, name="Edamatous_value", curie=RDF.curie('value'),
                   model_uri=GBM.Edamatous_value, domain=Edamatous, range=Optional[Union[Union[bool, Bool], List[Union[bool, Bool]]]])

slots.PseudoProgression_value = Slot(uri=RDF.value, name="PseudoProgression_value", curie=RDF.curie('value'),
                   model_uri=GBM.PseudoProgression_value, domain=PseudoProgression, range=Optional[Union[Union[bool, Bool], List[Union[bool, Bool]]]])

slots.OverallSurvival_value = Slot(uri=RDF.value, name="OverallSurvival_value", curie=RDF.curie('value'),
                   model_uri=GBM.OverallSurvival_value, domain=OverallSurvival, range=Optional[Union[int, List[int]]])

slots.ProgressiveFreeSurvival_value = Slot(uri=RDF.value, name="ProgressiveFreeSurvival_value", curie=RDF.curie('value'),
                   model_uri=GBM.ProgressiveFreeSurvival_value, domain=ProgressiveFreeSurvival, range=Optional[Union[int, List[int]]])

slots.DrugUse_value = Slot(uri=RDF.value, name="DrugUse_value", curie=RDF.curie('value'),
                   model_uri=GBM.DrugUse_value, domain=DrugUse, range=Optional[Union[int, List[int]]])

slots.DrugUse_unit = Slot(uri=SIO.SIO_000221, name="DrugUse_unit", curie=SIO.curie('SIO_000221'),
                   model_uri=GBM.DrugUse_unit, domain=DrugUse, range=Optional[Union[str, "Term"]])

slots.Bevacizumab_value = Slot(uri=RDF.value, name="Bevacizumab_value", curie=RDF.curie('value'),
                   model_uri=GBM.Bevacizumab_value, domain=Bevacizumab, range=Optional[Union[int, List[int]]])

slots.Temozolomide_value = Slot(uri=RDF.value, name="Temozolomide_value", curie=RDF.curie('value'),
                   model_uri=GBM.Temozolomide_value, domain=Temozolomide, range=Optional[Union[int, List[int]]])

slots.Localization_value = Slot(uri=RDF.value, name="Localization_value", curie=RDF.curie('value'),
                   model_uri=GBM.Localization_value, domain=Localization, range=Optional[Union[Union[str, "LocalizationEnum"], List[Union[str, "LocalizationEnum"]]]])

slots.IDH_value = Slot(uri=RDF.value, name="IDH_value", curie=RDF.curie('value'),
                   model_uri=GBM.IDH_value, domain=IDH, range=Optional[Union[Union[str, "MutationTypeEnum"], List[Union[str, "MutationTypeEnum"]]]])

slots.MGMT_value = Slot(uri=RDF.value, name="MGMT_value", curie=RDF.curie('value'),
                   model_uri=GBM.MGMT_value, domain=MGMT, range=Optional[Union[Union[str, "MethylationEnum"], List[Union[str, "MethylationEnum"]]]])

slots.ECOG_range = Slot(uri=RDFS.range, name="ECOG_range", curie=RDFS.curie('range'),
                   model_uri=GBM.ECOG_range, domain=ECOG, range=Optional[str])

slots.Dead_range = Slot(uri=RDFS.range, name="Dead_range", curie=RDFS.curie('range'),
                   model_uri=GBM.Dead_range, domain=Dead, range=Optional[str])

slots.LymphocyteCount_value = Slot(uri=RDF.value, name="LymphocyteCount_value", curie=RDF.curie('value'),
                   model_uri=GBM.LymphocyteCount_value, domain=LymphocyteCount, range=Optional[Union[float, List[float]]])

slots.BioSpecimen_range = Slot(uri=RDFS.range, name="BioSpecimen_range", curie=RDFS.curie('range'),
                   model_uri=GBM.BioSpecimen_range, domain=BioSpecimen, range=Optional[str])
