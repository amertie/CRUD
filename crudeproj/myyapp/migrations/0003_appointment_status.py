# Generated by Django 5.0.1 on 2024-02-27 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myyapp', '0002_appointment_delete_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('COMPLETED', 'Completed')], default='PENDING', max_length=20),
        ),
    ]
