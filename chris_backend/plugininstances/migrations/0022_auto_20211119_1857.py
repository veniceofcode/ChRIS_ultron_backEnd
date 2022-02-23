# Generated by Django 2.2.24 on 2021-11-19 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugininstances', '0021_plugininstance_error_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='plugininstance',
            name='size',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='plugininstance',
            name='raw',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='plugininstance',
            name='summary',
            field=models.CharField(blank=True, max_length=4000),
        ),
    ]