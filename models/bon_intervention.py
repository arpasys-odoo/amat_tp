# -*- coding: utf-8 -*-

import uuid
from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)

class BonIntervention(models.Model):
    _name = 'bon_intervention.bon_intervention'
    _description = "bon intervention"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string="Référence", copy=False, readonly=True)
    lieu_intervention = fields.Char(string="Lieu de l'intervention", required=True)
    company_id = fields.Many2one(
        comodel_name='res.company', required=True, index=True, default=lambda self: self.env.company)
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string="Client",
        required=True, change_default=True, index=True,
        tracking=1,
        readonly=False,
        domain="[('company_id', 'in', (False, company_id))]")
    user_id = fields.Many2one(comodel_name='res.users', string="Vendeur", store=True, readonly=False, index=True, tracking=2,
                            domain=lambda self: "[('groups_id', '=', {}), ('share', '=', False), ('company_ids', '=', company_id)]".format(
                            self.env.ref(
                            "amat_tp.amat_tp_group_user").id
                            ))
    date_order = fields.Date(string="Date de création", required=True, copy=False, default=fields.Date.today)
    
    type_machine = fields.Char(string="Type de machine", required=True)
    num_serie = fields.Char(string="N° de série", required=True)
    heures = fields.Float(string="Heures", required=True)
    date_panne = fields.Date(string="Date de la panne", required=True)
    date_fin_reparation = fields.Date(string="Date de fin de réparation", required=True)
    detail_panne_intervention = fields.Text(string="Détail de la panne et intervention effectuée", required=True)
    fourniture = fields.Text(string="Fourniture")
    total_heure = fields.Float(string="Nombre d'heures de main d\'œuvre TOTAL", required=True)
    

    # ---------------------------------------------------- METHODES DE CALCUL DES CHAMPS ----------------------------------------------------
    
    # à ajouter dans séquence pour numéroter les bons d'interventions
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name'):
                vals['name'] = self.env['ir.sequence'].next_by_code(
                    'bon_intervention.bon_intervention') or '/'
        return super(BonIntervention, self).create(vals_list)
    
    @api.model
    def get_hours_minutes(self, float_time):
        hours = int(float_time)
        minutes = int(round((float_time - hours) * 60))
        return "{:02d}:{:02d}".format(hours, minutes)
    # ---------------------------------------------------- METHODES ACTIONS ----------------------------------------------------
