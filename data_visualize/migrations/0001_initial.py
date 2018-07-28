# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bubble',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.CharField(max_length=100)),
                ('coin', models.CharField(max_length=50)),
                ('open', models.FloatField()),
                ('market_cap', models.FloatField()),
                ('volume', models.FloatField()),
            ],
        ),
    ]
