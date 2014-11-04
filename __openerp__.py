#==============================================================================
#                                                                             =
#    l10n_cm_paye module for Odoo, Module de gestion de la paye Camerounaise
#    Copyright (C) 2014 OpenERP Cameroun (<http://www.openerp-cameroun.com>)
#                       Clovis Nzouendjou <nzouendjou2002@yahoo.fr>
#                                                                             =
#    This file is a part of l10n_cm_paye
#                                                                             =
#    l10n_cm_paye is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License v3 or later
#    as published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#                                                                             =
#    l10n_cm_paye is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License v3 or later for more details.
#                                                                             =
#    You should have received a copy of the GNU Affero General Public License
#    v3 or later along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#                                                                             =
#==============================================================================

{
    'name': 'l10n_cm_paye',
    'category': 'Localization/Payroll',
    'author': 'OpenERP Cameroun',
    'version': '1.0',
    'sequence': 150,
    'website': 'http://www.openerp-cameroun.com',
    'description': """
        Module de gestion de la paye Camerounaise
        =========================================

    """,
    'depends': ['hr_payroll', ],
    'data': [
        'l10n_cm_paye_view.xml',
        'l10n_cm_paye_data.xml',
    ],
    'init': [

    ],
    'test': [
    ],
    'demo': [
    ],
    'js': [
    ],
    'qweb': [
    ],
    'css': [
    ],
    'icon': '',
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'AGPL-3',
}
