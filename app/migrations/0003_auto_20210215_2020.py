# Generated by Django 3.1.6 on 2021-02-15 19:20

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_publicar_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicar',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='publicar',
            name='conteudo',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='publicar',
            name='imagem',
            field=models.ImageField(blank=True, default='/placeholder2.png', null=True, upload_to='images', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='publicar',
            name='sub_titulo',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Subtitulo'),
        ),
        migrations.AlterField(
            model_name='publicar',
            name='titulo',
            field=models.CharField(max_length=200, verbose_name='Titulo'),
        ),
    ]
