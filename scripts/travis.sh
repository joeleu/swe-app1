#!/bin/bash

set -e

# Setup
cd "${TRAVIS_BUILD_DIR}/swe_app1"

python manage.py migrate

# Check formatting and lint
black --check .

flake8 .

# Test and measure coverage
python manage.py test

coverage run --source "." manage.py test

# Report coverage
coveralls
