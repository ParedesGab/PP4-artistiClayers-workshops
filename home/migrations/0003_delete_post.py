# Generated by Django 4.2.20 on 2025-04-15 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_post_featured_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
