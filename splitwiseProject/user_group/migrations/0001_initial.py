# Generated by Django 4.1 on 2022-11-03 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Groups",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("description", models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=30)),
                ("subscription", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="GroupDetails",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                (
                    "groupId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user_group.groups",
                    ),
                ),
                (
                    "userId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user_group.user",
                    ),
                ),
            ],
        ),
    ]