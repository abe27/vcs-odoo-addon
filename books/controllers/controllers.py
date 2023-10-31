# -*- coding: utf-8 -*-
# from odoo import http


# class Books(http.Controller):
#     @http.route('/books/books', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/books/books/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('books.listing', {
#             'root': '/books/books',
#             'objects': http.request.env['books.books'].search([]),
#         })

#     @http.route('/books/books/objects/<model("books.books"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('books.object', {
#             'object': obj
#         })
