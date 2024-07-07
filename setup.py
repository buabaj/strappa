from setuptools import setup, find_packages

setup(
    name="strappa",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "click",
    ],
    extras_require={
        "dev": [
            "pytest",
            "ruff",
            "mypy",
            "pytest-cov",
        ],
    },
    entry_points={
        "console_scripts": [
            "strappa=strappa.cli:cli",
        ],
    },
    author="jerry buaba",
    author_email="buabajerry+strappa@gmail.com",
    description="A Python bootstrapper to help set up Python projects easily and faster",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/buabaj/strappa",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
)
