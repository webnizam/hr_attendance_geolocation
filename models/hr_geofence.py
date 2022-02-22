# Copyright 2019 ForgeFlow S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from cmath import log
from odoo import models, _, exceptions, fields, api
import logging
import json
import re

logger = logging.getLogger(__name__)


class GeoFence(models.Model):
    _name = "hr.geofence"
    _description = "Geofence"

    name = fields.Char(string='Geofence Name', required=True)
    latitude = fields.Char(string='Latitude', required=True)
    longitude = fields.Char(string='Longitude', required=True)
    cordinates = fields.Char(string='Cordinates')
    radius = fields.Float(
        default=500, string="Geofence Radius in Meters", required=True)
    active = fields.Boolean(string='Active', default=True)
