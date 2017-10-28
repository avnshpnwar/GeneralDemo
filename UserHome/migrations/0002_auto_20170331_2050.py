# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-31 15:20
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UserHome', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_account',
            name='account_name',
            field=models.CharField(default='aa', max_length=20, validators=[django.core.validators.MinLengthValidator(4, message='Length has to be 4')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payee_account',
            name='account_no',
            field=models.PositiveIntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='user_account',
            name='account_no',
            field=models.PositiveIntegerField(db_index=True),
        ),
        migrations.AlterUniqueTogether(
            name='payee_account',
            unique_together=set([('user', 'payee_name', 'account_no')]),
        ),
        migrations.AlterUniqueTogether(
            name='user_account',
            unique_together=set([('user', 'account_no', 'account_name')]),
        ),
    ]