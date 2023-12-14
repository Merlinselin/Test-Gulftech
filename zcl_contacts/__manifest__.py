# -*- coding: utf-8 -*-
###################################################################################

# Author       :  Abin suresh
# Copyright(c) :  2023-Present Zinfog Codelabs Pvt Ltd (<https://www.zinfog.com>).
# License      :  LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

# This program is free software:
# you can modify it under the terms of the GNU Lesser General Public License (LGPL) as
# published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

###################################################################################

{
    "name"         : "Contacts",
    "summary"      : """ Contacts """,
    "category"     : "Zinfog",
    "version"      : "16.0.1.0.0",
    "author"       : "Zinfog Codelabs Pvt Ltd",
    "license"      : "LGPL-3",
    "website"      : "https://www.zinfog.com",
    "description"  : """ Contacts """,
    "depends"      : ['base', 'mail','contacts'],
    "data"         : ['security/security.xml',
                      'security/ir.model.access.csv',
                      'data/walkin_customer_data.xml',
                      'views/view_remove.xml',
                      'views/walk_in_customer.xml',
                      'views/customer.xml',
                      'views/vendor.xml',
                      'views/sales_man.xml',
                      'views/branch_view.xml',
                      'views/res_user_inherit.xml',
                      'views/payment_terms_view.xml',
                      'views/menus.xml',
                      ],
    "application"  : True,
    "installable"  : True,
    "auto_install" : False,
}
