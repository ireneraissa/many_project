# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 20:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.IntegerField(max_length=100)),
                ('numero_ligne', models.IntegerField(max_length=5)),
                ('nombre_place', models.IntegerField(max_length=200)),
                ('id_device', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='chauffeur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_chauffeur', models.TextField()),
                ('prenom_chauffeur', models.TextField()),
                ('telephone_chauffeur', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='bus',
            name='info_chauffeur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus_project.chauffeur'),
        ),
    ]
