# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0008_auto_20151028_1152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alias',
            old_name='address',
            new_name='name',
        ),
        migrations.AlterUniqueTogether(
            name='alias',
            unique_together=set([('domain', 'name')]),
        ),
    ]