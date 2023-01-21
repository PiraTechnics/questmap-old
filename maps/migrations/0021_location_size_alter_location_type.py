# Generated by Django 4.1.3 on 2023-01-20 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0020_location_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='size',
            field=models.CharField(choices=[('tiny', 'Tiny'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large'), ('huge', 'Huge'), ('gigantic', 'Gigantic')], default='small', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='location',
            name='type',
            field=models.CharField(choices=[('Settlements', (('city', 'City'), ('town', 'Town'), ('village', 'Village'), ('camp', 'Camp'))), ('Structures', (('castle', 'Castle'), ('fort', 'Fort'), ('tower', 'Tower'), ('ruin', 'Ruin'), ('house', 'House'), ('misc structure', 'Misc Structure'))), ('Nature', (('mountain', 'Mountain'), ('hill', 'Hill'), ('valley', 'Valley'), ('cavern', 'Cavern'), ('wood', 'Wood'), ('water', 'Water'), ('misc landform', 'Misc Landform'))), ('Other', (('point of interest', 'Point of Interest'), ('landmark', 'Landmark'), ('other', 'Other')))], max_length=25),
        ),
    ]
