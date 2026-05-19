/** @odoo-module **/

import { registry } from '@web/core/registry';
import { useService } from '@web/core/utils/hooks';
import { Component, onMounted, useRef, useState, xml } from '@odoo/owl';

class LmsWidget extends Component {
    static template = xml`
        <div class="o_action brusnika-lms-container" style="height:100%;display:flex;flex-direction:column;">
            <t t-if="state.loading">
                <div style="display:flex;align-items:center;justify-content:center;height:100%;">
                    <i class="fa fa-spinner fa-spin fa-2x text-muted"/>
                </div>
            </t>
            <t t-elif="state.error">
                <div class="alert alert-warning m-4" style="max-width:600px;">
                    <i class="fa fa-exclamation-triangle me-2"/>
                    <t t-esc="state.error"/>
                </div>
            </t>
            <t t-elif="state.url">
                <iframe
                    t-ref="lmsIframe"
                    t-att-src="state.url"
                    style="flex:1;border:none;width:100%;min-height:600px;"
                    allow="fullscreen"
                />
            </t>
        </div>
    `;

    setup() {
        this.rpc    = useService('rpc');
        this.iframe = useRef('lmsIframe');
        this.state  = useState({ url: '', error: '', loading: true });

        onMounted(async () => {
            try {
                const result = await this.rpc('/brusnika_lms/url');
                if (result.error === 'lms_not_configured') {
                    this.state.error   = 'Brusnika LMS is not configured. Go to Learning → Settings to add the URL and shared secret.';
                    this.state.loading = false;
                } else if (result.url) {
                    this.state.url     = result.url;
                    this.state.loading = false;
                }
            } catch (e) {
                this.state.error   = 'Failed to load LMS. Please try again.';
                this.state.loading = false;
            }
        });
    }
}

registry.category('actions').add('brusnika_lms.LmsWidget', LmsWidget);
