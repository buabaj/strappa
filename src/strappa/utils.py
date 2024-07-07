import subprocess
from pathlib import Path


def create_file(filename: str, content: str) -> None:
    with open(filename, "w") as f:
        f.write(content.strip())


def run_command(command: str) -> None:
    subprocess.run(command, shell=True, check=True)


def ensure_directory(directory: str) -> None:
    Path(directory).mkdir(parents=True, exist_ok=True)
