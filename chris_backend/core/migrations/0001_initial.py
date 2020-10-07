# Generated by Django 2.2.12 on 2020-09-22 21:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChrisInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default='ChRIS instance', max_length=100)),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('description', models.CharField(blank=True, max_length=600)),
            ],
            options={
                'verbose_name': 'ChRIS instance',
                'verbose_name_plural': 'ChRIS instance',
            },
        ),
    ]