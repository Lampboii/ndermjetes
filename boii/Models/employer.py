from odoo import api, fields, models
from odoo import tools, _
from odoo.exceptions import ValidationError, UserError


class Punekerkues(models.Model):
    _name = "employer.punekerkues"
    _description = "Punekerkues"

    _rec_name = 'emri'
    emri = fields.Char(string="Emer", required=True)
    mbiemri = fields.Char(string="Mbiemer", required=True)
    datelindje = fields.Date(string="Ditelindja")
    nr_identifikues = fields.Char(string="Nr. Personal", required=True)
    informacion = fields.Char(string="Informacion")
    nr_aplikime = fields.Integer(string="Numri i aplikimeve")
    historik_id = fields.One2many('employer.historik', 'punekerkues_id', string="")
    aplikim_id = fields.One2many('employer.apliko', 'punekerkues_id', string="Aplikanti")
    pozicion_id = fields.One2many('employer.pozicione', 'aplikim_id')

    @api.constrains('nr_identifikues')
    def _nr_identifikues_length(self):
        if len(self.nr_identifikues) != 10:
            raise ValidationError("Numri personal duhet te jete me 10 karaktere!")

class Punedhenes(models.Model):
    _name = "employer.punedhenes"
    _description = "Punedhenes"

    _rec_name = 'emri'
    emri = fields.Char(string="Emer", required=True)
    NIPT = fields.Char(string="NIPT", required=True)
    nr_vakante = fields.Integer(string="Nr. i vendeve vakante")
    nr_kontakt = fields.Integer(string="Numer kontakti")
    email = fields.Char(string="E-Mail")
    pozicion_id = fields.One2many('employer.pozicione', 'punedhenes_id')
    historik_id = fields.One2many('employer.historik', 'punedhenes_id')



    @api.constrains('NIPT')
    def _nipt_length(self):
        if len(self.NIPT) != 10:
            raise ValidationError("NIPT duhet te jete me 10 karaktere!")

class PozicionePune(models.Model):
    _name = "employer.pozicione"
    _description = "Pozicione Vakante"

    _rec_name = 'titull'
    titull = fields.Char(string="Pozicioni", required=True)
    nr_kerkuar = fields.Integer(string="Numri i kerkimeve")
    informacion = fields.Text(string="Informacion")
    date_fillimi = fields.Date(string="Nga")
    date_mbarimi = fields.Date(string="Deri")
    status = fields.Selection([('Vakant', 'Vakant'), ('I zënë', 'I zënë')], string='Statusi', default='Vakant')
    punedhenes_id = fields.Many2one('employer.punedhenes', string="Punedhenesi")
    aplikim_id = fields.One2many('employer.apliko', 'punekerkues_id', string="Aplikantet")




class HistorikAplikimesh(models.Model):
    _name = "employer.historik"
    _description = "Historiku i aplikimeve"

    aplikim_id = fields.Many2many('employer.apliko')
    punekerkues_id = fields.Many2one('employer.punekerkues', string="Punekerkuesi")
    pozicion_id = fields.Many2one('employer.pozicione', string="Pozicioni")
    punedhenes_id = fields.Many2one('employer.punedhenes', string="Punedhenes")
    date_aplikimi = fields.Integer(string="Data e Aplikimt")

class Aplikim(models.Model):
    _name = "employer.apliko"
    _description = "Apliko"

    pozicion_id = fields.Many2one ('emplyer.pozicione', string="Pozicioni")
    punekerkues_id = fields.Many2one('employer.punekerkues', string="Aplikanti")
    historik_id = fields.Many2many('employer.historik')