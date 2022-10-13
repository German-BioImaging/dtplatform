#!/usr/bin/env python

# This script takes the output from `dctap read model.csv --yaml`
# and parses it into linkml(-like) syntax. This done by reading
# the YAML output and passing it to the jinja template (template.yaml)
# in the same directory.
#

import click
import logging
import yaml
from click_loglevel import LogLevel
from jinja2 import Environment, FileSystemLoader, select_autoescape

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


@click.command()
@click.argument("tap", type=click.File())
@click.option("-l", "--log-level", type=LogLevel(), default=logging.INFO)
def dump(tap, log_level):

    logging.basicConfig(level=log_level)

    #
    # Loop through the data once to make sure we are aware of the existing columns.
    #
    data = yaml.load(tap, Loader=Loader)
    for shape in data["shapes"]:
        shapeID = shape.pop("shapeID")
        stmts = shape.pop("statement_templates")
        assert not shape, shape.keys()
        for stmt in stmts:
            propertyID = stmt.pop("propertyID")
            propertyLabel = stmt.pop("propertyLabel", None)
            valueNodeType = stmt.pop("valueNodeType", None)
            valueConstraint = stmt.pop("valueConstraint", None)
            valueDataType = stmt.pop("valueDataType", None)
            valueShape = stmt.pop("valueShape", None)
            assert not stmt, stmt.keys()


    #
    # Now send the same data to the Jinja template.
    #
    env = Environment(
        loader=FileSystemLoader("."),
        autoescape=select_autoescape(),
    )

    template = env.get_template("template.yaml")

    tap.seek(0)
    print(template.render(shapes=yaml.load(tap, Loader=Loader)["shapes"]))


if __name__ == "__main__":
    dump()
