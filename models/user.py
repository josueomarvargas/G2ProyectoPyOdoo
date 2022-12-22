# -*- coding: utf-8 -*-

from odoo import models, fields

class user(models.model):
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
    physical_condition = fields.Selection()
    
    isClient = fields.Boolean()
    isDietist = fields.Boolean()
    isAdministrator = fields.Boolean
    
    dietist_food= fields.One2many('g2modulojjg.food', 'idFood', string= 'Food')
    dietist_diest= fields.One2many('g2modulojjg.diet', 'idDiet', string= 'Diest')
    dietist_recipe= fields.One2many('g2modulojjg.recipe', 'idRecipe', string='Recipe')
    client_diets=fields.Many2many('g2modulojjg.diet', 'idDiet', string= 'Diet')
    clients_clients= fields.Oney2many('res.users',ondelete='set null',string='Client', required=True)
    dietist_dietist= fields.Many2one('res.users',ondelete='set null',string='Dietist', required=True)
