# Generated by Django 2.0 on 2017-12-31 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='article',
            name='featured_image',
            field=models.ImageField(upload_to='upload_images'),
        ),
    ]
