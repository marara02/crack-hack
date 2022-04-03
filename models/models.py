# -*- coding: utf-8 -*-

from odoo import models, fields, api


class volunteers(models.Model):
    _name = 'help.volunteers'

    name = fields.Char(string="Название организации")
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High'),
        ('3', 'Up to high'),
        ('4', 'High High'),
        ('5', 'Max High')
    ], default='0', index=True, string="Priority")


class doctors(models.Model):
    _name = 'help.doctors'

    name = fields.Char(string="Имя")
    how_many_patients = fields.Integer(string="Количество пациентов")


class crapt_hack(models.Model):
    _name = 'crapt_hack.crapt_hack'

    name = fields.Char()
    state = fields.Selection([
        ('Обращения', 'Обращения'),
        ('Назначена встреча', 'Назначена встреча'),
        ('Встреча была', 'Встреча была'),
        ('Отправлено на реабилитацию', 'Отправлено на реабилитацию'),
        ('Помогли полностью', 'Помогли полностью')
    ], default="Обращения")
    user_id = fields.Many2one('res.users', string="Запроситель")
    image_1920 = fields.Image(string='Photo')
    age = fields.Integer(string="Возраст")
    email = fields.Char(string="Email")
    tel_number = fields.Char(string="Номер Телефона")
    description = fields.Text(string="Причина обращения")
    doctor_id = fields.Many2one('help.doctors', string="Специалист")
    diagnos = fields.Char(string="Диагноз")
    future_help = fields.Text(string="Процесс реабилитации")

    def send_to_specialist(self):
        for rec in self:
            rec.state = 'Назначена встреча'

    def end_with_specialist(self):
        for rec in self:
            rec.state = 'Встреча была'

    def send_with_specialist(self):
        for rec in self:
            rec.state = 'Отправлено на реабилитацию'

    def finish_with_specialist(self):
        for rec in self:
            rec.state = 'Помогли полностью'
