# -*- coding: utf-8 -*-

from odoo import models, fields

class diet(models.Model):
    _name = 'g2modulojjg.diet'
    name = fields.Char()
    idDiet = fields.Char(required=True)
    timeDiet = fields.Integer()
    objectiveDiet = fields.Date()
   # dietType = fields.Selection([('OMNIVORO'),('VEGANA'),('VEGETARIANO')],string="Tipo Dieta")
    recipes = fields.Many2many('g2modulojjg.recipe',string="Recipe")
    clients = fields.Many2many('res.users', string="Clients")
    dietits = fields.Many2one('g2modulojjg.diet', ondelete='cascade',string="Dietist", required=True)
    
