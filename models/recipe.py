# -*- coding: utf-8 -*-

from odoo import models, fields, api

class recipe (models.Model):
    _name = 'g2modulojjg.recipe'



    idRecipe = fields.char(required= True)
    name = fields.char
    preparation = fields.Text
    recipeType = fields.Enum
    createDate = fields.Date
    dietist = fields.Many2one('res.user',ondelete = 'set null',string= 'Dietist')
    foods = fields.Many2many('g2modulojjg.food', string = 'Food')
    diets = fields.Many2many ('g2modulojjg.diet', string = 'Diet')
    
  