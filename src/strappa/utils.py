import subprocess
from pathlib import Path
from typing import Final

TEMPLATES_DIR: Final = Path(__file__).parent.parent / "templates"

def copy_template(template_name: str, dest_name: str) -> None:
    """Copy a template file to the destination."""
    template_path = TEMPLATES_DIR / template_name
    dest_path = Path(dest_name)
    
    if not template_path.exists():
        raise FileNotFoundError(f"Template {template_name} not found")
        
    dest_path.write_text(template_path.read_text())
    print(f"Created {dest_name}")

def create_config_files() -> None:
    """Create all configuration files from templates."""
    copy_template("pyproject.toml.template", "pyproject.toml")
    copy_template("Makefile.template", "Makefile")
    copy_template("requirements.txt.template", "requirements.txt")



def run_command(command: str) -> None:
    subprocess.run(command, shell=True, check=True)


def ensure_directory(directory: str) -> None:
    Path(directory).mkdir(parents=True, exist_ok=True)
