# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import subprocess
import sys

# Generate the api
if sys.platform in ["linux", "darwin"]:
    subprocess.check_output(["make", "generate-api"], cwd=os.path.dirname(os.path.abspath(__file__)))
else:
    subprocess.check_output(["make.bat", "generate-api"], cwd=os.path.dirname(os.path.abspath(__file__)))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Analysis project'
# author = 'Author name'
import methods
release = methods.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# add extensions
# https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.intersphinx']

intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

import sphinx_rtd_theme
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
