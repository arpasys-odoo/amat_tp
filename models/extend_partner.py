# -*- coding: utf-8 -*-

import uuid
from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)

class ExtendSaleOrder(models.Model):
    _inherit = ['res.partner']
    
    tva_intracom = fields.Char(string="N° de TVA Intracom")
    code_client = fields.Char(string="Code client")
    

    # ---------------------------------------------------- METHODES DE CALCUL DES CHAMPS ----------------------------------------------------
    
    
    # ---------------------------------------------------- METHODES ACTIONS ----------------------------------------------------
