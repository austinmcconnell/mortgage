.PHONY: clean clean-test clean-pyc clean-build docs help

## remove all build, test, coverage and Python artifacts
clean: clean-build clean-pyc clean-test

## remove build artifacts
clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

## remove Python file artifacts
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

## remove test and coverage artifacts
clean-test:
	rm -f .coverage
	rm -fr htmlcov/

## check style with pylint, pycodestyle, and pydocstyle
lint:
	pylint --rcfile=.pylintrc --output-format=parseable --reports=no mortgage
	pycodestyle mortgage --max-line-length=100
	pydocstyle mortgage

## run tests quickly with the default Python
test:
	pytest
	cd docs && make doctest

## check code coverage quickly with the default Python
coverage:
	coverage run --source mortgage -m pytest
	coverage report -m
	coverage html


## builds source and wheel package
dist:
	clean
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

## install the package to the active Python's site-packages
install:
	clean
	python setup.py install

docs:
	cd docs && make html
	@echo "\033[95m\n\nBuild successful! View the docs homepage at docs/_build/html/index.html.\n\033[0m"
