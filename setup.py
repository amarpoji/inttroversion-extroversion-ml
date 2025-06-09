from setuptools import setup, find_packages
from typing import List
from src.logger import logging

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns the list of requirements from the given file.
    '''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='introversion-extroversion-ml',
    version='0.0.1',
    author='Amar',
    author_email='amarpoji1999@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
