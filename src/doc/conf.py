# -*- coding: utf-8 -*-
import os
import sys

on_rtd = os.environ.get("READTHEDOCS", None) == "True"

# http://read-the-docs.readthedocs.org/en/latest/faq.html#i-get-import-errors-on-libraries-that-depend-on-c-modules
autodoc_mock_imports = ["pytz"]
# MOCK_MODULES = ["pytz"]
# if MOCK_MODULES and on_rtd:
#     from unittest.mock import MagicMock

#     class Mock(MagicMock):
#         @classmethod
#         def __getattr__(cls, name):
#             return Mock()

#     sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)

# region General configuration ----------------------------------------------------

project = "Astral"
author = "Simon Kennedy"
copyright = "2009-2020, %s" % author
version = "2.0"
release = "2.0.2"

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ["sphinx.ext.autodoc", "sphinx.ext.intersphinx", "sphinx.ext.napoleon"]

# intersphinx_mapping = {"python": ("http://docs.python.org/3", None)}
intersphinx_mapping = {"python": ("http://docs.python.org/3", "python3_intersphinx.inv")}

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.join(os.path.abspath("..")))

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8'

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
# unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = []

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ["templates"]
# endregion

# region Options for HTML output ---------------------------------------------------

if not on_rtd:
    project_home = os.environ.get("PROJECT_HOME", None)
    if not project_home:
        dev_home = os.environ.get("DEV_HOME", None)
        if dev_home:
            project_home = os.path.join(os.path.expanduser(dev_home), "projects")
    else:
        project_home = os.path.expanduser(project_home)

    html_theme = None
    if project_home:
        theme_root = os.path.relpath(os.path.join(project_home, "themes", "sphinx"))
        if os.path.exists(theme_root):
            html_theme_path = [theme_root]
            html_theme = "sffjunkie"

    if not html_theme:
        html_theme = "traditional"
# else:
#     html_theme = "basic"

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = os.path.join("static", "earth_sun.png")

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
if not on_rtd:
    html_favicon = os.path.join('static', 'weather-sunny.png')

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["static"]

html_css_files = [
    'astral.css',
]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
html_domain_indices = False

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = ''
# endregion

# region Options for HTML Help output --------------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "AstralDoc"
# endregion

# region Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
# latex_paper_size = 'a4'
latex_elements = {"papersize": "a4"}

# The font size ('10pt', '11pt' or '12pt').
# latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [("index", "Astral.tex", "Astral v%s" % release, author, "manual")]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# Additional stuff for the LaTeX preamble.
# latex_preamble = ''

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_use_modindex = True
# endregion
