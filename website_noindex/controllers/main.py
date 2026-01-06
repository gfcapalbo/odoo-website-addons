# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class WebsiteNoindex(http.Controller):

    @http.route('/website/index_noindex', type='json', auth="public", website=True)
    def index_noindex(self, index):
        if index == 'index':
            request.website.write({'no_index': False})
        else:
            request.website.write({'no_index': True})
        return True

