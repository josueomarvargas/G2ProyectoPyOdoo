# -*- coding: utf-8 -*-

from odoo import models, fields

class diet(models.Model):
    _name = 'g2modulojjg.diet'
    
    idDiet = fields.Char(required=True)
    name = fields.Char()
    time = fields.Integer()
    objective = fields.Date()
    dietType = fields.Selection(requeried=True)
    recipes = fields.Many2many('g2modulojjg.recipe','recipe')
    clients = flieds.Many2many('res.users')
    dietits = fields.Many2one('res.users')
    
