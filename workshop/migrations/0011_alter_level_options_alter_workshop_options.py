# Generated by Django 4.2.20 on 2025-04-22 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0010_alter_booking_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='level',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='workshop',
            options={'ordering': ['level']},
        ),
    ]
