from django.db import models
from enum import IntEnum

from django.apps import apps

#from splitwiseProject import user_group

#MyModel1 = apps.get_model('user_group', 'User')


# Create your models here.

class Transaction(models.Model):
    #id = models.IntegerField(primary_key=True, auto_created=True)
    owner = models.ForeignKey('user_group.User', on_delete=models.CASCADE)
    amount = models.FloatField()


class ShareTypes(IntEnum):
    PERCENT = 1
    ABSOLUTE = 2

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class TransactionDetail(models.Model):
    #id = models.IntegerField(primary_key=True, auto_created=True)
    transactionID = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    user = models.ForeignKey('user_group.User', on_delete=models.DO_NOTHING)
    shareType = models.IntegerField(choices=ShareTypes.choices(), default=1)
    shareValue = models.FloatField()
