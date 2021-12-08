# -*- coding: utf-8 -*-

"""Configuration for the Sphinx documentation builder."""
import os
import re
import sys

sys.path.append(os.path.abspath('_python'))
from autosum import AutoAutoSummary


def load_version(filepath_init):
    """Load version from variable __version__ in file __init__.py"""
    try:
        with open(filepath_init) as file_handle:
            file_content = file_handle.read()
        re_for_version = re.compile(r'''__version__\s+=\s+['"](.*)['"]''')
        match = re_for_version.search(file_content)
        version = match.group(1)
        print()
        print('Automatically detected version of the package '
              'from __version__ variable in __init__.py: {}'.format(version))
        print()
        return version
    except Exception as excp:
        message = (
            'Failed to load version string from __version__ variable in '
            '__init__.py in the package directory.')
        raise ValueError(message)



# -- Project information -----------------------------------------------------

project = 'gravis'
copyright = '2018-2021, Robert Haas (Vienna, Austria)'
author = 'Robert Haas'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = load_version(os.path.join('..', '..', 'gravis', '__init__.py'))



# -- General configuration ---------------------------------------------------

# Minimal Sphinx version for build
needs_sphinx = '1.7.4'

# Sphinx extension module names, see https://www.sphinx-doc.org/en/master/usage/extensions
extensions = [
    'sphinx.ext.autodoc',      # auto-generate documentation from docstrings
    'sphinx.ext.viewcode',     # links to highlighted source code for documented code objects
    'sphinx.ext.napoleon',     # support for Google and NumPy docstrings
    'sphinx.ext.autosummary',  # function/method/attribute summary lists
    'sphinx.ext.intersphinx',  # link to objects in external documentation
    'sphinx.ext.githubpages',  # creates .nojekyll file on generated HTML directory
    'nbsphinx',                # execute Jupyter notebooks and include HTML output in docs
    'IPython.sphinxext.ipython_console_highlighting',  # syntax-highlighting in Jupyter Notebooks
]

# Sphinx configuration
# - http://www.sphinx-doc.org/en/master/usage/configuration.html
add_module_names = False

# Relative path to package
sys.path.insert(0, os.path.abspath('../..'))

# Relative path to templates
templates_path = ['_templates']

# Relative path to examples
# - https://github.com/spatialaudio/nbsphinx/issues/170
# - https://github.com/vidartf/nbsphinx-link ... did not work
# - solved by copying example files into docs folder via Makefile
#   and removing them afterwards

# The suffix(es) of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'



# -- Options for HTML output -------------------------------------------------

# Read the Docs (RTD) Sphinx Theme
# - https://sphinx-rtd-theme.readthedocs.io/en/latest
# - https://github.com/rtfd/sphinx_rtd_theme
# - Caution: The Makefile copies a modified JS file into the theme's folder
#   before docs generation, effectively using a modified RTD theme.
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# - https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html
html_theme_options = {
    'logo_only': True,
    'titles_only': False,
}
html_logo = 'images/gravis.svg'

# Relative paths to custom static files (overwrite builtin static files)
html_static_path = ['_static']



# -- Extension configuration -------------------------------------------------

# intersphinx
intersphinx_mapping = {'https://docs.python.org/3/': None}

# autodoc
# - http://www.sphinx-doc.org/en/stable/ext/autodoc.html#confval-autodoc_member_order
autodoc_member_order = 'bysource'

# napoleon
# - https://github.com/sphinx-doc/sphinx/issues/2135
napoleon_use_param = False
# - https://wwoods.github.io/2016/06/09/easy-sphinx-documentation-without-the-boilerplate
napoleon_use_rtype = False
# - https://wwoods.github.io/2016/06/09/easy-sphinx-documentation-without-the-boilerplate
napoleon_numpy_docstring = True
napoleon_google_docstring = False
# - https://www.simonho.ca/programming/automatic-python-documentation
napoleon_use_ivar = True

# autosummary
# - https://romanvm.pythonanywhere.com/post/autodocumenting-your-python-code-sphinx-part-ii-6/
autosummary_generate = True

# nbsphinx
# - https://nbsphinx.readthedocs.io
nbsphinx_execute = 'always'     # execute Notebooks even if they have stored output cells
nbsphinx_timeout = 10*60        # fail if a cell execution takes too long
nbsphinx_allow_errors = False   # fail if a cell execution raises an Exception
nbsphinx_prompt_width = '1200'  # width of input and output prompts in HTML
nbsphinx_requirejs_path = ''    # prevent nbsphinx from loading RequireJS


def setup(app):
    # Use a self-defined class to auto-generate an index
    app.add_directive('autoautosummary', AutoAutoSummary)
    # Use a self-defined CSS file to modify HTML appearance
    app.add_css_file('css/custom.css')
    # Use a JS file to add RequireJS for Plotly plots
    app.add_js_file('js/require.js')
