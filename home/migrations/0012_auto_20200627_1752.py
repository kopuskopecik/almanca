# Generated by Django 3.0.7 on 2020-06-27 14:52

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20200627_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='feature',
            name='title',
        ),
        migrations.AddField(
            model_name='feature',
            name='font_title',
            field=models.CharField(default=1, max_length=50, verbose_name='Başlık:'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feature',
            name='ranking',
            field=models.SmallIntegerField(default=1, unique=True, verbose_name='sıralama'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feature',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='İçerik'),
        ),
    ]