# Generated by Django 2.2.9 on 2019-12-20 19:56

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_emailsettings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='', help_text='Ingrese email a donde llegarán los datos de contacto enviados por el formulario', max_length=254, verbose_name='Email')),
                ('parent', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_setting', to='home.EmailSettings')),
            ],
        ),
    ]
