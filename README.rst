.. contents:: Table of contents
   :depth: 2

Installation
============
Install the sphinx-sagecell-ext from PyPI
-----------------------------------------
::

    $ sudo pip install sphinx-sagecell-ext

Install the sphinx-sagecell-ext from GitHub
-------------------------------------------
::

    $ sudo pip install git+git://github.com/korniichuk/sphinx-sagecell-ext#egg=sphinx-sagecell-ext

Upgrade the sphinx-sagecell-ext from PyPI
-----------------------------------------
::

    $ sudo pip install -U sphinx-sagecell-ext

or::

    $ sudo pip install --upgrade sphinx-sagecell-ext

Uninstall the sphinx-sagecell-ext
---------------------------------
::

    $ sudo pip uninstall sphinx-sagecell-ext

Development installation
========================
::

    $ git clone git://github.com/korniichuk/sphinx-sagecell-ext.git
    $ cd sphinx-sagecell-ext
    $ sudo pip install .

Quickstart
==========
**First**, copy ``layout.html`` file to ``_templates`` documentation directory::

    $ wget -P DEST https://raw.githubusercontent.com/korniichuk/sphinx-sagecell-ext/master/layout.html

Where:

* ``DEST`` -- a path to ``_templates`` documentation directory.

Example::

    $ wget -P ~/sphinx-sagecell-ext/source/_templates https://raw.githubusercontent.com/korniichuk/sphinx-sagecell-ext/master/layout.html

**Second**, add ``sphinx-sagecell-ext.sagecell`` extension to ``conf.py`` documentation file:::

    extensions = [
        'sphinx-sagecell-ext.sagecell'
    ]
