from odoo import models, fields

class BlogPost(models.Model):
    _inherit = 'blog.post'

    no_index = fields.Boolean(
        string="Disallow indexing",
        help="If enabled, search engines will not index this blog post."
    )

