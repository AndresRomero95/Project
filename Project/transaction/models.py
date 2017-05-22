from django.db import models


class Transactions(models.Model):
    amount = models.BigIntegerField(),
    user_ID_from = models.PositiveIntegerField(),
    user_ID_to = models.PositiveIntegerField(),
    date = models.parse_datetime(),

#TODO @classmethod
#TODO def create_transaction(cls, amount,user_ID_from, user_ID_to,date):
