# -*- coding: utf-8 -*-

from odoo import models, fields, api


class odootycoon_producttemplate(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'
    unlockcost = fields.Float('Unlock Cost', default=750)
    unlocked = fields.Boolean('Unlocked', default=False)


class odootycoon_gamemanager(models.Model):
    _name = 'odootycoon.gamemanager'
    name = fields.Char('Game Name', default='New Game')
    day = fields.Integer('Current Day', default=1)
    cash = fields.Float('Cash', default=500)

    def nextday(self):
        self.write({
            'day': self.day + 1,
            'cash': self.day - 100
            })

    def skip5days(self):
        for i in range(5):
            self.nextday()
