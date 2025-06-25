# -*- coding: utf-8 -*-

import uuid
from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)

class ExtendSaleOrder(models.Model):
    _inherit = ['sale.order']

    mode_reglement = fields.Selection(
        string='Mode de Règlement',
        selection=[
            ('bank_transfer', 'Virement Bancaire'),
            ('credit_card', 'Carte Bancaire'),
            ('check', 'Chèque'),
            ('cash', 'Espèce'),
        ],
        default='bank_transfer',
    )
    # ---------------------------------------------------- METHODES DE CALCUL DES CHAMPS ----------------------------------------------------
    
    
    # ---------------------------------------------------- METHODES ACTIONS ----------------------------------------------------
