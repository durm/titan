# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_type',
            field=models.CharField(max_length=3, choices=[('KA', 'Key Activities'), ('KP', 'Key Partners'), ('KR', 'Key Resources'), ('CSt', 'Cost Strusture'), ('CR', 'Customer Relationships'), ('CSg', 'Customer Segments'), ('VP', 'Value Propositions'), ('CH', 'Channels'), ('RSt', 'Revenue Streams')]),
        ),
    ]
