from odoo import models, fields, api


class Sach(models.Model):
    _name = 'model.tacgia'
    _rec_name = 'ho_ten'

    anh = fields.Binary(string='Ảnh')
    ho_ten = fields.Char(string='Họ tên:')
    ngay_sinh = fields.Char(string='Ngày sinh')
    tac_pham = fields.Many2many(comodel_name='model.sach')
    mo_ta = fields.Text(string='Mô tả')




