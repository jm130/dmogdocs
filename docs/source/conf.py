# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'DMOG docs'
copyright = '2024 - Jose M Menendez, Graeme Pollock'
author = 'Jose M Menendez, Graeme Pollock'

release = '1.0'
version = '1.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = '_static/HWU_logo.svg'
html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'style_nav_header_background': '#c2ddf0',
    'sticky_navigation': False,
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
