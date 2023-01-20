# Generated by Django 4.1.3 on 2023-01-20 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0019_rename_char_desc_character_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='type',
            field=models.CharField(choices=[('Settlements', (('city', 'City'), ('town', 'Town'), ('village', 'Village'), ('other', 'Other'))), ('Structures', (('castle', 'Castle'), ('fort', 'fort'), ('tower', 'Tower'), ('ruin', 'Ruin'), ('house', 'House'), ('landmark', 'Landmark'), ('other', 'Other'))), ('Nature', (('mountain', 'Mountain'), ('cave', 'Cave'), ('wood', 'Wood'), ('water', 'Water'), ('landmark', 'Landmark'), ('other', 'Other'))), ('Other', (('point of interest', 'Point of Interest'), ('other', 'Other')))], default='other', max_length=25),
        ),
    ]