JUPYTER=conda run -n jbook
SHEET=


convert2rdf.py: convert2rdf.ipynb
	$(JUPYTER) jupyter nbconvert --to python convert2rdf.ipynb convert2rdf.py

test.tsv: test.xlsx
	xlsx2csv -s 1 -d tab test.xlsx test.tsv

out.tsv: test.tsv preprocess.py
	python preprocess.py test.tsv out.tsv

out.json: out.tsv gbm.yaml
	linkml-convert -f tsv -t json -s gbm.yaml -C Root -S subjects out.tsv > out.json

out.ttl: out.tsv gbm.yaml
	linkml-convert -f tsv -t ttl -s gbm.yaml -C Root -S subjects out.tsv > out.ttl

lint:
	linkml-lint gbm.yaml

clean:
	rm -f convert2rdf.py test.tsv out.tsv out.ttl out.json

.PHONY: lint
