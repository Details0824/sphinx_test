# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../trojanzoo_sphinx_theme'))


# -- Project information -----------------------------------------------------

project = 'test'
copyright = '2022, liss'
author = 'liss'

# The full version, including alpha/beta/rc tags
release = '1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'trojanzoo_sphinx_theme'

html_theme_options = {
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'display_version': True,
    # 'prev_next_buttons_location': bottom,
    'style_external_links': False,

    'gitlab_url': 'http://192.168.7.149:1080/framework/tecomodels/-/tree/develop/pytorch',
    'home_url': 'http://127.0.0.1:8000/index.html',

    # 'collapsedSections': '',
    'doc_items':  { 
         'Pytorch': '/index.html', 
         'TensorFlow': '/tensorflow', 
         'PaddlePaddle': '/paddle', 
         # 'base': 'https://github.com/ain-soph/base', 
     }, 

    'logo': '_static/imgs/Tecorigin_logo.svg',
    'logo_dark': '_static/imgs/Teco_logo.svg',
    'logo_icon': '_static/imgs/Tecorigin_logo.svg',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
