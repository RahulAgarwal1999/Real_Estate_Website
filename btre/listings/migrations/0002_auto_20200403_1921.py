# Generated by Django 3.0 on 2020-04-03 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='prize',
            new_name='price',
        ),
    ]