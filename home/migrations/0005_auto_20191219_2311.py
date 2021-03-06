# Generated by Django 2.2.9 on 2019-12-19 23:11

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('mainblock', wagtail.core.blocks.StructBlock([('bg_imagen', wagtail.images.blocks.ImageChooserBlock(help_text='Seleccione una imagen para el fondo de la secciond e bienvenida. Se recomienda imagen de 1910x1055', label='Imagen de fondo de seccion', required=True)), ('message_welcome', wagtail.core.blocks.CharBlock(label='Mensaje de Bienvenida: ')), ('sub_title', wagtail.core.blocks.CharBlock(help_text='Para efectos de la animacion se debe seperar por comas. Ejemplo: CEO DevFolio,Web Developer,Web Designer,Frontend Developer,Graphic Designer', label='Subtitulo de Mensaje de Bienvenida: '))]))], blank=True, null=True),
        ),
    ]
