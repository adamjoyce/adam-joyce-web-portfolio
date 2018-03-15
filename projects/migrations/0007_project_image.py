# Generated by Django 2.0.2 on 2018-03-14 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20180314_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, help_text='Site image for project page.', upload_to='projects/project_images'),
        ),
    ]
