from odoo import models, fields, api


class Sach(models.Model):
    _name = 'model.sach'
    _rec_name = 'ten_sach'

    ten_sach = fields.Char(string='Tên sách')
    tac_gia = fields.Char(string='Tác giả')
    anh = fields.Binary(string='Ảnh')
    so_trang = fields.Integer(string='Số trang')
    the_loai = fields.Many2many(comodel_name='model.theloai', inverse_name='ten_sach', string='Thể loại')
    mo_ta = fields.Text(string='Mô tả')
    anh_sach = fields.Binary(string='Ảnh sách')



