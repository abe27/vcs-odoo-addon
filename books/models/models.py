# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class books(models.Model):
    _name = 'custom.books'
    _description = 'custom.books'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    # skid = models.CharField(max_length=50, verbose_name="Key", unique=True, blank=False, null=False)
    # corporation_id = models.ForeignKey(Corporation, blank=True, null=True, on_delete=models.SET_NULL)
    # order_type_id = models.ForeignKey(RefType, verbose_name="Type ID", on_delete=models.SET_NULL, null=True)
    # filter_product_type = models.ManyToManyField(ProductType, blank=True, verbose_name="Filter Product Type ID",null=True)
    # code = models.CharField(max_length=50, verbose_name="Code", blank=False, null=False)
    # name = models.CharField(max_length=250, verbose_name="Name", blank=False, null=False)
    # prefix = models.CharField(max_length=250, verbose_name="Prefix", blank=True, null=True)
    # description = models.TextField(verbose_name="Description",blank=True, null=True)
    # is_active = models.BooleanField(verbose_name="Is Active", default=True)
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
