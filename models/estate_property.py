from odoo import models , fields,api
from odoo.exceptions import ValidationError,UserError

class EstateProperty(models.Model):
    """Model definition for EstateProperty."""
    _name = "estate.property"
    _description = "Estate Property"
    _order = "date_availability desc"
    _sql_constraints = [
        
        (
            'unique_name',
            'UNIQUE(name)',
            'Le nom doit etre unique'
        ),
         (
            'check_percentage',
            'CHECK(facades >= 0 AND facades <= 100)',
            'Ce nombre doit etre compris entre 0 et 100'
        )
    ]
    
    @api.constrains('selling_price')
    def _check_selling_price(self):
        for record in self:
            if record.selling_price < 1:
                raise ValidationError(('Le Prix de Vente dois être superieur à 0'))
            
    @api.depends('living_area','garden_area')
    def _compute_total_area(self):
        for prop in self:
            prop.total_area = prop.living_area + prop.garden_area
            
    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation= "N"
        else:
            self.garden_area = 0
            self.garden_orientation = False 
                
    
    name  = fields.Char(required=True)
    description =  fields.Text(default="Description de la Propriete")
    postcode = fields.Char()
    date_availability = fields.Date(default=fields.Datetime.now)
    expected_price = fields.Float()
    selling_price = fields.Float(default=1000000)
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        [("N","North"),("S","South"),("E","East"),("W","West")], string='Garden Orientation'
        )
    user_id = fields.Many2one("res.users", string="Salesman", default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", string="Buyer", readonly=True, copy=False)
    last_seen = fields.Datetime('Last Seen',default=fields.Datetime.now)
    total_area = fields.Integer(readonly=True, compute="_compute_total_area")
    state = fields.Selection(
        selection=[
            ("new","new"),
            ("offer_received","Offer Received"),
            ("offer_accepted","Offer Accepted"),
            ("sold","Sold"),
            ("canceled","Canceled"),
            
        ],
        string="Status",
        required=True,
        copy=False,
        default="new"
    )
    # TODO: Define fields here
    
    def action_sold(self):
        if "canceled" in self.mapped("state"):
            raise UserError("Canceled Properties Canoot Be Sold")
        return self.write({"state":"sold"})
    
    def action_cancel(self):
        if "sold" in self.mapped("state"):
            raise UserError("Sold Properties Canoot Be Sold")
        return self.write({"state":"canceled"})

    