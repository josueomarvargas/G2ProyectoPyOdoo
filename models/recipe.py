# -*- coding: utf-8 -*-

from odoo import api
from odoo import exceptions
from odoo import fields
from odoo import models
class recipe(models.Model):
    _name = 'g2modulojjg.recipe'
    name = fields.Char()
    idRecipe = fields.Char()
    preparation = fields.Text()
    #recipeType = fields.Selection([('OMNIVORO'),('VEGANA'),('VEGETARIANO')],string="Tipo Receta")
    createDate = fields.Date()
    dietist1 = fields.Many2one('res.users', ondelete='cascade', string="Dietist", required=True)
    foods = fields.Many2many('g2modulojjg.food', string="Food")
    diets = fields.Many2many ('g2modulojjg.diet', string="Diet")
    
    
    @api.constrains('createDate')
    def _verify_create_date(self):
        if self.createDate > fields.Date.today():
            raise exceptions.ValidationError("Create date can´t be after current one")
        
    @api.onchange('createDate')
    def _verify_create_date2(self):
        if self.createDate > fields.Date.today():
            raise exceptions.ValidationError("Create date can´t be after current one")
       
  
        
   