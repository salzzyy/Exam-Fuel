from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Eaxm Fuel",
    version="0.1",
    author="Saloni Singh",
    packages=find_packages(),
    install_requires = requirements,
)
