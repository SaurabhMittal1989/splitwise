# Generated by Django 4.1 on 2022-11-03 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user_group", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(old_name="Groups", new_name="Group",),
        migrations.RenameModel(old_name="GroupDetails", new_name="GroupDetail",),
    ]
