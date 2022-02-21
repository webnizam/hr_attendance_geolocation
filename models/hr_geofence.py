# Copyright 2019 ForgeFlow S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, _, exceptions, fields
import logging

log = logging.getLogger(__name__)


class GeoFence(models.Model):
    _name = "hr.geofence"
    _description = "Geofence"

    name = fields.Char(string='Genofence Name', required=True)
    latitude = fields.Char(string='Latitude', required=True)
    longitude = fields.Char(string='Longitude', required=True)
    radius = fields.Integer(
        default=500, string="Geofence Radius in Meters", required=True)
    active = fields.Boolean(string='Active', default=True)
