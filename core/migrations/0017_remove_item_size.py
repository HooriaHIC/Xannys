# Generated by Django 2.2 on 2019-10-27 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20191026_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='size',
        ),
    ]
