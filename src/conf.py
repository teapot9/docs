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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'config'
copyright = '2022, Louis Leseur'
author = 'Louis Leseur'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.intersphinx',
]

# External documentations
intersphinx_mapping = {
    'kernel': ('https://docs.kernel.org/', None),
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['static']
html_css_files = [
    'css/custom.css',
]

from docutils import nodes
from docutils.parsers.rst.roles import set_classes

def mytest(name, rawtext, text, lineno, inliner, options=None, content=None):
    if options is None:
        options = {}
    if content is None:
        content = []

    with open('/tmp/sphinx', 'a') as f:
        f.write(f"name={name}; rawtext={rawtext}; text={text}; line={lineno}; inliner={inliner}\n")
    set_classes(options)
    node = nodes.reference(rawtext, "voiture", refuri="http://google.com", **options)
    return [node], []

def sysctl(name, rawtext, text, lineno, inliner, options=None, content=None):
    if options is None:
        options = {}
    if content is None:
        content = []

    split = text.split('.')
    #path = '/'.join(split[:-1])
    path = split[0]
    name = split[-1].replace('_', '-')
    url = f'https://docs.kernel.org/admin-guide/sysctl/{path}.html#{name}'

    set_classes(options)
    node = nodes.reference(rawtext, text, refuri=url, **options)
    return [node], []

def setup(app):
    app.add_role('sysctl', sysctl)
