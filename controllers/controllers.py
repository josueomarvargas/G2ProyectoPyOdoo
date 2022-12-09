# -*- coding: utf-8 -*-
from odoo import http

# class G2modulojjg(http.Controller):
#     @http.route('/g2modulojjg/g2modulojjg/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/g2modulojjg/g2modulojjg/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('g2modulojjg.listing', {
#             'root': '/g2modulojjg/g2modulojjg',
#             'objects': http.request.env['g2modulojjg.g2modulojjg'].search([]),
#         })

#     @http.route('/g2modulojjg/g2modulojjg/objects/<model("g2modulojjg.g2modulojjg"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('g2modulojjg.object', {
#             'object': obj
#         })