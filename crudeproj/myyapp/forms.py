from django import forms
from .models import Appointment, Reminder

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['title', 'description', 'date', 'time', 'location', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].widget = forms.Select(choices=Appointment.status_choices)
        
class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['reminder_time']   