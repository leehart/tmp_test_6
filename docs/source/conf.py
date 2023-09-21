# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'malariagen_data API'
copyright = '2023, MalariaGEN'
author = 'MalariaGEN'
release = 'v7.13.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary'
]

autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

#html_theme = 'alabaster'
html_theme = "pydata_sphinx_theme"

# https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/version-dropdown.html
# In theory the JSON could be saved in a folder that is listed under your 
# site’s html_static_path configuration, but this is not recommended. 
# If you want to do it this way, see the Sphinx static path documentation 
# for more information but do so knowing that we do not support this use case.
#
# See https://github.com/pydata/pydata-sphinx-theme/issues/1389
#
html_theme_options = {
    "switcher": {
        "json_url": "https://leehart.github.io/tmp_test_6/switcher.json",
    },
    "check_switcher": True,
    "switcher": {
        "version_match": release,
    },
    "navbar_start": ["navbar-logo", "version-switcher"]
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Relative paths are taken as relative to the configuration directory. 
# They are copied to the output directory. They will overwrite any existing file 
# of the same name. As these files are not meant to be built, they are automatically 
# excluded from source files.
html_extra_path = ['extra']