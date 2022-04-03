# -*- coding: utf-8 -*-
from odoo import http

# class CraptHack(http.Controller):
#     @http.route('/crapt_hack/crapt_hack/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crapt_hack/crapt_hack/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('crapt_hack.listing', {
#             'root': '/crapt_hack/crapt_hack',
#             'objects': http.request.env['crapt_hack.crapt_hack'].search([]),
#         })

#     @http.route('/crapt_hack/crapt_hack/objects/<model("crapt_hack.crapt_hack"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crapt_hack.object', {
#             'object': obj
#         })