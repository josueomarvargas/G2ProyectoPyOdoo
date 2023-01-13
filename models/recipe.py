# -*- coding: utf-8 -*-

from odoo import models, fields, api

class recipe(models.Model):
    _name = 'g2modulojjg.recipe'
    idRecipe = fields.Char
    #name = fields.Char
    #preparation = fields.Text
    #recipeType = fields.Enum
    #createDate = fields.Date
    #dietist = fields.Many2one('res.user',ondelete = 'set null',string= 'Recipe_dietist')
    #foods = fields.Many2many('g2modulojjg.food', string = 'Recipe_food')
    #diets = fields.Many2many ('g2modulojjg.diet', string = 'Recipe_diet')
    
  