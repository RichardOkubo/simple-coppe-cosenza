from os import path
from setuptools import find_packages, setup


def read(filename):
    return [req.strip() for req in open(filename).readlines()]


dir = path.abspath(path.dirname(__file__))

with open(path.join(dir, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name="simple_coppe_cosenza",
    version="0.0.1",
    author="Richard Okubo",
    description="Simple COPPE-COSENZA model in Python.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    install_requires=read("requirements.txt"),
    extras_require={"dev": read("requirements-dev.txt")},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 1 - Planning"
    ],
)
