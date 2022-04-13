#!/usr/bin/env python
import requests
import json
import re

from xml.etree import ElementTree as ET


def download(*file_uuids):
    """
    Download a file from TCGA by UUID and return it as a string

    """
    params = {"ids": list(file_uuids)}

    data_endpt = "https://api.gdc.cancer.gov/data"
    response = requests.post(data_endpt, data = json.dumps(params), headers = {"Content-Type": "application/json"})
    # Unused
    # response_head_cd = response.headers["Content-Disposition"]
    # file_name = re.findall("filename=(.+)", response_head_cd)[0]
    return response.content.decode()

def parse_bcr_date(file_content):
    """
    Parse the XML elements tcga_bcr/admin/{day,month,year}_of_dcc_upload
    from the stringified content of a BCR file.
    """
    header = """
    <bio:tcga_bcr
        xsi:schemaLocation="http://tcga.nci/bcr/xml/biospecimen/2.7
        https://raw.githubusercontent.com/nchbcr/xsd/2.7/tcga.nci/bcr/xml/biospecimen/2.7/TCGA_BCR.Biospecimen.xsd"
        schemaVersion="2.7"
        xmlns:bio="http://tcga.nci/bcr/xml/biospecimen/2.7"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns:admin="http://tcga.nci/bcr/xml/administration/2.7"
        xmlns:shared="http://tcga.nci/bcr/xml/shared/2.7"
        xmlns:bio_model="http://tcga.nci/bcr/xml/biospecimen/bio_model/2.7"
        xmlns:bio_shared="http://tcga.nci/bcr/xml/biospecimen/shared/2.7">
    """
    admin = "http://tcga.nci/bcr/xml/administration/2.7"

    example = """
        <admin:admin>
            <admin:bcr xsd_ver="1.17">Nationwide Children's Hospital</admin:bcr>
            <admin:file_uuid xsd_ver="2.6">47870701-9C23-4AD2-B8E1-07275E5AB1B0</admin:file_uuid>
            <admin:batch_number xsd_ver="1.17">661.0.0</admin:batch_number>
            <admin:project_code xsd_ver="2.7">Human Cancer Model Initiative</admin:project_code>
            <admin:disease_code xsd_ver="2.6">HCMI</admin:disease_code>
            <admin:day_of_dcc_upload xsd_ver="1.17">10</admin:day_of_dcc_upload>
            <admin:month_of_dcc_upload xsd_ver="1.17">10</admin:month_of_dcc_upload>
            <admin:year_of_dcc_upload xsd_ver="1.17">2019</admin:year_of_dcc_upload>
            <admin:program xsd_ver="2.7">HCMI</admin:program>
            <admin:dbgap_registration_code xsd_ver="2.7">001486</admin:dbgap_registration_code>
        </admin:admin>
        """

    tree = ET.fromstring(file_content)
    info = tree.find(f"{{{admin}}}admin")
    year = info.find(f"{{{admin}}}year_of_dcc_upload").text.strip()
    month = info.find(f"{{{admin}}}month_of_dcc_upload").text.strip()
    day = info.find(f"{{{admin}}}day_of_dcc_upload").text.strip()
    return (year, month, day)

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        # https://portal.gdc.cancer.gov/files/02930356-2143-42c2-a0d3-7ca945156ae9
        example = "02930356-2143-42c2-a0d3-7ca945156ae9"
        print(parse_bcr_date(download(example)))
    else:
        for uuid in sys.argv[1:]:
            print(f"Downloading {uuid}...")
            print(download(uuid))
