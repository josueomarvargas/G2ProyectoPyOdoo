# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models
from odoo import api
from odoo import exceptions

class diet(models.Model):
    _name = 'g2modulojjg.diet'
    name = fields.Char()
    idDiet = fields.Char(required=True)
    timeDiet = fields.Integer()
    objectiveDiet = fields.Date()
    #dietType = fields.Selection([('OMNIVORO'),('VEGANA'),('VEGETARIANO')],string="Tipo Dieta")
    recipes = fields.Many2many('g2modulojjg.recipe', string="Recipe")
    clients = fields.Many2many('res.users', string="Clients")
    dietits = fields.Many2one('res.users', ondelete='cascade', string="Dietist", required=True)
    
    @api.onchange('timeDiet')
    def _verify_valid_time(self):
        if self.timeDiet < 0:
            return{
                'warning': {
                    'title':"Incorrect 'tiemDiet' value",
                    'message': "The number must be positive",
                },
            }
    
    @api.constrains('timeDiet')
    def _validate_timeDiet(self):
        for task in self:
            if self.timeDiet < 0:
                raise exceptions.ValidationError("Time cannot be a negative number")                
                
    @api.constrains('objectiveDiet')
    def _validate_objectiveDiet(self):
        for r in self:
            if fields.Date.from_string(r.objectiveDiet) <= fields.Date.from_string(fields.Date.today()):
                raise exceptions.ValidationError("Date cannot be today's date or less")
    
    @api.onchange('name')
    def _verify_valid_name(self):
        if len(str(self.name)) > 30:
            return{
                'warning': {
                    'title':"Incorrect 'name' value",
                    'message': "The name must have 30 characters or less",
                },
            }