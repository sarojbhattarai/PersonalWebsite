# Generated by Django 2.0 on 2018-02-24 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='work_url',
            field=models.URLField(default=2),
            preserve_default=False,
        ),
    ]
