.PHONY: help clean clean-pyc clean-build test test-all bake watch 
.DEFAULT_GOAL := help
BAKE_OPTIONS = --no-input


help:
	@echo "bake - generate project using defaults"
	@echo "watch - generate project using defaults and watch for changes"
	@echo "replay - replay last cookiecutter run and watch for changes"
	@echo "clean - remove all"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "test - run tests quickly with the default Python"
	@echo "test-all - run tests on every Python version with tox"
	@echo "docs - build docs"

bake:
	cookiecutter $(BAKE_OPTIONS) . --overwrite-if-exists

watch: bake
	watchmedo shell-command -p '*.*' -c 'make bake -e BAKE_OPTIONS=$(BAKE_OPTIONS)' -W -R -D \{{cookiecutter.project_slug}}/

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '.DS_Store' -exec rm -fr {} +

clean-pyc:
	find . -name '__pycache__' -exec rm -fr {} +

test:
	py.test

test-all:
	tox

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

replay: BAKE_OPTIONS=--replay
replay: watch
	;