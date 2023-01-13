# -*- coding: utf-8 -*-

from odoo import models, fields

class user(models.model):
    _name = 'res.users'
    _inherit = 'res.users'
    
    #dni = fields.Char()
    #last_name = fields.Char()
    #accesName = fields.Char()
    #birth_date = fields.Char()
    
    #height = fields.Float()
    #weight = fields.Float()
    #genre = fields.Char()
    #imc = fields.Float()
    #physical_condition = fields.Selection()
    
    #isClient = fields.Boolean()
    #isDietist = fields.Boolean()
    #isAdministrator = fields.Boolean
    
    #dietist_food= fields.One2many('g2modulojjg.food', 'idFood', string= 'Dietits_food')
    #dietist_diest= fields.One2many('g2modulojjg.diet', 'idDiet', string= 'Dietits_diest')
    #dietist_recipe= fields.One2many('g2modulojjg.recipe', 'idRecipe', string='Dietits_recipe')
    #client_diets=fields.Many2many('g2modulojjg.diet', 'idDiet', string= 'Client_diets')
    #clients_clients= fields.Oney2many('res.users',ondelete='set null',string='Client_client', required=True)
    #dietist_dietist= fields.Many2one('res.users',ondelete='set null',string='Dietist_dietist', required=True)
