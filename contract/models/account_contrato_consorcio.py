from odoo import fields, api, models
from odoo.exceptions import ValidationError


class ContratoConsorcio(models.Model):
    _name = 'contract.contrato_consorcio'
    _description = 'Contrato Consorcio'

    name = fields.Char(string="Código")
    cd_descricao = fields.Text()
    cd_ativo = fields.Boolean(default=False)

    contratos = fields.One2many('contract.contrato_consorcio_linha', 'contrato_id', string='Contratos')

class ContratoConsorcioLinha(models.Model):
    _name = 'contract.contrato_consorcio_linha'
    _description = 'Contrato Consorcio Linha'

    name = fields.Many2one('res.partner', string="Fornecedores")
    cd_contato = fields.Char(related='cd_fornecedores.mobile', string="Contato")
    cd_email = fields.Char(related='cd_fornecedores.email', string="Email")
    cd_telefone = fields.Char(related='cd_fornecedores.phone', string="Telefone")
    cd_participacao = fields.Integer(string="Participação")
    cd_ativo = fields.Boolean(default=False)

    contrato_id = fields.Many2one('contract.contrato_consorcio', string="Contrato")

    @api.constrains('cd_ativo')
    def verificar_porcentagem(self):
        if self.cd_ativo < 0 or self.cd_ativo > 100:
            raise ValidationError("Campo participação deve ser maior que 0 e menor que 100!")