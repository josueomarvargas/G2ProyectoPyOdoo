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
    createDate = fields.Date(string='Field Name', default=fields.Date.today())
    dietist1 = fields.Many2one('res.users', ondelete='cascade', string="Dietist", required=True)
    foods = fields.Many2many('g2modulojjg.food', string="Food")
    diets = fields.Many2many ('g2modulojjg.diet', string="Diet")    
    
    @api.constrains('createDate')
    def _verify_date(self):
        for r in self:
            if fields.Date.from_string(r.createDate) > fields.Date.from_string(fields.Date.today()):
                raise exceptions.ValidationError("Date cannot be greater than today one")
                 
    @api.onchange('idRecipe')
    def _verify_id(self):
        if len(str(self.idRecipe)) > 10:
            return {
        'warning':{
            'title': "id error",
            'message': "maximun character length is 10"
        }
        }
        
    @api.onchange('name')
    def _verify_name(self):
        if len(str(self.name)) > 30:
            return{
                'warning': {
                    'title':"Incorrect 'name' value",
                    'message': "The name must have 30 characters or less",
                },
            }
    
 