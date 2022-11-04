from django.db import models

# Create your models here.
# Data Models
from enum import IntEnum


class User(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    subscription = models.CharField(max_length=30)


class Group(models.Model):
    # id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=140)


class GroupDetail(models.Model):
    # id = models.IntegerField(primary_key=True, auto_created=True)
    groupId = models.ForeignKey(Group, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
