# Generated by Django 2.0 on 2018-01-03 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20180101_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
