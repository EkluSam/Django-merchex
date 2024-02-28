# Generated by Django 5.0.2 on 2024-02-26 14:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_rename_listings_listing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='name',
            new_name='description',
        ),
        migrations.AddField(
            model_name='listing',
            name='sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='listing',
            name='title',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='type',
            field=models.CharField(choices=[('Misc', 'Misc')], default='', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='year',
            field=models.IntegerField(default=200, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2024)]),
            preserve_default=False,
        ),
    ]
