# Generated by Django 3.2.4 on 2022-05-04 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazines',
            name='mfile',
            field=models.FileField(default='', upload_to='static/magazines'),
        ),
    ]
