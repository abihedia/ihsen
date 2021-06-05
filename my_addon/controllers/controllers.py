# -*- coding: utf-8 -*-
# from odoo import http


# class MyAddon(http.Controller):
#     @http.route('/my_addon/my_addon/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_addon/my_addon/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_addon.listing', {
#             'root': '/my_addon/my_addon',
#             'objects': http.request.env['my_addon.my_addon'].search([]),
#         })

#     @http.route('/my_addon/my_addon/objects/<model("my_addon.my_addon"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_addon.object', {
#             'object': obj
#         })
