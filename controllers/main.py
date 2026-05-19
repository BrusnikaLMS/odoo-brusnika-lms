import hashlib
import hmac
import time
from urllib.parse import quote

from odoo import http
from odoo.http import request


class BrusnikaLmsController(http.Controller):

    @http.route('/brusnika_lms/url', type='json', auth='user')
    def get_lms_url(self):
        """Return a signed LMS URL for the current employee."""
        env = request.env
        params = env['ir.config_parameter'].sudo()

        lms_url = params.get_param('brusnika_lms.url', '').rstrip('/')
        secret  = params.get_param('brusnika_lms.secret', '')

        if not lms_url:
            return {'error': 'lms_not_configured'}

        user     = env.user
        employee = env['hr.employee'].sudo().search([('user_id', '=', user.id)], limit=1)

        employee_id = str(employee.id) if employee else '0'
        email       = user.email or ''
        name        = user.name or ''
        ts          = str(int(time.time()))

        # HMAC-SHA256 signature: employee_id|email|ts
        payload = f'{employee_id}|{email}|{ts}'
        sig = hmac.new(
            secret.encode('utf-8'),
            payload.encode('utf-8'),
            hashlib.sha256,
        ).hexdigest() if secret else ''

        full_url = (
            f'{lms_url}/index.php'
            f'?odoo=Y'
            f'&employee_id={quote(employee_id)}'
            f'&email={quote(email)}'
            f'&name={quote(name)}'
            f'&ts={ts}'
            f'&sig={sig}'
            f'#/'
        )

        return {'url': full_url, 'configured': True}
