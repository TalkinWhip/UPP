from setuptools import setup

setup(
    name="src",
    version="0.1",
    packages=["src", "src.domain"],
)

# $python3 setup.py sdist; python setup.py build; python setup.py install
