# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('balance', models.BigIntegerField()),
                ('initial_balance', models.BigIntegerField(default=10000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StocksOwned',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('ticker', models.CharField(max_length=5)),
                ('date', models.DateField()),
                ('price', models.IntegerField()),
                ('portfolio', models.ForeignKey(to='game.Portfolio')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
