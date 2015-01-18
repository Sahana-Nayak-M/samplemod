#!/bin/sh

mkdir meta

# list of integration tests (unit tests would be in src/tests)

ack -l "\(unittest.TestCase" . --type=python > all_test_names.txt

# Process them one at a time

for fn in `cat all_test_names.txt`; do

	# One nose invocation per test (so we can get focused coverage)

    nosetests --cover-erase --with-coverage --tests=$fn 2>&1 | grep "\%" > last_test_coverage.txt

	metapath="meta/${fn}"
	mkdir -p ${metapath%/*}
	python testimpact_subset_to_covered.py > $metapath

	# TODO deleted tests not handled.
done

# Turn many files into map of the total picture
# that's source vs tests (instead of tests vs sources)

ack --type=python --noheading "." meta | sed 's#meta/##g' | sed 's/:[[:digit:]]:/ /' | awk ' { t = $1; $1 = $2; $2 = t; print; } ' | sort > meta/impact-map.txt

# TODO - check in potentially changed cross references files here