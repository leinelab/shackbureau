# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentmanagement', '0008_auto_20160224_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donationreceipt',
            name='address',
        ),
    ]
