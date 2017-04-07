.PHONY: install test pylint

install:
	python setup.py install
	pip install pylint
	pip install pytest

test:
	PYTHONPATH=PYTHONPATH:money py.test money

pylint:
	PYTHONPATH=PYTHONPATH:money python $$(which pylint) money --output-format colorized
