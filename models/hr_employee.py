# Copyright 2019 ForgeFlow S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, _, exceptions, fields
import logging
from geopy.distance import geodesic

logger = logging.getLogger(__name__)


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    require_location = fields.Boolean(
        string="GPS Location is Mandatory ?", default=False)
    geofence = fields.Many2one("hr.geofence", "Geofence")
    geofence_ids = fields.Many2many("hr.geofence", string="Active Geofences")

    def attendance_manual(self, next_action, entered_pin=False, location=False):
        need_gps = self.env['hr.employee'].search(
            [('user_id', '=', self.env.user.id)]).require_location

        fences = self.env['hr.employee'].search(
            [('user_id', '=', self.env.user.id)]).geofence_ids

        logger.error(
            '------------------------------------------------------------------')

        if location == [0, 0] and need_gps:
            return {'warning': _(f"You\'ve to enable gps location in your browser. Please permit the gps location request when it prompts, or do it manually from the appropriate settings.")}

        if len(list(fences)) > 0 and need_gps and location != [0, 0]:
            logger.error(f'Fences: {len(fences)} --- {len(list(fences))}')
            current_loc = (location[0], location[1])
            for fence in fences:
                fence_loc = (fence.latitude, fence.longitude)
                logger.error(
                    f'Locations: {str(current_loc)} --- {str(fence_loc)}')
                distance = geodesic(current_loc, fence_loc).meters
                if distance > fence.radius:
                    return {'warning': _(f"You're {round(distance/1000, 2)} kilometer/s away from your designated working area, please try again when you are at your working location.")}

        res = super(
            HrEmployee, self.with_context(attendance_location=location)
        ).attendance_manual(next_action, entered_pin)
        logger.error(
            '------------------------------------------------------------------')
        return res

    # def attendance_manual(self, next_action, entered_pin=False, location=False):
    #     res = super(
    #         HrEmployee, self.with_context(attendance_location=location)
    #     ).attendance_manual(next_action, entered_pin)
    #     return res

    def _attendance_action_change(self):
        res = super()._attendance_action_change()
        location = self.env.context.get("attendance_location", False)
        if location:
            if self.attendance_state == "checked_in":
                res.write(
                    {
                        "check_in_latitude": location[0],
                        "check_in_longitude": location[1],
                        "check_in_url": f"https://www.google.com/maps/search/?api=1&query={location[0]},{location[1]}"
                    }
                )
            else:
                res.write(
                    {
                        "check_out_latitude": location[0],
                        "check_out_longitude": location[1],
                        "check_out_url": f"https://www.google.com/maps/search/?api=1&query={location[0]},{location[1]}"
                    }
                )
        return res
