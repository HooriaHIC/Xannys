# Generated by Django 2.2 on 2019-10-27 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_remove_item_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='size',
            field=models.CharField(choices=[('xs', 'Extra small'), ('s', 'Small'), ('m', 'Medium'), ('l', 'Large'), ('xl', 'Extra Large')], default='S', max_length=1),
            preserve_default=False,
        ),
    ]
