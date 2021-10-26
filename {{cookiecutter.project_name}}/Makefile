.PHONY: help clean dist release-staging bump-release bump-release-dry-run bump-minor bump-minor-dry-run bump-major bump-major-dry-run bump-patch bump-patch-dry-run
.EXPORT_ALL_VARIABLES:

# Platform Independent options for common commands
MV?=mv
RM?=rm
# Convenience function for running dev scripts
PDS=$(PY) ./.dev_scripts/
PY?=python
IPY=python -c
PDR=$(PDS)run.py
CLDIR=$(PDS)clean_dir.py
PYPI_URL?=https://packages.idmod.org/api/pypi/idm-pypi-staging/
PACKAGE_NAME=Gene_Drive

# Makefile rules

help:
	$(PDS)get_help_from_makefile.py

setup-dev:  ## Setup packages in dev mode
	python ./.dev_scripts/bootstrap.py

clean: ## Clean most of the temp-data from the project
	$(CLDIR) --file-patterns "*.py[co],*.done,*.log,**/.coverage" \
		--dir-patterns "**/__pycache__,**/htmlcov,**/.pytest_cache" --directories "dist,build"
	$(PDR) -wd "docs" -ex "make clean"

clean-all:  ## Deleting package info hides plugins so we only want to do that for packaging
	@make clean
	$(CLDIR) --dir-patterns "**/*.egg-info/"


# Release related rules
#######################

dist: clean ## build our package
	python setup.py sdist

release-staging: dist ## perform a release to staging
	twine upload --verbose --repository-url $(PYPI_URL) dist/*

# versioning
bump-release: ## bump the release version.
	bump2version release --commit

# Use before release-staging-release-commit to confirm next version.
bump-release-dry-run: ## bump the release version. (dry run)
	bump2version release --dry-run --allow-dirty --verbose

bump-patch: ## bump the patch version
	bump2version patch --commit

bump-minor: ## bump the minor version
	bump2version minor --commit

bump-major: ## bump the major version
	bump2version major --commit

bump-patch-dry-run: ## bump the patch version(dry run)
	bump2version patch --dry-run --allow-dirty --verbose

bump-minor-dry-run: ## bump the minor version(dry run)
	bump2version minor --dry-run --allow-dirty --verbose

bump-major-dry-run: ## bump the major version(dry run)
	bump2version major --dry-run --allow-dirty --verbose
licenses: ## Generate LICENSES.txt
	pip-licenses --format=rst --output-file ./{{cookiecutter.project_name}}/licenses/LICENSES.txt
	pip-licenses --format=json --output-file ./{{cookiecutter.project_name}}/licenses/LICENSES.json