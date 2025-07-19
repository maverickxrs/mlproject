from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = "-e ."


def get_requirements(file_path:str) -> List[str]:
    """
    This fucntion will return a list of requirements that are needed to be installed for the ML workflow
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  # Will add a /n for a newline
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Rohit Brahme",
    author_email="maverickxrs17@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
