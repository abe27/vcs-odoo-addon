# -*- coding: utf-8 -*-
# from odoo import http


# class RegionThai(http.Controller):
#     @http.route('/region_thai/region_thai', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/region_thai/region_thai/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('region_thai.listing', {
#             'root': '/region_thai/region_thai',
#             'objects': http.request.env['region_thai.region_thai'].search([]),
#         })

#     @http.route('/region_thai/region_thai/objects/<model("region_thai.region_thai"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('region_thai.object', {
#             'object': obj
#         })
