requirements/tox.txt: tox.ini
	tox -l >/dev/null 2>&1

requirements.txt: $(wildcard requirements/*.txt)
	echo $^ \
	| tr " " "\n" \
	| sed -e 's/^/-r/g' \
	> $@

constraints.txt: requirements.txt
	pip-compile --generate-hashes --output-file $@ $^ >/dev/null 2>&1

# Shortcut for recreating an sdist that depends on the current sources only, not also on the previous sdist build.
sdist:
	-rm src/*.egg-info/SOURCES.txt
	python setup.py sdist