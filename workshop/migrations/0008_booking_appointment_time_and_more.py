# Generated by Django 4.2.20 on 2025-04-15 09:07

from django.db import migrations, models
import workshop.models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0007_alter_booking_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='appointment_time',
            field=models.CharField(choices=[('9am-11am', '9am - 11am'), ('1pm-3pm', '1pm - 3pm'), ('7pm-9pm', '7pm - 9pm')], default='9am-11am', max_length=10),
        ),
        migrations.AlterField(
            model_name='booking',
            name='appointment_date',
            field=models.DateField(validators=[workshop.models.validate_date_not_in_past]),
        ),
    ]
