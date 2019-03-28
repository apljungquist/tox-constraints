requirements/tox.txt: tox.ini
	tox -l >/dev/null 2>&1

requirements.txt: $(wildcard requirements/*.txt)
	echo $^ \
	| tr " " "\n" \
	| sed -e 's/^/-r/g' \
	> $@

constraints.txt: requirements.txt
	pip-compile --output-file $@ $^ >/dev/null 2>&1