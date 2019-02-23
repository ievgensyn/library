from odoo import models, fields, api


# from odoo import decimal_precision as dp


class LabraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    _order = 'date_release desc, name'
    # _rec_name = 'short_name'

    name = fields.Char('Title', required=True)
    # short_name = fields.Char(string='Short Title',
    #                          size=100, required=True)
    _sql_constraints = [
        ('name_uniq',
         'UNIQUE (name)',
         'Book title must be unique.')
    ]
    notes = fields.Text(string='Internal Notes')
    state = fields.Selection(
        [('draft', 'Not Available'),
         ('available', 'Available'),
         ('lost', 'Lost')],
        string='State'
    )
    description = fields.Html(string='Description')
    cover = fields.Binary(string='Book Cover')
    out_of_print = fields.Boolean(string='Out of Print')
    date_release = fields.Date(string='Release Date')
    date_updated = fields.Datetime(string='Last Updated')
    cost_price = fields.Float(string='Book Cost')
    pages = fields.Integer(
        string='Number of Pages', default=0,
        groups='base.group_user',
        states={'lost': [('readonly', True)]}
    )
    reader_rating = fields.Float(
        string='Reader Average Rating',
        digits=(14, 4),
    )
    author_ids = fields.Many2many(
        comodel_name='res.partner',
        string='Authors'
    )
    currency_id = fields.Many2one(
        comodel_name='res.currency', string='Currency'
    )
    retail_price = fields.Monetary(string='Retail Price')
    publisher_id = fields.Many2one(
        comodel_name='res.partner', string='Publisher'
    )

    @api.constrains('date_release')
    def _check_release_date(self):
        for rec in self:
            if (rec.date_release and
                    rec.date_release > fields.Date.today()):
                raise models.ValidationError(
                    'Release must be in the past.'
                )


class ResPartner(models.Model):
    _inherit = 'res.partner'

    published_book_ids = fields.One2many(
        comodel_name='library.book',
        inverse_name='publisher_id',
        striing='Published Books'
    )
    authored_book_ids = fields.Many2many(
        comodel_name='library.book',
        string='Authored Books',
        relation='library_book_res_partner_rel'
    )
