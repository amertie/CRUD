# Generated by Django 5.0.1 on 2024-02-28 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myyapp', '0004_alter_appointment_location_alter_appointment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='assigned_to',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
