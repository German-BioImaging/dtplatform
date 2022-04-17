#!/usr/bin/env python
import pywikibot as pb

filename = u"File:Case TCGA-AN-A046 slide 01Z-00-DX1 from the TCGA-BRCA project.png"

site = pb.Site("commons", "commons")
page = pb.Page(site, filename)
text = page.text
print(text)
