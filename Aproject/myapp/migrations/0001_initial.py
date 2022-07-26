# Generated by Django 4.0.5 on 2022-07-29 12:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookLibrary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('about', models.TextField()),
                ('category', models.CharField(max_length=10)),
                ('author', models.CharField(max_length=500)),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'book_library',
            },
        ),
    ]
