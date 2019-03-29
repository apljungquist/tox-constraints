# TODO: This should remove reduntant environments as well
requirements/tox.txt: tox.ini
	tox -l >/dev/null 2>&1

requirements.txt: $(wildcard requirements/*.txt)
	echo $^ \
	| tr " " "\n" \
	| sed -e 's/^/-r/g' \
	> $@

# TODO: This will not update if requirements/tox/*.txt is touched
constraints.txt: requirements.txt
	pip-compile --output-file $@ $^ >/dev/null 2>&1