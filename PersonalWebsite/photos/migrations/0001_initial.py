# Generated by Django 2.0 on 2018-01-11 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='my_photos')),
                ('alt', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('published_on', models.DateField(auto_now_add=True)),
            ],
        ),
    ]