install:
	pip install --upgrade pip
	pip install pre-commit flake8 flake8-docstrings Flake8-pyproject radon pylint mypy black isort

synth-project:
	python .projenrc.py

lint:
	pre-commit run --all-files
