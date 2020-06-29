# Generated by Django 3.0.7 on 2020-06-27 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200627_1708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mission',
            old_name='about_image',
            new_name='image',
        ),
        migrations.AddField(
            model_name='mission',
            name='font',
            field=models.CharField(choices=[('icofont-computer', 'bilgisayar'), ('icofont-chart-bar-graph', 'grafik'), ('icofont-image', 'resim'), ('icofont-settings', 'ayar'), ('icofont-earth', 'dünya'), ('icofont-tasks-alt', 'alt görev'), ('icofont-award', 'ödül'), ('icofont-clock-time', 'saat'), ('icofont-document-folder', 'dosya'), ('icofont-simple-smile', 'gülücük'), ('ri-brush-4-line', 'mission'), ('ri-movie-2-line', 'film şeridi'), ('ri-calendar-check-line', 'takvim')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]