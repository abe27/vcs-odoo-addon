# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


# class province_region_thailand(models.Model):
#     _name = 'province_region_thailand.province_region_thailand'
#     _description = 'province_region_thailand.province_region_thailand'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class RegionThailand(models.Model):
    _name = 'custom_table.region_thailand'
    _description = 'custom_table.region_thailand'

    name = fields.Char(size=50, string="ชื่อ",  required=True)
    description = fields.Text(string="รายละเอียด")
    is_active = fields.Boolean(string="สถานะ", default=True)

    # @api.constrains('name')
    # def _check_duplicate(self):
    #     for rec in self:
    #         domain = [('name', '=', rec.name)]
    #         count = self.sudo().search_count(domain)

    #         if count > 0:
    #             raise ValidationError(("The Name should be unique"))

class Province(models.Model):
    _name = 'custom_table.province'
    _description = 'custom_table.province'

    region_id = fields.Many2one('custom_table.region_thailand', string="ภูมิภาค",  required=True)
    province_id = fields.Char(size=50, string="รหัส",  required=True)
    name = fields.Char(size=50, string="ชื่อ",  required=True)
    description = fields.Text(string="รายละเอียด")
    is_active = fields.Boolean(string="สถานะ", default=True)

    # @api.constrains('name')
    # def _check_duplicate(self):
    #     for rec in self:
    #         domain = [('name', '=', rec.name)]
    #         count = self.sudo().search_count(domain)

    #         if count > 0:
    #             raise ValidationError(("The Name should be unique"))

class District(models.Model):
    _name = 'custom_table.district'
    _description = 'custom_table.district'

    province_id = fields.Many2one('custom_table.province', string="รหัสจังหวัด",  required=True)
    code = fields.Char(size=20, string="รหัส")
    name = fields.Char(size=50, string="ชื่อ",  required=True)
    description = fields.Text(string="รายละเอียด")
    is_active = fields.Boolean(string="สถานะ", default=True)

class Tambon(models.Model):
    _name = 'custom_table.tambon'
    _description = 'custom_table.tambon'

    district_id = fields.Many2one('custom_table.district.code', string="รหัสอำเภอ",  required=True)
    code = fields.Char(size=20, string="รหัส", required=True)
    name = fields.Char(size=50, string="ชื่อ",  required=True)
    zip_code = fields.Char(size=5, string="รหัสไปษณี")
    description = fields.Text(string="รายละเอียด")
    is_active = fields.Boolean(string="สถานะ", default=True)
