# Generated by Django 2.2 on 2019-11-07 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20191107_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='size',
        ),
    ]
