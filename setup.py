"""Setup script for lyric-ppt"""

import os.path
import setuptools

ROOT = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(ROOT, "README.md")) as fid:
    README = fid.read()

# This call to setup() does all the work
setuptools.setup(
    name="lyric-ppt",
    version="1.0.0",
    author="William JIANG",
    author_email="williamjiang0218@gmail.com",
    description="Generate PPT from lyric defined in *.md files.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Cruisoring/lyric-ppt",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where='src'),
    include_package_data=True,
    install_requires=[],
)