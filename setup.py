import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="asmaulhusna",
    packages=setuptools.find_packages(),
    version="0.0.1",
    author="Izan Majeed",
    author_email='izanmajeed03@gmail.com',
    url='https://github.com/izan-majeed/Asma-ul-Husna-Pypi',
    description="Get all the 99 names of Allah",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
