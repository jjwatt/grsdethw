.PHONY flake8
SRCDIR := grsdethw
init:
	pip install .
	pip install requirements-dev.txt
ci:
	pytest tests --junitxml=report.xml
flake8:
	flake8 $(SRCDIR)
