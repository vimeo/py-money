.PHONY: install test pylint

install:
	python setup.py install
	pip install pylint

test:
	PYTHONPATH=PYTHONPATH:money py.test money

pylint:
	PYTHONPATH=PYTHONPATH:money python $$(which pylint) money --output-format colorized
