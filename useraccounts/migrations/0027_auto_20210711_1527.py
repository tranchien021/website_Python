# Generated by Django 3.2.4 on 2021-07-11 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0026_remove_question_uploader'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='course',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='teacher',
            name='exp',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='teacher',
            name='follow',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='teacher',
            name='review',
            field=models.TextField(default=''),
        ),
    ]