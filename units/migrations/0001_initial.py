# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('order', models.IntegerField(default=0)),
                ('item_type', models.CharField(choices=[('KA', 'Key Activities'), ('KP', 'Key Partners'), ('KR', 'Key Resources'), ('C$', 'Cost Strusture'), ('CR', 'Customer Relationships'), ('CS', 'Customer Segment'), ('VP', 'Value Proposition'), ('CH', 'Channels'), ('R$', 'Revenue Streams')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='unit',
            field=models.ForeignKey(to='units.Unit'),
        ),
    ]
