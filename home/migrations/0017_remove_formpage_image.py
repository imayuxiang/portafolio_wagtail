# Generated by Django 2.2.9 on 2019-12-23 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formpage',
            name='image',
        ),
    ]
