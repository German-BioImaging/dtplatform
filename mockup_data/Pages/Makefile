JUPYTER=conda run -n jbook
LINKML=conda run -n linkml
SHEET=

### RDF WORKFLOW ################################

out.jsonld: gbm.yaml test.ttl
	$(LINKML) linkml-convert -f ttl -t json-ld -s gbm.yaml -C Subject test.ttl -o out.jsonld

out.yaml: gbm.yaml test.ttl
	$(LINKML) linkml-convert -f ttl -t yaml -s gbm.yaml -C Subject test.ttl -o out.yaml

### TABULAR WORKFLOW ############################

tabular: out.json
	cat out.json

test.tsv: test.xlsx
	xlsx2csv -s 1 -d tab test.xlsx test.tsv

out.tsv: test.tsv preprocess.py clinics.tsv labs.tsv
	python preprocess.py test.tsv out.tsv

out.json: out.tsv gbm.yaml
	$(LINKML) linkml-convert -f tsv -t json -s gbm.yaml -C Root -S subjects out.tsv -o out.json

out.ttl: out.tsv gbm.yaml
	$(LINKML) linkml-convert -f tsv -t ttl -s gbm.yaml -C Root -S subjects out.tsv -o out.ttl

#
# Schema level tools
#

lint:
	$(LINKML) linkml-lint gbm.yaml

schema.png: gbm.yaml
	$(LINKML) gen-graphviz -o schema -f png gbm.yaml

docs: gbm.yaml
	$(LINKML) gen-markdown --index-file docs/schema.md -d docs gbm.yaml

#
# Misc
#
#

mkdocs: docs
	mkdocs serve

convert2rdf.py: convert2rdf.ipynb
	$(JUPYTER) jupyter nbconvert --to python convert2rdf.ipynb convert2rdf.py

test.ttl: convert2rdf.py
	$(JUPYTER) python convert2rdf.py

graphviz: convert2rdf.py
	python convert2rdf.py

clean:
	rm -rf convert2rdf.py test.tsv out.tsv out.ttl out.json out.yaml schema.png docs

.PHONY: graphviz lint mkdocs tabular
