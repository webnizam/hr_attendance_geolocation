# Copyright 2019 ForgeFlow S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Hr Attendance Geolocation",
    'sequence': -1000,
    "summary": """
        With this module the geolocation of the user is tracked at the
        check-in/check-out step""",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "FDT",
    "website": "https://fdtech.ae",
    "depends": ["hr_attendance", "hr"],
    "data": [
        "views/assets.xml",
        "security/ir.model.access.csv",
        "views/hr_attendance_views.xml",
        "data/location_data.xml",
        'views/hr_employee.xml',
        'views/hr_geofence.xml',
    ],
}
