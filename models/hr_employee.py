# Copyright 2019 ForgeFlow S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, _, exceptions, fields
import logging
from geopy.distance import geodesic

log = logging.getLogger(__name__)


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    require_location = fields.Boolean(
        string="GPS Location is Mandatory ?", default=False)
    geofence = fields.Many2one("hr.geofence", "Geofence")

    # 'You\ve to enable location in your browser. Please permit the location request when it prompts'

    def attendance_manual(self, next_action, entered_pin=False, location=False):
        need_gps = self.env['hr.employee.public'].search(
            [('user_id', '=', self.env.user.id)]).require_location
        # need_gps = self.env.user.require_location
        # need_gps = True
        fence = self.env['hr.employee.public'].search(
            [('user_id', '=', self.env.user.id)]).geofence
        log.error('Need GPS-->', "Test", need_gps)
        if location == [0, 0] and need_gps:

            return {'warning': _(f"You\'ve to enable gps location in your browser. Please permit the gps location request when it prompts.")}
            # raise exceptions.UserError(
            #     _('You\'ve to enable location in your browser. Please permit the location request when it prompts.'))
        if fence and need_gps and location != [0, 0]:
            current_loc = (location[0], location[1])
            fence_loc = (fence.latitude, fence.longitude)
            if geodesic(current_loc, fence_loc).meters > fence.radius:
                return {'warning': _(f"You're not inside the company premises, please try again when you reach company premise.")}

        res = super(
            HrEmployee, self.with_context(attendance_location=location)
        ).attendance_manual(next_action, entered_pin)
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
