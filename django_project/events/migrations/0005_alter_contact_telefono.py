# Generated by Django 4.1.3 on 2024-12-05 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='telefono',
            field=models.IntegerField(),
        ),
    ]
