# Generated by Django 3.1.6 on 2021-02-16 19:47

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210215_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicar',
            name='conteudo',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Conteudo'),
        ),
    ]
