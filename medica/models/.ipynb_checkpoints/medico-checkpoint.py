# -*- coding: utf-8 -*

from odoo import models, fields, api

class Medica(models.Model):
    
    _name = 'medica.medico'
    _description = 'Datos de medicos'
    
    name = fields.Char(string='Title',required=True)
    description = fields.Text(string='Description')
    telefono = fields.Text(string='Description')
    level = fields.Selection(string='Level',
                            selection=[('beginner','Beginner'),
                                      ('intermediate','Intermediate'),
                                      ('advanced','Advanced')],
                            copy=False)
    
    active = fields.Boolean(string='Active', default=True)
