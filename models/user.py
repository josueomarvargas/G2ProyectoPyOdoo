# -*- coding: utf-8 -*-

from odoo import models, fields, api

class user(models.Model):
    _name = 'res.users'
    _inherit = 'res.users'
    
    dni = fields.Char()
    last_name = fields.Char()
    accesName = fields.Char()
    birth_date = fields.Char()    
    height = fields.Float()
    weight = fields.Float()
    genre = fields.Char()
    imc = fields.Float()
    #physical_condition = fields.Selection()
    
    isClient = fields.Boolean()
    isDietist = fields.Boolean()
    isAdministrator = fields.Boolean()
    clients= fields.One2many('res.users','dni',string="Client")
    dietist= fields.Many2one('res.users',ondelete='set null',string="Dietist", index=True)
    dietist_food= fields.One2many('g2modulojjg.food', 'dietist', string= "Food")
    dietist_diest= fields.One2many('g2modulojjg.diet', 'dietits', string= "Diest")
    dietist_recipe= fields.One2many('g2modulojjg.recipe', 'dietist1', string="Recipe")
    client_diets=fields.Many2many('g2modulojjg.diet', string= "Diet")
 
