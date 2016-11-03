# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-03 05:41
from __future__ import unicode_literals

import django.db.models.deletion
import estimators
import estimators.models.evaluations
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('object_hash', models.CharField(
                    default=None, editable=False, max_length=64, unique=True)),
                ('object_file', models.FileField(
                    blank=True, default=None, editable=False, upload_to=estimators.get_upload_path)),
                ('description', models.CharField(
                    max_length=256)),
            ],
            options={
                'db_table': 'data_sets',
            },
        ),
        migrations.CreateModel(
            name='Estimator',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('object_hash', models.CharField(
                    default=None, editable=False, max_length=64, unique=True)),
                ('object_file', models.FileField(
                    blank=True, default=None, editable=False, upload_to=estimators.get_upload_path)),
                ('description', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'estimators',
            },
        ),
        migrations.CreateModel(
            name='EvaluationResult',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('_X_test_proxy', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, related_name='X_test', to='estimators.DataSet')),
                ('_estimator_proxy', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='estimators.Estimator')),
                ('_y_predicted_proxy', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.CASCADE,
                    related_name='y_predicted', to='estimators.DataSet')),
                ('_y_test_proxy', models.ForeignKey(
                    blank=True, on_delete=django.db.models.deletion.CASCADE,
                    related_name='y_test', to='estimators.DataSet')),
            ],
            options={
                'db_table': 'evaluation_results',
            },
            bases=(estimators.models.evaluations.EvaluationMixin, models.Model),
        ),
    ]
