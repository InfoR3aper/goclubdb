# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-30 15:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, verbose_name=b'A uniquely defining name for the club')),
                ('meettime', models.TextField(blank=True, null=True, verbose_name=b'Meeting times of the club (as text for now)')),
                ('meetplace', models.TextField(blank=True, null=True, verbose_name=b'Meeting place of the club (as text address)')),
                ('postcode', models.CharField(blank=True, max_length=32, null=True, verbose_name=b'Postal code')),
                ('contact', models.TextField(blank=True, null=True, verbose_name=b'Contact details (free-form text)')),
                ('website', models.URLField(blank=True, null=True, verbose_name=b'Website of the club, if any')),
                ('lat', models.FloatField(verbose_name=b'Decimal latitude')),
                ('lon', models.FloatField(verbose_name=b'Decimal longitude')),
                ('province', models.CharField(blank=True, max_length=52, null=True, verbose_name=b'Province or state')),
            ],
        ),
        migrations.CreateModel(
            name='Clubstatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name=b'What we call the status (e.g. "active")')),
                ('description', models.TextField(verbose_name=b'What does this status mean?')),
                ('iconclass', models.CharField(blank=True, max_length=200, null=True, verbose_name=b'What marker shape to use for this status')),
            ],
        ),
        migrations.CreateModel(
            name='Clubtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name=b'What we call the type (e.g. "club" or "individual")')),
                ('description', models.TextField(verbose_name=b'What does this type include')),
                ('iconurl', models.CharField(blank=True, max_length=200, null=True, verbose_name=b'What icon picture to use for this type of club')),
            ],
        ),
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name=b'Layer name, normally ISO 3166-1 country code')),
                ('description', models.TextField(verbose_name=b'Description of the layer')),
                ('website', models.URLField(verbose_name=b'Website of the organisation, if any')),
                ('color', models.CharField(max_length=25, verbose_name=b'Color of the marker; must be a valid HTML color name')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='club',
            name='clubstatus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goclubdb.Clubstatus'),
        ),
        migrations.AddField(
            model_name='club',
            name='clubtype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goclubdb.Clubtype'),
        ),
        migrations.AddField(
            model_name='club',
            name='layer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goclubdb.Layer'),
        ),
    ]
