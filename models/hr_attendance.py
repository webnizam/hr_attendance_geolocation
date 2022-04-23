# Copyright 2019 ForgeFlow S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class HrAttendance(models.Model):
    _inherit = "hr.attendance"

    check_in_latitude = fields.Float(
        "Check-in Latitude", digits="Location", readonly=True
    )
    check_in_longitude = fields.Float(
        "Check-in Longitude", digits="Location", readonly=True
    )
    check_out_latitude = fields.Float(
        "Check-out Latitude", digits="Location", readonly=True
    )
    check_out_longitude = fields.Float(
        "Check-out Longitude", digits="Location", readonly=True
    )
    check_in_url = fields.Char(string='Check in URL')
    check_out_url = fields.Char(string='Check out URL')

    check_in_ip = fields.Char(string='Check in Ip')
    check_out_ip = fields.Char(string='Check out Ip')

    check_in_useragent = fields.Char(string='Check in Useragent')
    check_out_useragent = fields.Char(string='Check out Useragent')
