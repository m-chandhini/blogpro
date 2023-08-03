# Generated by Django 4.2.3 on 2023-08-01 06:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='image2',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='image3',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images'),
            preserve_default=False,
        ),
    ]
