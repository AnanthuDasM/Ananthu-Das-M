# Generated by Django 3.2.11 on 2022-01-18 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2021-11-10'),
            preserve_default=False,
        ),
    ]
