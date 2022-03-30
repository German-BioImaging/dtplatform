#!/usr/bin/env python
# https://commons.wikimedia.org/wiki/Commons:Command-line_upload
import sys

import pywikibot
from pywikibot.specialbots import UploadRobot

name_template = u"""Case_%(case)s_slide_%(slide)s_from_the_%(project)s_project.png"""

desc_template = u"""A png generated from a microscopic image in SVS format taken at %(location)s. The image is one of %(number)s from case %(case)s (https://portal.gdc.cancer.gov/cases/%(case_uuid)s) a part of the "%(project_name)" project in the %(program)s program.}}"""

wiki_template = u"""
=={{int:filedesc}}==
{{Information
|description={{en|1=%(desc)s}}
|date=%(date)s
|source=https://portal.gdc.cancer.gov/files/%(file_uuid)s
|author=Unknown photographer
|permission=
|other versions=
}}

=={{int:license-header}}==
{{cc-zero}}

[[Category:Breast cancer]]
[[Category:Breast tumors]]
[[Category:Tissue]]
[[Category:Microscopic images]]
"""

def complete_desc_and_upload(filename, pagetitle, description):
    url = [ filename ]
    keepFilename = False        #set to True to skip double-checking/editing destination filename
    verifyDescription = True    #set to False to skip double-checking/editing description => change to bot-mode
    targetSite = pywikibot.getSite('commons', 'commons')

    bot = UploadRobot(url, description=description, useFilename=pagetitle, keepFilename=keepFilename, verifyDescription=verifyDescription, targetSite=targetSite)
    bot.run()

def main(args):
    args = {
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
    args["desc"] = desc_template % args
    filename    = name_template % args
    pagetitle   = filename
    desciption  = wiki_template % args
    #complete_desc_and_upload(filename, pagetitle, description)


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    finally:
        pywikibot.stopme()
