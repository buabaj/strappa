import subprocess
import sys
from pathlib import Path
import venv

from strappa.utils import create_files, ensure_directory

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


def copy_templates() -> None:
    create_files()
    print("Created requirements.txt and requirements-strappa.txt")

def setup_project() -> None:
    print("Setting up project in the current directory")

    create_virtual_environment()

    ensure_directory("src")
    ensure_directory("tests")

    run_in_venv("pip install -r requirements.txt")

    print("Project setup complete!")
    print("Virtual environment is now active. You can start working on your project.")


if __name__ == "__main__":
    setup_project()
