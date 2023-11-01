# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Whouse(models.Model):
    _name = 'custom.whouse'
    _description = 'custom.whouse'

    code = fields.Char(size=10, string="Code", required=True)
    name = fields.Char(size=50, string="Name", required=True)
    description = fields.Text(string="Description")
    is_active = fields.Boolean(string="Is Active")

class RefType(models.Model):
    _name = 'custom.ref_type'
    _description = 'custom.ref_type'

    code = fields.Char(size=10, string="Code", required=True)
    name = fields.Char(size=50, string="Name", required=True)
    description = fields.Text(string="Description")
    is_active = fields.Boolean(string="Is Active")

class Books(models.Model):
    _name = 'custom.books'
    _description = 'custom.books'

    ref_type = fields.Many2one('custom.ref_type.code', string="Ref. Type", required=True)
    code = fields.Char(size=10, string="Code", required=True)
    name = fields.Char(size=250, string="Name", required=True)
    prefix = fields.Char(size=250, string="Prefix")
    description = fields.Text(string="Description")
    is_active = fields.Boolean(string="Is Active")

class BookingDetails(models.Model):
    _name = 'custom.book_detail'
    _description = 'custom.book_detail'

    booking_id = fields.Many2one('custom.books', string="Booking ID", required=True)
    factory_type = fields.Selection([('F','From WHS'), ('T', 'To WHS')], string="Select Type")
    whouse_id = fields.Many2one('custom.whouse', string="Whouse ID", required=True)
    description = fields.Text(string="Description")
    is_active = fields.Boolean(string="Is Active")
