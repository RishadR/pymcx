# Write a setuptools setup file for the package.
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="pymcx",
    version="0.0.1",
    author="Aidan O'Brien",
    description="A Python wrapper for the MCX Monte Carlo photon transport simulator",
)
