# Generated by Django 3.2.4 on 2021-07-11 00:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0025_chitiet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='uploader',
        ),
    ]