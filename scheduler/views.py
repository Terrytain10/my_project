# Create your views here.

from django.shortcuts import render, redirect
from .models import Appointment

def appointment_list(request):
    appointments = Appointment.objects.all().order_by('date', 'time')
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        time = request.POST.get('time')
        if title and date and time:
            Appointment.objects.create(
                title=title,
                description=description,
                date=date,
                time=time
            )
            return redirect('appointment_list')
    return render(request, 'scheduler/index.html', {'appointments': appointments})
