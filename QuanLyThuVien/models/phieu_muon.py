from odoo import models, fields, api
from odoo import _
from odoo.exceptions import ValidationError
from datetime import datetime


class PhieuMuon(models.Model):
    _name = 'model.phieumuon'
    _rec_name = 'ma_phieu_muon'

    ma_phieu_muon = fields.Char(string='Mã phiếu mượn', copy=False,
                                default= lambda self: _('Tạo phiếu mượn'))
    ten_kh = fields.Char(string='Tên khách hàng:')
    sdt = fields.Char(string='Số điện thoại:')
    dia_chi = fields.Text(string='Địa chỉ:')
    danhsach_sach = fields.Many2many(comodel_name='model.sach')
    ngay_muon = fields.Date(string='Ngày mượn sách:', default=datetime.today())
    ngay_tra = fields.Date(string='Ngày trả sách:')
    so_ngay_muon = fields.Integer(string='Số ngày mượn', compute='tinh_ngay_muon')
    tong_tien = fields.Integer(string='Tổng tiền', compute='tinh_tong_tien')

    @api.model
    def create(self, vals):
        if vals.get('ma_phieu_muon', 'Tạo phiếu mượn') == 'Tạo phiếu mượn':
            vals['ma_phieu_muon'] = self.env['ir.sequence'].next_by_code('model.phieumuon.sequence') or 'Tạo phiếu mượn'
        result = super(PhieuMuon, self).create(vals)
        return result

    @api.depends('ngay_muon', 'ngay_tra')
    def tinh_ngay_muon(self):
        self.so_ngay_muon = abs((self.ngay_tra-self.ngay_muon).days)

    @api.depends('ngay_muon', 'ngay_tra', 'danhsach_sach')
    def tinh_tong_tien(self):
        self.tong_tien = abs((self.ngay_tra-self.ngay_muon).days) * len(self.danhsach_sach) * 5000


