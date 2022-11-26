# Generated by Django 4.1.3 on 2022-11-24 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0002_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='image_height',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='map',
            name='image_width',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='map',
            name='map_image',
            field=models.ImageField(height_field='image_height', upload_to='upload/', width_field='image_width'),
        ),
    ]
