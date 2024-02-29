from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Appointment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    status_choices = [
        ('completed', 'Completed'),
        ('pending', 'Pending'),
    ]
    status = models.CharField(max_length=20, choices=status_choices)
    assigned_to = models.IntegerField(null=True, blank=True) 

    def __str__(self):
        return self.title
    
    
class Reminder(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    appointment_number = models.CharField(max_length=50)
    appointment_title = models.CharField(max_length=100)
    reminder_time = models.DateTimeField()

    def __str__(self):
        return f'Reminder for {self.appointment.title} at {self.reminder_time}'