# Generated by Django 4.1.4 on 2023-01-09 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrifolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='texto',
            field=models.FileField(upload_to='', verbose_name='Texto'),
        ),
    ]
