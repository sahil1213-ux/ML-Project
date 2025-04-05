# this file is used to install the package and mainly it is used as the project descriptor file
# it contains the meta data about the project and it can be installed as package or tool like we install seaborn package etc.

# when find_packages() is used, it will find all the packages in the current directory and subdirectories using __init__.py file
# it is used to create a package and install it using pip

from setuptools import setup, find_packages
from typing import List

HYPEN_PACKAGE = '-e .' # when we use -e . in requirements.txt, it helps to install the package automatically
# it is used to install the package in editable mode
 
def get_requirements(file_path:str)-> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPEN_PACKAGE in requirements:
            requirements.remove(HYPEN_PACKAGE)
    return requirements

setup(
    name='ML-Project',
    version='0.0.1',
    author='Sahil Anand',
    author_email='sahilanand00027@gmail.com',
    description='A simple ML project',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt'),
)