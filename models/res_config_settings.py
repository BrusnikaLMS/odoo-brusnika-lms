from odoo import api, fields, models


class BrusnikaLmsSettings(models.TransientModel):
    _name = 'brusnika.lms.settings'
    _description = 'Brusnika LMS Settings'

    lms_url = fields.Char(
        string='LMS URL',
        help='Base URL of your Brusnika LMS instance, e.g. https://lms.example.com',
    )
    lms_secret = fields.Char(
        string='Shared Secret',
        help='Secret key used to sign SSO tokens. Must match the value set in Brusnika LMS.',
    )

    def execute(self):
        params = self.env['ir.config_parameter'].sudo()
        params.set_param('brusnika_lms.url', self.lms_url or '')
        params.set_param('brusnika_lms.secret', self.lms_secret or '')
        return {'type': 'ir.actions.act_window_close'}

    @api.model
    def get_default_values(self):
        params = self.env['ir.config_parameter'].sudo()
        return {
            'lms_url':    params.get_param('brusnika_lms.url', ''),
            'lms_secret': params.get_param('brusnika_lms.secret', ''),
        }

    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        params = self.env['ir.config_parameter'].sudo()
        res['lms_url']    = params.get_param('brusnika_lms.url', '')
        res['lms_secret'] = params.get_param('brusnika_lms.secret', '')
        return res
