JUPYTER=conda run -n jbook
SHEET=

### RDF WORKFLOW ################################

rdf:
	linkml-convert -f ttl -t yaml -s gbm.yaml -C Subject test.ttl -o out.yaml

### TABULAR WORKFLOW ############################

tabular: out.json
	cat out.json

convert2rdf.py: convert2rdf.ipynb
	$(JUPYTER) jupyter nbconvert --to python convert2rdf.ipynb convert2rdf.py

test.tsv: test.xlsx
	xlsx2csv -s 1 -d tab test.xlsx test.tsv

out.tsv: test.tsv preprocess.py clinics.tsv labs.tsv
	python preprocess.py test.tsv out.tsv

out.json: out.tsv gbm.yaml
	linkml-convert -f tsv -t json -s gbm.yaml -C Root -S subjects out.tsv -o out.json

out.ttl: out.tsv gbm.yaml
	linkml-convert -f tsv -t ttl -s gbm.yaml -C Root -S subjects out.tsv -o out.ttl

#
# Schema level tools
#

lint:
	linkml-lint gbm.yaml

schema.png: gbm.yaml
	gen-graphviz -o schema -f png gbm.yaml

#
# Misc
#

clean:
	rm -f convert2rdf.py test.tsv out.tsv out.ttl out.json out.yaml schema.png

.PHONY: lint tabular
