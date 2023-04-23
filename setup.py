import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="text-box-wrapper",
    version="0.1.0",
    description="A simple package to wrap text with ASCII art",
    author="Ho",
    author_email="hhtjim@gmail.com",
    packages=find_packages(),
    install_requires=[
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],

    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hootrix/text-box-wrapper",

)
