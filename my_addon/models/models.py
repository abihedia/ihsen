-*- coding: utf-8 -*-

from odoo import models, fields, api


class my_addon(models.Model):
    _inherit = 'res.partner'
    _description = 'my_addon.my_addon'

    birthday = fields.Datetime(string='Date of birth')
    
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
