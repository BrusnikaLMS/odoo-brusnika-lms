{
    'name': 'Brusnika LMS',
    'version': '17.0.1.0.0',
    'category': 'eLearning',
    'summary': 'Embed Brusnika LMS inside Odoo with single sign-on for employees.',
    'description': """
Brusnika LMS Integration
========================
Embed Brusnika LMS directly inside Odoo with single sign-on for employees.

Features:
- One-click access to LMS from Odoo menu (no separate login)
- Employees authenticated automatically via their Odoo identity
- Configure LMS URL and shared secret in Brusnika LMS Settings
    """,
    'author': 'Brusnika Solutions',
    'website': 'https://brusnika-lms.com',
    'license': 'LGPL-3',
    'depends': ['base', 'hr', 'mail', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_config_settings_views.xml',
        'views/lms_views.xml',
        'views/lms_menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'brusnika_lms/static/src/js/lms_widget.js',
        ],
    },
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 0,
    'currency': 'EUR',
}
