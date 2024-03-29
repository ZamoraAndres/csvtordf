# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import csvtottl.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(storage=csvtottl.models.OverwriteStorage(), upload_to=csvtottl.models.Document.doc_filename)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
