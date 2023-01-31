# -*- coding: utf-8 -*-

from odoo import models, fields,api,exceptions
class food(models.Model):
    _name='g2modulojjg.food'
    name=fields.Char()
    idFood = fields.Char()
    calories = fields.Float()
    carbohydrate = fields.Float()
    totalFat = fields.Float()
    proteins=fields.Float()
    #foodType= fields.Selection([('CEREAL'),('CARNE'),('LEGUMBRE'),('HORTALIZA'),('FRUTA'),('LECHE_DERIVADOS'),('MATENCA_ACEITE')],string="Tipo Alimento")
    insertDate= fields.Date()
    recipes= fields.Many2many('g2modulojjg.recipe',string= "Recipes")
    dietist= fields.Many2one('res.users',ondelete='cascade', string="Dietist", required=True)
    @api.onchange('calories','carbohydrate','totalFat','calories','proteins','calories')
    def _verify_valid_Positive(self):
        if self.calories < 0:
            return {
                'warning': {
                    'title': "Incorrect 'calories' value",
                    'message': "The number of available calories may not be negative",
                },
            }
        if self.carbohydrate < 0:
            return {
                'warning': {
                    'title': "Incorrect 'carbohydrate' value",
                    'message': "The number of available carbohydrate may not be negative",
                },
            }
        if self.totalFat < 0:
            return {
                'warning': {
                    'title': "Incorrect 'totalFat' value",
                    'message': "The number of available totalFat may not be negative",
                },
            }            
        if self.proteins < 0:
            return {
                'warning': {
                    'title': "Incorrect 'proteins' value",
                    'message': "The number of available proteins may not be negative",
                },
            }
   