from setuptools import find_packages
from setuptools import setup

setup(
    name='pupper_interfaces',
    version='0.0.0',
    packages=find_packages(
        include=('pupper_interfaces', 'pupper_interfaces.*')),
)
