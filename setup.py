from setuptools import setup
from setuptools import find_packages

version_py = "MutSeq/_version.py"
exec(open(version_py).read())

setup(
    name="MutSeq", # Replace with your own username
    version=__version__,
    author="Benxia Hu",
    author_email="hubenxia@gmail.com",
    description="generate in silicon point mutations",
    long_description="generate in silicon point mutations in each position in a given DNA sequence",
    url="https://pypi.org/project/MutSeq/",
    entry_points = {
        "console_scripts": ['MutSeq = MutSeq:main',]
        },
    python_requires = '>=3.6',
    packages = ['MutSeq'],
    install_requires = [
        'pandas',
        'argparse',
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    zip_safe = False,
  )