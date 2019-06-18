# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "Sphinx Documentation",
    "version": "12.0.1.0.0",
    "author": "eXcec Consulting Ltd.",
    "maintainer": "eXcec Consulting Ltd.",
    "website": "http://www.excecbc.com",
    "category": "Web",
    "license": "AGPL-3",
    'summary': 'User Documentation with Sphinx',
    "description": "Sphinx  User documentation available through the user menu. Put your Sphinx files in the top directory of the module and issue make html command to generate the documentation.",
    "depends": [
            "web","base",
    ],
    "data": [
       "templates.xml",
    ],
    "qweb": [
       "base.xml",
    ],    
    "installable": True,
}
