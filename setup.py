import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="albania_pkg",
    version="3.7.1",
    author="Ryden Kaye",
    author_email="rydenkaye@gmail.com",
    description="a pip installable albanian flag",
    long_description=long_description,
    long_description_content_type="Markdown",
    url="https://github.com/RydenKaye/Albania",
    packages=setuptools.find_packages("albania.pkg"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
