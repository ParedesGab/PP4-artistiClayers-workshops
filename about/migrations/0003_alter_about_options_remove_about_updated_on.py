# Generated by Django 4.2.20 on 2025-04-09 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_rename_content_about_description_about_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={},
        ),
        migrations.RemoveField(
            model_name='about',
            name='updated_on',
        ),
    ]
