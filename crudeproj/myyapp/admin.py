from django.contrib import admin
from .models import Appointment, Reminder

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'location', 'time', 'description', 'date', 'status', 'assigned_to')
    list_filter = ('date', 'assigned_to')
    search_fields = ('title', 'description', 'location')
    date_hierarchy = 'date'

admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Reminder)