# Generated by Django 2.2 on 2019-10-25 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20191025_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='other_image',
            field=models.ImageField(blank=True, default='', null=True, upload_to=''),
        ),
    ]
