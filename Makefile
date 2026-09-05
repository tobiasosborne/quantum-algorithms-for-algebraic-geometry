PYTHON ?= python3

.PHONY: setup setup-browser hooks report report-build report-check build check ci

setup:
	$(PYTHON) scripts/report_ci.py setup

setup-browser:
	$(PYTHON) scripts/report_ci.py setup-browser

hooks:
	$(PYTHON) scripts/install_hooks.py

report: report-build
build: report-build
check: report-check

report-build:
	$(PYTHON) scripts/report_ci.py build

report-check:
	$(PYTHON) scripts/report_ci.py check

ci:
	$(PYTHON) scripts/report_ci.py ci
