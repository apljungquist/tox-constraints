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

# Create, unpack and display contents of sdist
# Automatically check some desired properties of the sdist:
# * pyc files have not been included
# * tests work
# * the licence file has been included
test_sdist:
	-rm src/*.egg-info/SOURCES.txt
	-rm -r dist
	python setup.py sdist

	cd dist \
	&& tar -xzf *.tar.gz \
	&& rm *.tar.gz \
	&& cd * \
	&& tree . \
	&& test -z "$$(find . -name '*.pyc')" \
	&& python setup.py test \
	&& test -e LICENSE \
	&& pwd
