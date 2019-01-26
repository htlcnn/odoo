# test
from openerp import models, fields, api

class DietFacts_product_template(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    calories = fields.Integer('Calories')
    serving_size = fields.Float('Serving Size')
    last_updated = fields.Date('Last Updated')
    diet_item = fields.Boolean('Diet item')
    nutrient_ids = fields.One2many('product.template.nutrient', 'product_id', 'Nutrients')


class DietFacts_res_users_meal(models.Model):

    @api.one
    @api.depends('item_ids', 'item_ids.servings')
    def _calccalories(self):
        current_calories = 0
        for item in self.item_ids:
            current_calories += item.calories * item.servings
        self.total_calories = current_calories

    _name = 'res.users.meal'
    name = fields.Char('Meal Name')
    meal_date = fields.Datetime('Meal Date')
    item_ids = fields.One2many('res.users.mealitem', 'meal_id')
    user_id = fields.Many2one('res.users', 'Meal User')
    total_calories = fields.Integer(string='Total Calories', store=True, compute='_calccalories')
    notes = fields.Text('Meal Notes')


class DietFacts_res_users_mealitem(models.Model):
    _name = 'res.users.mealitem'
    meal_id = fields.Many2one('res.users.meal')
    item_id = fields.Many2one('product.template', 'Meal Item')
    servings = fields.Float('Servings')
    calories = fields.Integer(related='item_id.calories', string='Calories per serving', store=True, readonly=True)
    notes = fields.Text('Meal item notes')


class DietFacts_product_nitrient(models.Model):
    _name = 'product.nutrient'
    name = fields.Char('Nutrient Name')
    uom_id = fields.Many2one('product.uom', 'Unit of Measure')
    description = fields.Text('Description')


class DietFacts_product_template_nutrient(models.Model):
    _name = 'product.template.nutrient'
    nutrient_id = fields.Many2one('product.nutrient', string='Product Nutrient')
    product_id = fields.Many2one('product.template')
    value = fields.Float('Nutrient value')
    daily_percent = fields.Float('Daily Recommended Value')

