import subprocess
import sys
from pathlib import Path
import venv

from strappa.utils import create_file, ensure_directory


def create_virtual_environment(venv_path: Path = Path(".venv")) -> None:
    venv.create(venv_path, with_pip=True)
    print(f"Created virtual environment at {venv_path}")


def get_activation_script(venv_path: Path = Path(".venv")) -> Path:
    if sys.platform == "win32":
        return venv_path / "Scripts" / "activate.bat"
    else:
        return venv_path / "bin" / "activate"


def run_in_venv(command: str, venv_path: Path = Path(".venv")) -> None:
    activate_script = get_activation_script(venv_path)

    if sys.platform == "win32":
        full_command = f'"{activate_script}" && {command}'
        shell = True
    else:
        full_command = f'source "{activate_script}" && {command}'
        shell = True  # Changed from "/bin/bash" to True

    try:
        subprocess.run(
            full_command, shell=shell, check=True, executable="/bin/bash" if sys.platform != "win32" else None
        )
    except subprocess.CalledProcessError as e:
        print(f"Error running command in virtual environment: {e}")
        sys.exit(1)


def create_pyproject_toml() -> None:
    content = """
[tool.pytest.ini_options]
addopts = "-ra"
testpaths = [
    "tests",
]
pythonpath = ["src",]

[tool.mypy]
namespace_packages = true
explicit_package_bases = true
strict = true
mypy_path = "src:."
follow_imports = "silent"
warn_redundant_casts = true
warn_unused_ignores = true
disallow_any_generics = true
check_untyped_defs = true
no_implicit_reexport = true
exclude = ["tests/*"]

[tool.pydantic-mypy]
init_forbid_extra = true
init_typed = true
warn_required_dynamic_aliases = true

[tool.ruff]
line-length = 120
indent-width = 4
target-version = "py310"

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "PTH", "G", "T10", "A", "PL", "RUF100", "PGH004", "N", "ANN", "EXE"]
ignore = [
"PLR0912", "PLR0915", "PLR2004", "PLR0913", "PLR1714", "PLR0911", # Over-opinionated
"G004", # F-string in logging
"UP028", # Use yield from
"UP007", # "Use | instead for union
"ANN002", "ANN003", "ANN101", "ANN102", "ANN201", "ANN202", "ANN204", "ANN401", # Type hints needed
"I001", # No need as using formatter
"PTH123", # Do not recommend using Path.open()
]

dummy-variable-rgx = "^(_+|(_+[a-zA-Z0-9_]*[a-zA-Z0-9]+?))$"

[tool.coverage.run]
branch = true
parallel = true
omit = [
    '__init__.py',
    'tests/*',
]

[tool.coverage.report]
skip_empty = true
show_missing = true
fail_under = 95
exclude_lines = [
    "pragma: no cover",
    "case _:",
    "raise NotImplementedError",
]
"""
    create_file("pyproject.toml", content)
    print("Created pyproject.toml")


def create_makefile() -> None:
    content = """
[.PHONY: test
test:
    python3 -m pytest

.PHONY: ruff
ruff:
    python3 -m ruff check --output-format=full

.PHONY: ruff-fix
ruff-fix:
    python3 -m ruff check --fix

.PHONY: mypy
mypy:
    python3 -m mypy ./src --check-untyped-defs

.PHONY: format
format:
    python3 -m ruff format

.PHONY: lint
lint: ruff mypy

.PHONY: coverage
coverage:
    python3 -m pytest --verbose --cov=.

.PHONY: coverage-report
coverage-report:
    python3 -m pytest --verbose --cov=. --cov-report=html

.PHONY: all_checks
all_checks: format ruff-fix lint test ]
"""
    create_file("Makefile", content)
    print("Created Makefile")


def create_requirements_files() -> None:
    strappa_content = """
pytest
ruff
mypy
pytest-cov
"""
    create_file("requirements-strappa.txt", strappa_content)

    requirements_content = """
        -r requirements-strappa.txt
    """
    create_file("requirements.txt", requirements_content)
    print("Created requirements.txt and requirements-strappa.txt")


def setup_project() -> None:
    print("Setting up project in the current directory")

    create_virtual_environment()
    create_pyproject_toml()
    create_makefile()
    create_requirements_files()

    ensure_directory("src")
    ensure_directory("tests")

    run_in_venv("pip install -r requirements.txt")

    print("Project setup complete!")
    print("Virtual environment is now active. You can start working on your project.")


if __name__ == "__main__":
    setup_project()
