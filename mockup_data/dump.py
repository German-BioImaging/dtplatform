#!/usr/bin/env python

import click
from click_loglevel import LogLevel
import logging
import os
import sys
from pathlib import Path
from typing import List

from linkml_runtime import DataNotFoundError
from linkml_runtime.linkml_model import Prefix
from linkml_runtime.utils import inference_utils
from linkml_runtime.utils.compile_python import compile_python
from linkml_runtime.utils.inference_utils import infer_all_slot_values
from linkml_runtime.utils.schemaview import SchemaView

from linkml.generators.pythongen import PythonGenerator
from linkml.utils import datautils, validation
from linkml.utils.datautils import (
    _get_context,
    _get_format,
    _is_xsv,
    dumpers_loaders,
    get_dumper,
    get_loader,
    infer_index_slot,
    infer_root_class,
)

from rdflib import Graph


@click.command()
@click.argument("dirname", type=click.Path(exists=True))
@click.option("-l", "--log-level", type=LogLevel(), default=logging.INFO)
def dump(dirname, log_level):

    logging.basicConfig(level=log_level)

    sys.path.insert(0, dirname)
    import dtmodel as python_module

    turtle = Path(dirname) / "test.ttl"
    schema = Path(dirname) / "model.yaml"
    sv = SchemaView(str(schema))
    py_target_class = python_module.__dict__["GBMSubject"]
    input_format = _get_format(turtle, "ttl")
    loader = get_loader(input_format)

    graph = Graph().parse(turtle)
    objects = loader.from_rdf_graph(graph, target_class=py_target_class, schemaview=sv)
    print("[")
    print(",\n".join([x._as_json_dumps() for x in objects]))
    print("]")


if __name__ == "__main__":
    dump()
