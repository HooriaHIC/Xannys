# Generated by Django 2.2 on 2019-10-25 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_remove_item_other_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='item',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='item',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='item',
            name='img4',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='item',
            name='img5',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
