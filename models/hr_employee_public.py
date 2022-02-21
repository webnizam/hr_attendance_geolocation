# Copyright 2019 ForgeFlow S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, _, exceptions, fields
import logging

log = logging.getLogger(__name__)


class HrEmployee(models.Model):
    _inherit = "hr.employee.public"

    require_location = fields.Boolean(
        string="GPS Location is Mandatory ?", default=False)
    geofence = fields.Many2one("hr.geofence", "Geofence")
