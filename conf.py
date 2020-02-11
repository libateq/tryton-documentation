# Configuration file for the Tryton Documentation.
# This file is part of the tryton-documentation project.
# Please see the README file at the top level of this repository for the full
# copyright notices, license terms and support information.
from datetime import date
from sphinxcontrib.tryton.inherit import inherit_installed_modules as inherit_modules  # noqa
import ssl


def get_copyright(first_year, current_year, author):
    years = first_year
    if first_year != current_year:
        years = '{}-{}'.format(first_year, current_year)
    return '{}, {}'.format(years, author)


def get_version(release):
    second_point = release.find('.', release.find('.')+1)
    return release[:second_point]


# Project information
project = "Tryton Documentation"
description = "Tryton Documentation"
author = "David Harper"
copyright = get_copyright(2019, date.today().year, author)
release = '0.1.0'
version = get_version(release)

# General settings
extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinxcontrib.inherit',
    'sphinxcontrib.tryton',
    ]
master_doc = 'index'
exclude_patterns = [
    '.*',
    'README.rst',
    'common',
    ]
language = None
pygments_style = None
source_suffix = {'.rst': 'restructuredtext'}
templates_path = []

# Auto section label settings
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 2

# Inheritance settings
inherit_modules_dir = 'modules'

# Tryton settings
trytond_activate_modules = []

# HTML output settings
html_static_path = []

# LaTeX output settings
latex_elements = {'papersize': 'a4paper'}
latex_documents = [
    (master_doc, project + '.tex', project, author, 'manual', False),
    ]

# Man page output settings
man_pages = [
    (master_doc, project.replace('-', ''), project, [author], 1),
    ]

# Texinfo output settings
texinfo_documents = [
    (master_doc, project, project, author, project,
     description, 'Miscellaneous', False),
    ]

# Epub output settings
epub_title = project
epub_exclude_files = ['search.html']
