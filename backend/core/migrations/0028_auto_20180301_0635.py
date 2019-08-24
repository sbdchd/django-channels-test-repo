# Generated by Django 2.0.2 on 2018-03-01 06:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("core", "0027_myuser_membership")]

    operations = [
        migrations.AlterField(
            model_name="myuser",
            name="membership",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="membership",
                to="core.Membership",
            ),
        )
    ]
