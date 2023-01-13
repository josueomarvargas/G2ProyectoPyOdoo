# -*- coding: utf-8 -*-

from odoo import models, fields
class food(models.Model):
    _name='g2modulojjg.food'
    name=fields.Char()
    idFood = fields.Char()
    calories = fields.Float()
    carbohydrate = fields.Float()
    totalFat = fields.Float()
    proteins=fields.Float()
    foodType= fields.Selection([('CEREAL'),('CARNE'),('LEGUMBRE'),('HORTALIZA'),('FRUTA'),('LECHE_DERIVADOS'),('MATENCA_ACEITE')],string='Tipo Alimento')
    insertDate= fields.Date()
    recipes= fields.Many2many('g2modulojjg.recipe',string= "Recipes")
    dietist= fields.Many2one('res.users',ondelete='cascade', string="Dietist", required=True)
