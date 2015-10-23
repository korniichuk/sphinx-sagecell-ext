# -*- coding: utf-8 -*-

from os.path import dirname, join
from setuptools import setup

setup(
    author = "Ruslan Korniichuk",
    author_email = "ruslan.korniichuk@gmail.com",
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Framework :: Sphinx",
        "Framework :: Sphinx :: Extension",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "License :: Public Domain",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 2 :: Only",
        "Topic :: Documentation",
        "Topic :: Documentation :: Sphinx",
        "Topic :: Scientific/Engineering"
    ],
    description = ("The Sphinx extension "
                   "embedding a Sage cell into a webpage"),
    download_url = ("https://github.com/korniichuk/sphinx-sagecell-ext/"
                    "archive/0.1.zip"),
    include_package_data = True,
    install_requires = [
        "Sphinx"
    ],
    keywords = ["extension", "python2", "sagecell", "sphinx",
                "sphinx-sagecell-ext"],
    license = "Public Domain",
    long_description = open(join(dirname(__file__), "README.rst")).read(),
    name = "sphinx-sagecell-ext",
    packages = ["sphinx-sagecell-ext"],
    platforms = ["Linux"],
    url = "https://github.com/korniichuk/sphinx-sagecell-ext",
    version = "0.1b1",
    zip_safe = True
)
