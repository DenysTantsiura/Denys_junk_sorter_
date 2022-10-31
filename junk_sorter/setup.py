from importlib.metadata import entry_points
from setuptools import setup, find_namespace_packages

setup(
    name='junk_sorter',
    version='4.0.1',
    description='Creation of the fourth version of the sorter of '
    'personal junk (files of different categories in one pile) '
            'by category.',
    url='https://github.com/DenysTantsiura/junk_sorter_.git',
    author='Denys Tantsiura',
    author_email='tdv@tesis.kiev.ua',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': [
        'junk-sorter = junk_sorter.junk_sorter:main',
        'jsa = junk_sorter.junk_sorter:print_author']}
)
"""
The package is installed in the system by the command:
 pip install -e . 
 (or :
python setup.py install
, administrator rights are required!)
"""
