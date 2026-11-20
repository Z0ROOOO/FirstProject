from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as f:
        requirements = f.read().splitlines()

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="FirstProject",
    version="0.1.0",
    author="Abhay",
    author_email="abhaykumarsingh20456@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("req.txt"),
)