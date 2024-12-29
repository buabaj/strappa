import os
import sys
from pathlib import Path
from typing import Any
import pytest

from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from strappa.main import (
    get_activation_script,
    run_in_venv,
    create_config_files
)


@pytest.fixture
def temp_dir(tmp_path: Path) -> Any:
    original_dir = os.getcwd()  # noqa: PTH109
    os.chdir(tmp_path)
    yield tmp_path
    os.chdir(original_dir)


def test_get_activation_script():
    if sys.platform == "win32":
        expected = Path(".venv") / "Scripts" / "activate.bat"
    else:
        expected = Path(".venv") / "bin" / "activate"

    assert get_activation_script() == expected


@patch("subprocess.run")
def test_run_in_venv(mock_run: str):
    run_in_venv("pip list")
    mock_run.assert_called_once()
    args, kwargs = mock_run.call_args
    assert "pip list" in args[0]
    assert kwargs["shell"] is True
    assert kwargs["check"] is True


def test_create_files(temp_dir: temp_dir):
    create_config_files()

    assert (temp_dir / "pyproject.toml").exists()
    with open(temp_dir / "pyproject.toml") as f:  # no
        content = f.read()
        assert "[tool.pytest.ini_options]" in content

    assert (temp_dir / "Makefile").exists()

    with open(temp_dir / "Makefile") as f:
        content = f.read()
        assert ".PHONY: test" in content
