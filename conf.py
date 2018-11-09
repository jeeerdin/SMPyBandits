#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SMPyBandits documentation build configuration file, created by
sphinx-quickstart on Thu Jan 19 17:20:57 2017.

This file is execfile()d with the current directory set to its
containing dir.

Note that not all possible configuration values are present in this
autogenerated file.

All configuration values have a default; values that are commented out
serve to show the default.
"""
from __future__ import division, print_function  # Python 2 compatibility

import sys
import os
import sphinx
# import shutil

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('SMPyBandits'))
# sys.path.insert(0, os.path.abspath(os.path.join('SMPyBandits', 'Policies')))

print("Using python, version %s on %s." % (sys.version, sys.platform))

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
print("On readthedocs.org ?", on_rtd)  # DEBUG

# -- Generate apidoc from Python code -------------------------------------

has_apidoc = False
if on_rtd:
    if not os.path.isdir('docs'):
        os.mkdir('docs')
    if not os.path.exists(os.path.join('docs', 'Arms.rst')):
        print("WARNING: the docs/*.rst files are not here, we will try to regenerate them.")
        # --- Move files that bother sphinx-apidoc
        if os.path.exists(os.path.join('docs', 'modules.rst')):
            os.replace(os.path.join('docs', 'modules.rst'), os.path.join('docs', 'modules.rst.backup'))
        if os.path.exists(os.path.join('SMPyBandits', '__init__.py')):
            os.replace(os.path.join('SMPyBandits', '__init__.py'), os.path.join('SMPyBandits', '__init__.py.backup'))
        # --- Then simulate a cli call to sphinx-apidoc
        try:
            from sphinx.ext.apidoc import main as main_apidoc
            has_apidoc = True
        except ImportError:
            print("Failing to import 'apidoc' from 'sphinx.ext'...")  # DEBUG
            try:
                from sphinx.apidoc import main as main_apidoc
                has_apidoc = True
            except ImportError:
                print("Failing to import 'apidoc' from 'ext'...")  # DEBUG
                print("Error: impossible to import 'apidoc', from both 'sphinx.ext' and 'sphinx' ?")  # DEBUG

if on_rtd and has_apidoc:
    if not os.path.exists(os.path.join('docs', 'Arms.rst')):

        os.chdir("SMPyBandits")
        print("Content of '../docs' before calling apidoc:\n", os.listdir(os.path.join("..", "docs")))
        argv = [
            "fake_call_to_sphinx-apidoc",
            # this first argument gets deleted on old versions of sphinx
            # but now it is not, see https://github.com/sphinx-doc/sphinx/blob/31fd657/sphinx/ext/apidoc.py#L385
            "-o", os.path.join("..", "docs"),
            "-f",
            "-e",
            "-M", ".",
        ]
        if sphinx.version_info[:2] < (1, 7):
            print("Sphinx version < 1.7, using apidoc.main(argv) as a hack.")  # DEBUG
            main_apidoc(argv=argv)
        else:
            print("Sphinx version >= 1.7, using apidoc.main(argv[1:]) as a hack.")  # DEBUG
            main_apidoc(argv=argv[1:])
        os.chdir("..")
        # --- Restore files
        if os.path.exists(os.path.join('docs', 'modules.rst.backup')):
            os.replace(os.path.join('docs', 'modules.rst.backup'), os.path.join('docs', 'modules.rst'))
        if os.path.exists(os.path.join('docs', 'modules.rst.backup')):
            os.rename(os.path.join('docs', 'modules.rst.backup'), os.path.join('docs', 'modules.rst'))
        assert not os.path.exists(os.path.join('docs', 'modules.rst.backup'))
        if os.path.exists(os.path.join('SMPyBandits', '__init__.py.backup')):
            os.replace(os.path.join('SMPyBandits', '__init__.py.backup'), os.path.join('SMPyBandits', '__init__.py'))
        if os.path.exists(os.path.join('SMPyBandits', '__init__.py.backup')):
            os.rename(os.path.join('SMPyBandits', '__init__.py.backup'), os.path.join('SMPyBandits', '__init__.py'))
        assert not os.path.exists(os.path.join('SMPyBandits', '__init__.py.backup'))
        # Check
        print("Content of '../docs' after calling apidoc:\n", os.listdir("docs")[:10])


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = '1.5'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'sphinx.ext.intersphinx',  # http://www.sphinx-doc.org/en/stable/ext/intersphinx.html
    # From https://nbsphinx.readthedocs.io/
    'nbsphinx',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst']

# The recommonmark Sphinx extension adds support for Markdown files
# https://github.com/rtfd/recommonmark (and it works very well)
AutoStructify = None
has_AutoStructify = False
try:
    from recommonmark.parser import CommonMarkParser
    source_parsers = {
        '.md': CommonMarkParser,  # *.md are the concerned files
    }
    source_suffix = ['.rst', '.md']
    from recommonmark.transform import AutoStructify
    has_AutoStructify = False
except ImportError:
    print("recommonmark.parser.CommonMarkParser was not found.\nrecommonmark can be installed with 'pip install recommonmark' (from https://github.com/rtfd/recommonmark)")

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'SMPyBandits'
copyright = '2016-2018, Lilian Besson (Naereen)'
author = 'Lilian Besson'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.9'
# The full version, including alpha/beta/rc tags.
release = '0.9.4'

# http://pypi.python.org/pypi/sphinxcontrib-googleanalytics
# https://bitbucket.org/birkenfeld/sphinx-contrib/src/default/googleanalytics/
# useless if built on Read the Docs, see https://read-the-docs.readthedocs.io/en/latest/guides/google-analytics.html
googleanalytics_id = 'UA-38514290-2'

# http://www.sphinx-doc.org/en/stable/ext/intersphinx.html
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference/', None),
    'matplotlib': ('https://matplotlib.org/', None),
    # 'sklearn': ('http://scikit-learn.org/stable/', None),
}

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%d %b %Y, %Hh'
# avoid doing git commits on https://github.com/SMPyBandits/SMPyBandits.github.io/ if you build the doc twice in the same hour!

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = [
    '_build', 'dist',
    '.vscode', '_static', '_templates',
    'Thumbs.db', '.DS_Store',
    '**.ipynb_checkpoints',
    'paper.md', 'longpaper.md', 'paper',
    'docs/paper/paper.md', 'docs/paper/longpaper.md', 'docs/paper',
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


autodoc_default_flags = ['members', 'private-members', 'undoc-members', 'special-members']
# Pour trier dans l'ordre du code et non pas par ordre alphabétique
autodoc_member_order = 'bysource'


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

if not on_rtd:  # only import and set the theme if we're building docs locally
    # To install with 'pip install sphinx_rtd_theme'
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

    try:
        import sphinxcontrib.googleanalytics
        extensions += [
            # From https://bitbucket.org/birkenfeld/sphinx-contrib/
            'sphinxcontrib.googleanalytics',
        ]
    except ImportError:
        print("'sphinxcontrib.googleanalytics' was not found, try to install it manually from 'https://bitbucket.org/birkenfeld/sphinx-contrib/'...")  # DEBUG
        from sphinx.application import ExtensionError

        def add_ga_javascript(app, pagename, templatename, context, doctree):
            if not app.config.googleanalytics_enabled:
                return

            metatags = context.get('metatags', '')
            metatags += """<script type="text/javascript">

            var _gaq = _gaq || [];
            _gaq.push(['_setAccount', '%s']);
            _gaq.push(['_trackPageview']);

            (function() {
                var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
                ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
                var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
            })();
            </script>""" % app.config.googleanalytics_id
            context['metatags'] = metatags

        def check_config(app):
            if not app.config.googleanalytics_id:
                raise ExtensionError("'googleanalytics_id' config value must be set for ga statistics to function properly.")

        def setup(app):
            app.add_config_value('googleanalytics_id', '', 'html')
            app.add_config_value('googleanalytics_enabled', True, 'html')
            app.connect('html-page-context', add_ga_javascript)
            app.connect('builder-inited', check_config)
            return {'version': '0.1'}

# otherwise, readthedocs.org uses their theme by default, so no need to specify it


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# If given, this must be the name of an image file
# (path relative to the configuration directory) that is the logo of the docs.
# It is placed at the top of the sidebar; its width should therefore not exceed 200 pixels. Default: None.
html_logo = 'logo.png'

# Cf. https://recommonmark.readthedocs.io/en/latest/auto_structify.html#inline-math
if has_AutoStructify and AutoStructify is not None:
    # At the bottom of conf.py
    def setup(app):
        app.add_config_value('recommonmark_config', {
                # 'url_resolver': lambda url: github_doc_root + url,
                # 'auto_toc_tree_section': 'Contents',
                'enable_math': True,
                'enable_inline_math': True,
            }, True)
        app.add_transform(AutoStructify)
