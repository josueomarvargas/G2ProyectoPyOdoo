# -*- coding: utf-8 -*-

from odoo import models, fields, api
class food(models.Model):
    _name = 'g2modulojjg.food'
    idFood = fields.Char()
    name=fields.Char()
    calories = fields.Float()
    carbohydrate = fields.Float()
    totalFat = fields.Float()
    proteins=fields.Float()
    foodType= fields.Enum()
    insertDate= fields.Date()
    recipes= fields.Many2many('g2modulojjg.recipes',string= "Recipes")
    dietist= fields.Many2one('res.users',ondelete='set null', string='Dietist', required=True)
