# This feels a bit like a matroska doll, but it makes it quick to get up and running
# from nothing but a clean repo.
init_venv.sh:
	toxc-recutter $@ --prompt toxc > $@

# Use -l to stop tox from running envs
requirements/tox.txt: tox.ini
	tox -l --requirements-file $@ >/dev/null 2>&1

requirements.txt: $(wildcard requirements/*.txt)
	echo $^ \
	| tr " " "\n" \
	| sed -e 's/^/-r/g' \
	> $@

constraints.txt: requirements.txt
	pip-compile --generate-hashes --allow-unsafe --output-file $@ $^ >/dev/null

# Shortcut for recreating an sdist that depends on the current sources only, not also on the previous sdist build.
sdist:
	-rm src/*.egg-info/SOURCES.txt
	python setup.py sdist