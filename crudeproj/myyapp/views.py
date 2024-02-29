from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment, Reminder
from .forms import AppointmentForm, ReminderForm
from django.http import HttpResponse
from django.contrib import messages

def appointment_list(request):
    status = request.GET.get('status', 'all')
    if status == 'all':
        appointments = Appointment.objects.all()
    else:
        appointments = Appointment.objects.filter(status=status)
    
    any_reminders = any(appointment.reminder_set.exists() for appointment in appointments)
    
    return render(request, 'appointment_list.html', {'appointments': appointments, 'status': status, 'any_reminders': any_reminders})



def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointment_form.html', {'form': form})

def appointment_update(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointment_update_form.html', {'form': form, 'appointment': appointment})

def appointment_delete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'appointment_confirm_delete.html', {'appointment': appointment})

def save_reminder(request):
    if request.method == 'POST':
        reminder_text = request.POST.get('reminder_text')
        return HttpResponse("Reminder saved successfully!")
    else:
        return HttpResponse("This view is for saving reminders. Please submit a POST request with the reminder data.")

def set_reminder_create(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.appointment = appointment
            reminder.save()
            messages.success(request, 'Reminder saved successfully!')
            return redirect('appointment_list')  
    else:
        form = ReminderForm()
    return render(request, 'set_reminder_create.html', {'form': form, 'appointment': appointment})

def set_reminder_list(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    reminders = Reminder.objects.filter(appointment=appointment)
    return render(request, 'set_reminder_list.html', {'appointment': appointment, 'reminders': reminders, 'appointment_id': appointment_id})

def set_reminder_update(request, reminder_id):
    reminder = get_object_or_404(Reminder, pk=reminder_id)
    if request.method == 'POST':
        form = ReminderForm(request.POST, instance=reminder)
        if form.is_valid():
            form.save()
            return redirect('set_reminder_list', appointment_id=reminder.appointment_id)
    else:
        form = ReminderForm(instance=reminder)
    return render(request, 'set_reminder_form.html', {'form': form, 'reminder': reminder})

def set_reminder_delete(request, reminder_id):
    reminder = get_object_or_404(Reminder, pk=reminder_id)
    if request.method == 'POST':
        appointment_id = reminder.appointment_id
        reminder.delete()
        return redirect('set_reminder_list', appointment_id=appointment_id)
    return render(request, 'set_reminder_confirm_delete.html', {'reminder': reminder})
