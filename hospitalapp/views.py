from django.http import HttpResponse
from django.shortcuts import render
from .models import Department, Doctor
from .forms import BookingForm

# Create your views here.

def index(request):
    numbers = {
        'num1': '10',
    }
    return render(request, 'index.html', numbers)

def about(request):
    return render(request, 'about.html')

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'conformation.html')
            form = BookingForm()
    else:
        form = BookingForm()

    dict_form = {
        'form': form
    }

    return render(request, 'booking.html', dict_form)

def doctors(request):
    dict_docs = {
        'doctors': Doctor.objects.all()
    }
    return render(request, 'doctors.html', dict_docs)

def contact(request):
    return render(request, 'contact.html')

def department(request):
    dict_dept = {
        'dept': Department.objects.all()
    }
    return render(request, 'department.html', dict_dept)
