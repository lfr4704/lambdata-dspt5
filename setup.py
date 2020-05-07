# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="my-lambdata-pt5", # the name that you will install via pip
    version="1.0",
    author="Luis Robles",
    author_email="lfr4704@gmail.com",
    description="My first python package",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/lfr4704/lambdata-dspt5",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)
