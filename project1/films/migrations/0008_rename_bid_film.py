# Generated by Django 4.0.5 on 2022-08-08 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0007_rename_film_bid'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BID',
            new_name='Film',
        ),
    ]
