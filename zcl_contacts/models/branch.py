# -*- coding: utf-8 -*-
###################################################################################

# Author       :  Sayooj t k ,Merlin Thomas
# Copyright(c) :  2023-Present Zinfog Codelabs Pvt Ltd (<https://www.zinfog.com>).
# License      :  LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

# This program is free software:
# you can modify it under the terms of the GNU Lesser General Public License (LGPL) as
# published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

###################################################################################

from odoo import fields, models


class BranchDetails(models.Model):
    _name = 'branch.branch'
    _description = "Branch"
    _rec_name = "branch"

    branch = fields.Char(string="Branch")
    branch_categories = fields.Selection([
        ('shop', 'Shop'),
        ('store', 'Store'),
    ], string="Branch Categories", required=True)