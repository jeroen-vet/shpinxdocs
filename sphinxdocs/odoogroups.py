#from sphinx.application import Sphinx
import docutils
# add customer role group to refer to odoo user roles
def setup(app):
    app.add_crossref_type('group','group', 'group: %s',docutils.nodes.emphasis)

